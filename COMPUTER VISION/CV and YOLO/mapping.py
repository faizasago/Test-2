import cv2
import numpy as np
from ultralytics import YOLO

# Path to the trained YOLOv8 model
MODEL_PATH = "path/to/your/trained_yolov8_model.pt"

# Load YOLOv8 model
model = YOLO(MODEL_PATH)

# Initialize webcam
web_cam = cv2.VideoCapture(0)
if not web_cam.isOpened():
    print("Error: Unable to access the webcam.")
    exit()

# Create a blank map canvas for visualization
map_canvas = np.zeros((500, 500, 3), dtype=np.uint8)  # Adjust size as needed

def map_walls(boxes, map_canvas):
    """
    Update the 2D map with wall points based on bounding boxes.
    :param boxes: List of detected bounding boxes.
    :param map_canvas: Canvas to draw the map.
    """
    for box in boxes:
        x1, y1, x2, y2 = map(int, box[:4])  # Bounding box coordinates
        center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2  # Approximate wall center

        # Scale and map to the 2D canvas
        scaled_x = int(center_x / web_cam.get(cv2.CAP_PROP_FRAME_WIDTH) * map_canvas.shape[1])
        scaled_y = int(center_y / web_cam.get(cv2.CAP_PROP_FRAME_HEIGHT) * map_canvas.shape[0])

        # Draw a point on the map for the detected wall
        cv2.circle(map_canvas, (scaled_x, scaled_y), 3, (0, 255, 0), -1)  # Green points

while True:
    ret, frame = web_cam.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Perform wall detection using YOLOv8
    results = model.predict(frame, conf=0.5, device="cpu")

    # Extract detected bounding boxes
    boxes = []
    for result in results:
        for box in result.boxes:
            boxes.append(box.xyxy[0].tolist())  # Get bounding box coordinates

    # Visualize detections on the video frame
    for box in boxes:
        x1, y1, x2, y2 = map(int, box[:4])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box for walls
        cv2.putText(frame, "Wall", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Update the 2D map
    map_walls(boxes, map_canvas)

    # Display the video frame and 2D map
    cv2.imshow("Wall Detection", frame)
    cv2.imshow("2D Wall Map", map_canvas)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
web_cam.release()
cv2.destroyAllWindows()
