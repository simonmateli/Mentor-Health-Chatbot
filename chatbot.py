# chatbot.py

"""
Main chatbot engine for Mental Health Chatbot system.
Connects emotion detection + response generation.
"""

from response import generate_response

# =========================
# CHATBOT CLASS
# =========================
class MentalHealthChatbot:

    def __init__(self, name="Support Bot"):
        self.name = name
        self.chat_history = []

    # =========================
    # PROCESS USER MESSAGE
    # =========================
    def get_reply(self, user_message):
        response = generate_response(user_message)

        # Store conversation history
        self.chat_history.append({
            "user": user_message,
            "bot": response
        })

        return response

    # =========================
    # GET CHAT HISTORY
    # =========================
    def get_history(self):
        return self.chat_history

    # =========================
    # CLEAR HISTORY
    # =========================
    def clear_history(self):
        self.chat_history = []
        return "Chat history cleared."

# =========================
# SIMPLE TEST RUN (OPTIONAL)
# =========================
if __name__ == "__main__":
    bot = MentalHealthChatbot()

    print("Mental Health Chatbot is running... Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Take care of yourself ❤️")
            break

        reply = bot.get_reply(user_input)
        print("Bot:", reply)