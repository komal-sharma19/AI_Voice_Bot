import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import time
import google.generativeai as genai 
import base64 

# --- API Key Configuration ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except (FileNotFoundError, KeyError):
    st.error("API Key not found. Please create a .streamlit/secrets.toml file with your GOOGLE_API_KEY.")
    st.stop()

# --- NEW: Autoplay Audio Function ---
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

# --- Core Functions (Unchanged) ---
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"

def generate_response_with_ai(sentiment, user_input):
    model = genai.GenerativeModel('gemini-flash-latest')
    prompt = f"""
## Persona & Goal
You are Talrn, a friendly and empathetic AI voice bot. Your primary goal is to be an active listener and make the user feel heard. Your responses should be short (1-2 sentences), natural-sounding, and supportive.

## Safety Rules
- You must not provide any medical, legal, or financial advice.
- You must not ask personal or intrusive questions.
- You must not generate responses that are preachy or judgmental.

## Examples of desired responses:
---
**User Message:** "I finally got the promotion I was working so hard for!"
**Sentiment:** positive
**Your Response:** That's absolutely fantastic news! All your hard work paid off, and you deserve it.
---
**User Message:** "The project failed and I feel like it's all my fault."
**Sentiment:** negative
**Your Response:** That sounds incredibly tough, and it's understandable to feel that way. Remember to be kind to yourself.
---
**User Message:** "I need to go to the grocery store later today."
**Sentiment:** neutral
**Your Response:** Okay, thanks for sharing. I hope you manage to get everything you need.
---
**User Message:** "I'm so tired, I just can't seem to get anything done."
**Sentiment:** negative
**Your Response:** It sounds like you're feeling really drained. It's okay to rest and recharge when you need to.
---

## Task
Now, generate a response for the following user message, following the persona, rules, and examples above.

**User Message:** "{user_input}"
**Sentiment:** {sentiment}
**Your Response:**
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.warning(f"AI response failed: {e}. Using a fallback response.")
        return "I'm here to listen. Could you please tell me more?"

def text_to_speech_gtts(text):
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        # Use a unique filename in a dedicated 'audio' folder if you want to manage them
        audio_file = f"response_{int(time.time())}.mp3"
        tts.save(audio_file)
        return audio_file
    except Exception as e:
        st.error(f"Failed to generate audio: {e}")
        return None

# --- UI Configuration ---
st.set_page_config(page_title="Talrn AI Voice Bot", layout="centered")
col1, col2 = st.columns([1, 8]) 
with col1:
    st.image("bot.jpeg", width=80)

with col2:
    st.title("Talrn-Voice-Bot") 
st.write("Type a message, or click an example to load it, then press Send.")

if 'audio_file' not in st.session_state:
    st.session_state.audio_file = None

# --- Main App Logic ---
def process_and_respond(text):
    if text and text.strip():
        st.session_state.audio_file = None
        with st.spinner("Thinking..."):
            sentiment = analyze_sentiment(text)
            bot_response = generate_response_with_ai(sentiment, text)
            st.info(f"**Detected Sentiment:** {sentiment.capitalize()}")
            st.success(f"**Bot's Response:** {bot_response}")
            audio_file_path = text_to_speech_gtts(bot_response)
            st.session_state.audio_file = audio_file_path
    else:
        st.warning("Please enter a message.")
        st.session_state.audio_file = None

# --- UI Elements ---
st.write("👇 Click an example to load it into the text box")
col1, col2, col3 = st.columns(3)

if col1.button("Positive Example ✨"):
    st.session_state.input = "I had a wonderful and productive day!"

if col2.button("Negative Example 😔"):
    st.session_state.input = "I'm feeling really stressed out about my workload."

if col3.button("Neutral Example 😐"):
    st.session_state.input = "The meeting is scheduled for 3 PM tomorrow."

user_input = st.text_input("Enter your message here:", key="input")

if st.button("Send", type="primary"):
    process_and_respond(user_input)

# --- Sidebar Content ---
with st.sidebar:
    st.header("About:")
    st.write("""
    This is Voice-Bot, an intelligent and empathetic AI Voice Bot. 
    
    Simply type a message, and Talrn-Bot will analyze its emotional sentiment (positive, negative, or neutral). 
    It then uses a powerful AI model to generate a unique, conversational response and speaks it back to you.
""")

    st.subheader("Technologies Used 🛠️:")
    st.write("""
- **Streamlit**: For creating the interactive web user interface.
- **Google Gemini**: For the core AI-powered response generation.
- **VADER(Valence Aware Dictionary and sentiment Reasoner) Sentiment**: For fast and effective sentiment analysis of your message.
- **gTTS (Google Text-to-Speech)**: For converting the bot's text reply into audio.
""")

    st.divider() 

    st.header("Contact Me")
    st.markdown("""
    **Komal Sharma**
    
    ---
    
    **Professional Profiles:**
    - **LinkedIn:** [k-sharma19](https://www.linkedin.com/in/k-sharma19/)
    - **GitHub:** [komal-sharma19](https://github.com/komal-sharma19)
    - **LeetCode:** [Komal Sharma](https://leetcode.com/u/KomalSharma19/)
    - **GeeksforGeeks:** [Komal Sharma](https://www.geeksforgeeks.org/user/2023asppwkz/)
    - **HackerRank:** [Komal Sharma](https://www.hackerrank.com/profile/2023aspire96)
    
    ---

    **Contact:**
    - ✉️ [1908.komalsharma@gmail.com](mailto:1908.komalsharma@gmail.com)
    - 📍 Kanpur,Uttar Pradesh
    """)

# --- Audio Player Display ---
# Use the new autoplay function instead of st.audio
if st.session_state.audio_file:
    autoplay_audio(st.session_state.audio_file)