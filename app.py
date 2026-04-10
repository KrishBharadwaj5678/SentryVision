from ultralytics import YOLO
import cv2
import pygame
import time

# Load Music
pygame.mixer.init()
pygame.mixer.music.load("sounds/alert.mp3")

# Load Model
model = YOLO("yolov8n.pt")

# Video Capture
cap = cv2.VideoCapture(0)

sound_played = False
target_object = "cell phone"

while True:
    ret, frame = cap.read()

    results = model(frame)
    annotated_frame = results[0].plot()

    # Check Detection
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        name = model.names[class_id]

        if name == target_object and not sound_played:
            # Capture evidence
            cv2.imwrite(f"detected_{time.time()}.jpg",annotated_frame)
            # Play the sound
            pygame.mixer.music.play()
            sound_played = True

    # Show the image
    cv2.imshow("Object Detection",annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()