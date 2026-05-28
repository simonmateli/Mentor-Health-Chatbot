# emotions.py

"""
Simple emotion detection module for a mental health chatbot.
Maps user text → emotional category → supportive response type.
"""

# =========================
# EMOTION KEYWORDS DATABASE
# =========================
EMOTION_MAP = {
    "sad": ["sad", "depressed", "down", "cry", "unhappy", "lonely", "empty"],
    "anxious": ["anxious", "nervous", "panic", "worried", "fear", "scared"],
    "stressed": ["stress", "stressed", "overwhelmed", "pressure", "burnout"],
    "happy": ["happy", "good", "great", "excited", "joy", "fine", "okay"],
    "angry": ["angry", "mad", "furious", "annoyed", "irritated"]
}


# =========================
# DETECT EMOTION FUNCTION
# =========================
def detect_emotion(text):
    text = text.lower()

    for emotion, keywords in EMOTION_MAP.items():
        for word in keywords:
            if word in text:
                return emotion

    return "neutral"


# =========================
# RESPONSE TEMPLATES
# =========================
RESPONSE_MAP = {
    "sad": "I'm really sorry you're feeling this way. Want to talk more about what's making you feel sad?",

    "anxious": "I hear you. Try taking slow deep breaths. What do you think is triggering your anxiety?",

    "stressed": "That sounds like a lot to handle. What part feels the heaviest right now?",

    "happy": "I'm glad you're feeling better! What made your day positive?",

    "angry": "I understand you're upset. Want to talk about what caused this feeling?",

    "neutral": "I'm here with you. Can you tell me more about how you're feeling?"
}


# =========================
# GET RESPONSE FUNCTION
# =========================
def get_emotion_response(text):
    emotion = detect_emotion(text)
    return RESPONSE_MAP.get(emotion, RESPONSE_MAP["neutral"])