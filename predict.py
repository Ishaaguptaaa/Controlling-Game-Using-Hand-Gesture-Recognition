# import cv2
# from ultralytics import YOLO

# # Load custom model
# model = YOLO(r'C:\Users\Isha Gupta\OneDrive\Desktop\Python\runs\detect\train6\weights\best.pt')
# print("Model Class Names:", model.names)  # Verify class IDs: 0=closed_fist, 1=open_palm, 2=finger_curl?

# webcam = cv2.VideoCapture(0)

# while True:
#     success, frame = webcam.read()
#     if not success: break
    
#     # Use predict() instead of track() for gesture detection
#     results = model.predict(frame, conf=0.4, imgsz=640)
    
#     # Get detection data
#     boxes = results[0].boxes
#     class_ids = boxes.cls.cpu().numpy()  # Gesture class IDs
#     confidences = boxes.conf.cpu().numpy()
    
#     # Custom annotation
#     annotated_frame = frame.copy()
#     for box, cls_id, conf in zip(boxes.xyxy, class_ids, confidences):
#         label = f"{model.names[int(cls_id)]} {conf:.2f}"
        
#         # Choose different colors per gesture
#         color = (0,255,0) if "open" in label else (0,0,255)  # Green for open, red for others
        
#         cv2.rectangle(annotated_frame, (int(box[0]), int(box[1])), 
#                      (int(box[2]), int(box[3])), color, 2)
#         cv2.putText(annotated_frame, label, (int(box[0]), int(box[1]-10)), 
#                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

#     # Display counts
#     counts = {name: sum(class_ids == i) for i, name in model.names.items()}
#     count_text = f"Fist: {counts.get('closed_fist',0)} | Palm: {counts.get('open_palm',0)} | Curl: {counts.get('finger_curl',0)}"
#     cv2.putText(annotated_frame, count_text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

#     cv2.imshow("Gesture Detection", annotated_frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

# webcam.release()
# cv2.destroyAllWindows()
import cv2
from ultralytics import YOLO
import pyautogui
import time

# Load custom model
model = YOLO(r'C:\Users\Isha Gupta\OneDrive\Desktop\Python\runs\detect\train6\weights\best.pt')
print("Model Class Names:", model.names)  # Verify class IDs

webcam = cv2.VideoCapture(0)

# To avoid repeated key presses, keep track of last pressed gesture
last_gesture = None
gesture_cooldown = 1.0  # seconds
last_time = time.time()

while True:
    success, frame = webcam.read()
    if not success:
        break
    
    results = model.predict(frame, conf=0.4, imgsz=640)
    boxes = results[0].boxes
    class_ids = boxes.cls.cpu().numpy()
    confidences = boxes.conf.cpu().numpy()
    
    annotated_frame = frame.copy()
    detected_gestures = set()
    
    for box, cls_id, conf in zip(boxes.xyxy, class_ids, confidences):
        label = model.names[int(cls_id)]
        detected_gestures.add(label)
        
        color = (0,255,0) if "open" in label else (0,0,255)
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(annotated_frame, f"{label} {conf:.2f}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    # Game control logic: send key press if a gesture is detected and cooldown passed
    current_time = time.time()
    if detected_gestures and (current_time - last_time) > gesture_cooldown:
        # Example priority: closed_fist > open_palm > finger_curl
        if "closed_fist" in detected_gestures:
            pyautogui.press('space')  # Jump 

            
            print("Action: Jump (space)")
            last_gesture = "closed_fist"
        elif "open_palm" in detected_gestures:
            pyautogui.press('right')  # Move right
            print("Action: Move Right (right arrow)")
            last_gesture = "open_palm"
        elif "finger_curl" in detected_gestures:
            pyautogui.press('left')  # Move left
            print("Action: Move Left (left arrow)")
            last_gesture = "finger_curl"
        last_time = current_time

    # Display counts on frame
    counts = {name: sum(class_ids == i) for i, name in model.names.items()}
    count_text = f"Fist: {counts.get('closed_fist',0)} | Palm: {counts.get('open_palm',0)} | Curl: {counts.get('finger_curl',0)}"
    cv2.putText(annotated_frame, count_text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Gesture Detection - Game Control", annotated_frame)
    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
