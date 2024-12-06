import cv2

# Open the camera
cap = cv2.VideoCapture(0)  # Use the appropriate camera index

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Test capturing frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
