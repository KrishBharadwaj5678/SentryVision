[English](README.md) | **Português** | [日本語](README.ja.md) | [Русский](README.ru.md)

# 👁️ Sentry Vision

Sentry Vision é um projeto de visão computacional que utiliza **YOLOv8**, **OpenCV** e **Pygame** para detectar objetos em tempo real através de uma webcam e acionar alertas quando objetos específicos são identificados.

![SentryVisionDemo](https://github.com/KrishBharadwaj5678/SentryVision/blob/main/SentryVisionDemo.jpg)

## 🚀 Funcionalidades

| Funcionalidade                       | Descrição                                        |
| ------------------------------------ | ------------------------------------------------ |
| 🎯 Detecção de objetos em tempo real | Usa YOLOv8 para detecção instantânea de objetos  |
| 📷 Monitoramento ao vivo da webcam   | Processa o fluxo de vídeo usando OpenCV          |
| 🔔 Sistema de alerta sonoro          | Reproduz um som quando o objeto alvo é detectado |
| 🖼️ Captura de evidências            | Salva automaticamente imagens anotadas           |
| 📧 Sistema de notificação por e-mail | Envia alertas com imagens anexadas               |
| ⚡ Desempenho leve                    | Otimizado para inferência em tempo real          |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia              | Descrição                                               |
| ----------------------- | ------------------------------------------------------- |
| 🐍 Píton               | Linguagem principal de programação                      |
| 🧠 YOLOv8 (Ultralytics) | Modelo de aprendizado profundo para detecção de objetos |
| 📷 OpenCV               | Captura de vídeo e processamento de imagens             |
| 🔊 Pygame               | Sistema de alerta sonoro                                |
| 📧 SMTP (smtplib)       | Sistema de notificação por e-mail                       |

---

## ⚙️ Instalação

### 1️⃣ Clone o repositório

```bash id="4fj5ht"
git clone https://github.com/KrishBharadwaj5678/SentryVision.git
```

### 2️⃣ Navegue até a pasta do projeto

```bash id="2kv8pc"
cd SentryVision
```

### 3️⃣ Configure as variáveis de ambiente

Crie um arquivo `.env` no diretório raiz do projeto:

```env id="j5r9qe"
SENDER_EMAIL=seu email remetente
RECEIVER_EMAIL=email destinatário
EMAIL_PASS=sua senha de aplicativo
```

### 4️⃣ Instale as dependências

```bash id="4v5m8q"
pip install -r requirements.txt
```

### 5️⃣ Execute o projeto

```bash id="8s7nwd"
python app.py
```
