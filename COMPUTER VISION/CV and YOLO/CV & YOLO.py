import cv2
from ultralytics import YOLO

# Load the YOLOv8 model (replace with your custom-trained model if needed)
model = YOLO("yolov8n.pt")  # Use a YOLOv8 pre-trained model, e.g., yolov8n.pt

# Initialize webcam
web_cam = cv2.VideoCapture(0)

if not web_cam.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = web_cam.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Perform detection using YOLOv8
    results = model.predict(source=frame, save=False, conf=0.5)  # Adjust confidence threshold as needed

    # Extract detection results
    detections = results[0].boxes.xyxy  # Bounding box coordinates
    confidences = results[0].boxes.conf  # Confidence scores

    # Loop through detections and draw bounding boxes
    for (box, conf) in zip(detections, confidences):
        x1, y1, x2, y2 = map(int, box)  # Bounding box coordinates
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box
        label = f"Face: {conf:.2f}"  # Label with confidence
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("YOLOv8 Face Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
