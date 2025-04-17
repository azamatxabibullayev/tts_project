# 🎙️ TTS Project Bot

This is a Telegram bot built using Python and Aiogram that allows users to contribute their voice recordings for
specific PDF documents. It's part of a Text-To-Speech (TTS) project that aims to gather voice samples for training or
informative use cases.

## 💡 Features

- 📄 PDF selection: Users choose a document from a list of available PDFs.
- 🎤 Voice recording: Users record their voice reading the selected document.
- ✅ Confirmation: Before sending, users confirm their audio recording.
- 📩 Submission: Upon confirmation, the bot sends the audio file along with user details and the selected PDF name to a
  private admin group.
- 🔒 Secure: All sensitive data (bot token, admin group ID, PDF metadata) is managed via a `.env` file and excluded from
  version control.

## 🧑‍💻 Tech Stack

- **Language:** Python
- **Framework:** [Aiogram v3](https://docs.aiogram.dev/)
- **Bot API:** Telegram
- **Deployment:** Local or server (e.g., VPS)