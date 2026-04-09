# 🚀 AI Virtual Drag & Drop using Hand Gestures

This project implements a real-time gesture-controlled drag-and-drop system using computer vision.

Instead of a traditional mouse, users can interact with on-screen elements using hand gestures captured via webcam.

---

## 🧠 Key Features
- ✋ Real-time hand tracking using MediaPipe  
- 📍 Detection of 21 hand landmarks  
- 🤏 Pinch gesture to drag and move objects  
- 🖐️ Three-finger gesture to create new objects  
- 🎯 Smooth mapping of hand coordinates to screen interaction  

---

## ⚙️ Tech Stack
- Python  
- OpenCV  
- MediaPipe (Hand Landmarker - Tasks API)  
- NumPy  

---

## 🧩 How It Works
- Webcam captures live video using OpenCV  
- Frames are processed and passed to MediaPipe  
- Hand landmarks are detected and converted to pixel coordinates  
- Distance between thumb and index finger is calculated for pinch detection  
- Finger position logic is used to detect gestures  
- Objects are dynamically updated based on hand movement  

---

## 🎮 Controls
- 🤏 **Pinch (Thumb + Index)** → Drag objects  
- 🖐️ **Three Fingers Up** → Create new box  

---

## 📦 Installation
```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ Run the Project
```bash
python main.py
```

---

## 📌 Requirements
- Webcam  
- Python 3.8+  

---

## 🌟 Future Improvements
- Multi-hand support  
- Gesture-based resizing  
- UI enhancements  
- Integration with AR/VR systems  

---

## 🤝 Contributing
Feel free to fork this repo and build your own ideas on top of it.

---

## 📢 Connect
If you liked this project, feel free to connect and follow my journey of building AI projects every day 🚀
