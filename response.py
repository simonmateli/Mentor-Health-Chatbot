# response.py

"""
Response engine for Mental Health Chatbot.
Uses emotion detection output to generate supportive replies.
"""

from emotions import detect_emotion

# =========================
# DETAILED RESPONSE BANK
# =========================
RESPONSES = {
    "sad": [
        "I'm really sorry you're feeling this way. Do you want to talk about what's making you feel sad?",
        "That sounds heavy. I'm here with you. What’s been going on?",
        "It’s okay to feel this way. Would you like to share more?"
    ],

    "anxious": [
        "I hear you. Let’s slow things down together. What’s on your mind?",
        "Anxiety can feel overwhelming. Do you know what triggered it?",
        "Try taking a slow breath with me. Want to talk about it?"
    ],

    "stressed": [
        "That sounds like a lot of pressure. What’s the biggest challenge right now?",
        "You don’t have to carry everything alone. Let’s break it down together.",
        "Stress can feel heavy—what part feels hardest?"
    ],

    "happy": [
        "I’m really glad you’re feeling good! What made your day better?",
        "That’s great to hear! Keep that positive energy going 😊",
        "Nice! What’s been going well for you?"
    ],

    "angry": [
        "I understand you're upset. Want to talk about what caused it?",
        "It’s okay to feel angry. Let’s try to understand it together.",
        "That sounds frustrating. I’m here to listen."
    ],

    "neutral": [
        "I’m here with you. Tell me more about how you're feeling.",
        "Would you like to share what's on your mind?",
        "I'm listening. Go on."
    ]
}

# =========================
# MAIN RESPONSE FUNCTION
# =========================
def generate_response(user_input):
    emotion = detect_emotion(user_input)

    import random
    return random.choice(RESPONSES.get(emotion, RESPONSES["neutral"]))