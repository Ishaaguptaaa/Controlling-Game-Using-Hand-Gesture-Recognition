# 🖐️ Hand Gesture Controlled Game using YOLO and PyAutoGUI

This project uses **YOLO (You Only Look Once)** object detection to recognize custom hand gestures from a webcam feed and maps those gestures to **keyboard controls** (left, right, and up) using **PyAutoGUI**. This allows you to control a game using just your hand gestures!

## 🎯 Project Objective

Train a **custom YOLO model** to detect 3 specific hand gestures:

- ✊ **Closed Fist** → Move **Left**
- ✋ **Open Palm** → Move **Right**
- 🤏 **Finger Curl** → Move **Up**

These gestures simulate arrow key presses in any game or application that responds to keyboard input.

---

## 📁 Dataset

We created a custom dataset with labeled images for:

1. `closed_fist`
2. `open_palm`
3. `finger_curl`

The dataset was annotated in YOLO format and split into training and validation sets.

---

## 🧠 Model Training

We used a YOLO variant (YOLOv5/YOLOv8 - update as per your version) for training on the custom gesture dataset.

### Steps:

1. Annotated the dataset using tools like Roboflow or LabelImg.
2. Trained the YOLO model with custom classes.
3. Validated the model performance on unseen images.
4. Exported the trained model for inference.

---

## 🧪 Real-Time Inference

The trained YOLO model is used to detect hand gestures in **real-time** via webcam. Detected gestures are mapped to keyboard keys using `pyautogui`.

| Gesture       | Action       |
|---------------|--------------|
| Closed Fist   | ⬅️ Left Arrow |
| Open Palm     | ➡️ Right Arrow|
| Finger Curl   | ⬆️ Up Arrow   |

