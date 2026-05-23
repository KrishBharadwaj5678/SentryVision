[English](README.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

# 👁️ Sentry Vision

Sentry Vision is a computer vision project that uses **YOLOv8**, **OpenCV**, and **Pygame** to detect objects in real-time through a webcam and trigger alerts when specific objects are identified.

![SentryVisionDemo](https://github.com/KrishBharadwaj5678/SentryVision/blob/main/SentryVisionDemo.jpg)

## 🚀 Features

| Feature                       | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| 🎯 Real-time object detection | Uses YOLOv8 for instant object detection                  |
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

### 1️⃣ Clone the repository

```bash id="j8n1v2"
git clone https://github.com/KrishBharadwaj5678/SentryVision.git
```

### 2️⃣ Navigate to the project folder

```bash id="g4p9kx"
cd SentryVision
```

### 3️⃣ Set up environment variables

Create a `.env` file in the project root directory:

```env id="w2f7mn"
SENDER_EMAIL=sender email
RECEIVER_EMAIL=receiver email
EMAIL_PASS=your app password
```

### 4️⃣ Install dependencies

```bash id="u6q3za"
pip install -r requirements.txt
```

### 5️⃣ Run the project

```bash id="r5c1de"
python app.py
```
