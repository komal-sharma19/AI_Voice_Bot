# 🤖 Talrn Voice Bot

An intelligent and empathetic AI voice bot that analyzes sentiment in your messages and responds with context-aware, natural-sounding audio responses.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-4285F4.svg)
![VADER](https://img.shields.io/badge/VADER-Sentiment-orange.svg)
![gTTS](https://img.shields.io/badge/gTTS-Text--to--Speech-yellow.svg)

## 📋 Overview

Talrn Voice Bot is an interactive web application that combines sentiment analysis with AI-powered response generation. Simply type a message, and the bot will:

1. Analyze the emotional sentiment (positive, negative, or neutral)
2. Generate an empathetic, conversational response using Google's Gemini AI
3. Convert the response to speech and play it back automatically

## ✨ Features

- **Real-time Sentiment Analysis**: Uses VADER Sentiment to detect emotional tone
- **AI-Powered Responses**: Leverages Google Gemini for natural, context-aware replies
- **Text-to-Speech**: Converts responses to audio using Google Text-to-Speech (gTTS)
- **Auto-play Audio**: Automatic playback of bot responses
- **Quick Examples**: Pre-loaded example messages for testing
- **User-Friendly Interface**: Clean, intuitive Streamlit-based UI

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: Interactive web interface
- **[Google Gemini AI](https://deepmind.google/technologies/gemini/)**: Advanced language model for response generation
- **[VADER Sentiment](https://github.com/cjhutto/vaderSentiment)**: Sentiment analysis engine
- **[gTTS](https://gtts.readthedocs.io/)**: Google Text-to-Speech for audio generation
- **Python 3.8+**: Core programming language

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini AI

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/komal-sharma19/talrn-voice-bot.git
   cd talrn-voice-bot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**
   
   Create a `.streamlit` folder in the project root and add a `secrets.toml` file:
   ```bash
   mkdir .streamlit
   ```
   
   Create `.streamlit/secrets.toml` with your Google API key:
   ```toml
   GOOGLE_API_KEY = "your-google-api-key-here"
   ```

5. **Add bot image**
   
   Place a `bot.jpeg` image file in the project root directory for the bot avatar.

## 🚀 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the interface**
   
   Open your browser and navigate to `http://localhost:8501`

3. **Interact with the bot**
   - Type your message in the text input field
   - Or click one of the example buttons (Positive, Negative, Neutral)
   - Press "Send" to get the bot's response
   - Listen to the automatic audio playback

## 📁 Project Structure

```
talrn-voice-bot/
│
├── app.py                  # Main application file
├── bot.jpeg               # Bot avatar image
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
└── .streamlit/
    └── secrets.toml      # API keys (not in repo)
```

## 📝 Requirements.txt

```txt
streamlit>=1.28.0
vaderSentiment>=3.3.2
gTTS>=2.3.0
google-generativeai>=0.3.0
```

## 🔧 Configuration

### Sentiment Analysis Thresholds

The bot uses VADER's compound score to determine sentiment:
- **Positive**: compound score ≥ 0.05
- **Negative**: compound score ≤ -0.05
- **Neutral**: compound score between -0.05 and 0.05

### AI Persona

Talrn is designed to be:
- Friendly and empathetic
- An active listener
- Brief and natural (1-2 sentences)
- Supportive without being preachy

## 🔒 Safety & Privacy

The bot is programmed with safety guidelines:
- Does not provide medical, legal, or financial advice
- Avoids asking personal or intrusive questions
- Maintains a non-judgmental tone
- Respects user privacy

## 🚀 Future Improvements

Here are some planned enhancements for future versions:

- **🎙️ Voice Input**: Add speech-to-text functionality for hands-free interaction
- **🌍 Multi-language Support**: Expand beyond English to support multiple languages
- **💬 Conversation History**: Implement chat memory to maintain context across messages
- **🎨 Custom Voice Options**: Allow users to choose different voice styles and accents

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👩‍💻 Author

**Komal Sharma**

- **LinkedIn**: [k-sharma19](https://www.linkedin.com/in/k-sharma19/)
- **Email**: 1908.komalsharma@gmail.com
- **Location**: Kanpur, Uttar Pradesh

## 🙏 Acknowledgments

- Google for the Gemini AI API and gTTS
- VADER Sentiment Analysis tool
- Streamlit for the amazing framework
- The open-source community

## 📞 Support

For issues, questions, or suggestions, please:
- Open an issue on GitHub
- Contact via email: 1908.komalsharma@gmail.com

---

⭐ If you found this project helpful, please consider giving it a star on GitHub!