[English](README.md) | [Português](README.pt.md) | **日本語** | [Русский](README.ru.md)

# 👁️ セントリービジョン

セントリービジョン は、**YOLOv8**、**OpenCV**、および **Pygame** を使用して、ウェブカメラを通じてリアルタイムで物体を検出し、特定の物体が識別された際にアラートを発するコンピュータビジョンプロジェクトです。

![セントリービジョン](https://github.com/KrishBharadwaj5678/SentryVision/blob/main/SentryVisionDemo.jpg)

## 🚀 特徴

| 機能             | 説明                     |
| -------------- | ---------------------- |
| 🎯 リアルタイム物体検出  | YOLOv8 を使用した高速な物体検出    |
| 📷 ライブウェブカメラ監視 | OpenCV を使用して映像ストリームを処理 |
| 🔔 音声アラートシステム  | 対象物体を検出するとサウンドを再生      |
| 🖼️ 証拠画像の保存    | 注釈付き画像を自動的に保存          |
| 📧 メール通知システム   | 画像添付付きの検出アラートを送信       |
| ⚡ 軽量パフォーマンス    | リアルタイム推論向けに最適化         |

---

## 🛠️ 使用技術

| 技術                      | 説明            |
| ----------------------- | ------------- |
| 🐍 パイソン              | メインプログラミング言語  |
| 🧠 YOLOv8（ウルトラリティクス） | 物体検出用の深層学習モデル |
| 📷 OpenCV               | 映像取得および画像処理   |
| 🔊 Pygame               | 音声アラートシステム    |
| 📧 SMTP (smtplib)       | メール通知システム     |

---

## ⚙️ インストール

### 1️⃣ リポジトリをクローン

```bash
git clone https://github.com/KrishBharadwaj5678/SentryVision.git
```

### 2️⃣ プロジェクトフォルダへ移動

```bash
cd SentryVision
```

### 3️⃣ 環境変数を設定

プロジェクトのルートディレクトリに `.env` ファイルを作成してください：

```env
SENDER_EMAIL=送信者メールアドレス
RECEIVER_EMAIL=受信者メールアドレス
EMAIL_PASS=アプリパスワード
```

### 4️⃣ 依存関係をインストール

```bash
pip install -r requirements.txt
```

### 5️⃣ プロジェクトを実行

```bash
python app.py
```
