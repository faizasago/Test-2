import cv2
import pyttsx3
import speech_recognition as sr
from ultralytics import YOLO

# Initialize TTS engine
tts_engine = pyttsx3.init()

# Load the YOLOv8 model (ensure the model file is available)
model = YOLO("yolov8n.pt")  # Small YOLOv8 model for face detection

# Initialize webcam
web_cam = cv2.VideoCapture(0)

if not web_cam.isOpened():
    print("Error: Unable to access the webcam.")
    exit()

def text_to_speech(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def speech_to_text():
    """Recognize speech using the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            print("Speech not understood.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

def capture_and_tag_face():
    """Capture the user's face and tag it with their name."""
    text_to_speech("Please tell me your name.")
    name = speech_to_text()
    if not name:
        text_to_speech("Sorry, I didn't catch that. Please try again.")
        return

    text_to_speech(f"Hello {name}, I will now capture your face.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = web_cam.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Perform face detection using YOLOv8
        results = model.predict(source=frame, save=False, conf=0.5, device="cpu")

        # Loop through detections and draw bounding boxes
        for result in results:
            boxes = result.boxes  # Get bounding boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                conf = box.conf[0]  # Confidence score
                label = f"{name}: {conf:.2f}"  # Label with name and confidence

                # Draw the bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow("Face Detection with Tagging", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    text_to_speech("Face capture completed. Goodbye!")

def main():
    """Main function to handle the workflow."""
    text_to_speech("Say hello to start face detection.")
    command = speech_to_text()
    if command and "hello" in command:
        text_to_speech("Hello! Starting face detection.")
        capture_and_tag_face()
    else:
        text_to_speech("I didn't hear hello. Please try again.")

try:
    main()
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    # Release the webcam and close all windows
    web_cam.release()
    cv2.destroyAllWindows()
