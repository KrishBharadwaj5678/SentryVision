# 👁️ Sentry Vision

Sentry Vision is a computer vision project that uses **YOLOv8**, **OpenCV**, and **Pygame** to detect objects in real-time through a webcam and trigger alerts when specific objects are identified.

![SentryVisionDemo](https://github.com/KrishBharadwaj5678/SentryVision/blob/main/SentryVisionDemo.jpg)

## 🚀 Features

| Feature                       | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| 🎯 Real-time object detection | Uses YOLOv8 for instant object detection from webcam feed |
| 📷 Live webcam monitoring     | Processes video stream using OpenCV                       |
| 🔔 Audio alert system         | Plays sound when target object is detected                |
| 🖼️ Evidence capture          | Saves annotated images automatically                      |
| 📧 Email notification system  | Sends detection alerts with image attachments             |
| ⚡ Lightweight performance     | Optimized for real-time inference                         |

---

## 🛠️ Tech Stack

| Technology              | Description                              |
| ----------------------- | ---------------------------------------- |
| 🐍 Python               | Core programming language                |
| 🧠 YOLOv8 (Ultralytics) | Deep learning model for object detection |
| 📷 OpenCV               | Video capture and image processing       |
| 🔊 Pygame               | Audio alert system                       |
| 📧 SMTP (smtplib)       | Email notification system                |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/KrishBharadwaj5678/SentryVision.git
cd SentryVision
```

### 2. Set up environment variables (important)

Create a `.env` file in the project root directory:

```env
SENDER_EMAIL=sender email
RECEIVER_EMAIL=receiver email
EMAIL_PASS=your app password
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python app.py
```

---

## Contributing 🤝

Want to contribute? Here's how:

1. 🍴 Fork the repository.
2. 🌿 Create a new branch (`git checkout -b feature-name`).
3. ✍️ Make your changes and commit them (`git commit -am 'Add feature-name'`).
4. 🚀 Push to your branch (`git push origin feature-name`).
5. 🔄 Submit a pull request to merge into the main branch.
