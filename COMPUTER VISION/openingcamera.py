import cv2

# Create a VideoCapture object
web_cam = cv2.VideoCapture(0)

while True:
    retrieve, frame = web_cam.read()
    cv2.imshow('Webcam', frame)
    
    # Wait for 'c' key to be pressed
    key = cv2.waitKey(20) & 0xFF
    if key == ord('c'):
        # Capture the frame and save it
        cv2.imwrite('captured_image.png', frame)
        print("Image captured!")
    elif key == ord('q'):  # Press 'q' to exit
        break

# Release the VideoCapture object
web_cam.release()
cv2.destroyAllWindows()