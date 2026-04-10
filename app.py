from ultralytics import YOLO
import cv2
import pygame
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import threading
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# SMPT Configuration
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("EMAIL_PASS")

# Load Music
pygame.mixer.init()
pygame.mixer.music.load("sounds/alert.mp3")

# Load Model
model = YOLO("yolov8n.pt")

# Video Capture
cap = cv2.VideoCapture(0)

sound_played = False
target_object = "cell phone"

def sendMail():
    # Create message
    msg = MIMEMultipart()
    msg["Subject"] = "🚨 Alert: Sentry Vision Event Triggered"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Email Body
    msg.attach(MIMEText("This is an automated notification to inform you that a target object "
    "has been successfully detected.\n"
    "Kindly review the attached image for further details.", "plain"))

    # Attach image
    with open("SentryVision.jpg", "rb") as img:
        mime_img = MIMEImage(img.read())
        mime_img.add_header("Content-Disposition", "attachment", filename="SentryVision.jpg")
        msg.attach(mime_img)

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

# OpenCV Loop
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
            cv2.imwrite(f"SentryVision.jpg",annotated_frame)

            # Play the sound
            pygame.mixer.music.play()
            sound_played = True

            # Run email in background thread. Threading means running multiple tasks at the same time (concurrently)
            threading.Thread(target=sendMail,daemon=True).start()

    # Show the image
    cv2.imshow("Object Detection",annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()