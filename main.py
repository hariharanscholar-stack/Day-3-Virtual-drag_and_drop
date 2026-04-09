import cv2
import mediapipe as mp
import numpy as np
import random
from math import hypot


BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1
)

landmarker = HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
frame_count = 0


boxes = []
for i in range(5):
    boxes.append({
        "pos":[random.randint(100,500), random.randint(100,300)],
        "color":(random.randint(50,255),random.randint(50,255),random.randint(50,255)),
        "size":80
    })

dragging_index = None
create_delay = 0

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    if not ret:
        break

    h,w,_ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = landmarker.detect_for_video(mp_image, frame_count)
    frame_count += 1

    pinch = False
    three_fingers = False
    ix,iy = 0,0

    if result.hand_landmarks:

        lm = result.hand_landmarks[0]

        thumb = lm[4]
        index = lm[8]
        middle = lm[12]
        ring = lm[16]

        tx,ty = int(thumb.x*w), int(thumb.y*h)
        ix,iy = int(index.x*w), int(index.y*h)
        mx,my = int(middle.x*w), int(middle.y*h)
        rx,ry = int(ring.x*w), int(ring.y*h)

        cv2.circle(frame,(ix,iy),10,(0,255,0),-1)
        cv2.circle(frame,(tx,ty),10,(255,0,0),-1)

        cv2.line(frame,(ix,iy),(tx,ty),(255,0,0),2)

        dist = hypot(ix-tx, iy-ty)

        
        if dist < 40:
            pinch = True

        
        if my < iy and ry < iy:
            three_fingers = True

    
    if three_fingers and create_delay == 0 and len(boxes) < 10:

        boxes.append({
            "pos":[random.randint(50, w-100), random.randint(50, h-150)],
            "color":(random.randint(50,255),random.randint(50,255),random.randint(50,255)),
            "size":80
        })

        create_delay = 30

    if create_delay > 0:
        create_delay -= 1

    
    if pinch:

        if dragging_index is None:

            for i,box in enumerate(boxes):

                x,y = box["pos"]
                s = box["size"]

                if x < ix < x+s and y < iy < y+s:
                    dragging_index = i
                    break

        if dragging_index is not None:
            boxes[dragging_index]["pos"] = [ix-40, iy-40]

    else:
        dragging_index = None

    
    for i,box in enumerate(boxes):

        x,y = box["pos"]
        s = box["size"]

        color = box["color"]

        if i == dragging_index:
            color = (0,255,0)

        cv2.rectangle(frame,(x,y),(x+s,y+s),color,-1)

    cv2.putText(frame,
                "AI VIRTUAL DRAG & DROP",
                (120,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,255),
                2)

    cv2.putText(frame,
                "Pinch = Drag | Three Fingers = Create Box",
                (10,450),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255,255,255),
                2)

    cv2.imshow("Virtual Drag & Drop", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()