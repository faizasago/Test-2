import cv2

# Load the cascade classifier for face detection
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a VideoCapture object
web_cam = cv2.VideoCapture(0)

# Load crosshair image
crosshair_img = cv2.imread('crosshair.png', cv2.IMREAD_UNCHANGED)

# Resize crosshair image to fit face
crosshair_height, crosshair_width, _ = crosshair_img.shape

while True:
    # Capture frame-by-frame
    ret, frame = web_cam.read()
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    # Draw rectangle around detected faces and display crosshair near the face
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        # Calculate position for crosshair
        crosshair_x = x + w // 2 - crosshair_width // 2
        crosshair_y = y + h // 2 - crosshair_height // 2
        
        # Display crosshair near the face
        for i in range(crosshair_height):
            for j in range(crosshair_width):
                if crosshair_img[i, j, 3] != 0:
                    frame[crosshair_y + i, crosshair_x + j, :3] = crosshair_img[i, j, :3]
    
    # Display the frame
    cv2.imshow('Webcam with Target', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
web_cam.release()
cv2.destroyAllWindows()