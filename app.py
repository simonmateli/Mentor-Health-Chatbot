# app.py

"""
Tkinter GUI for Mental Health Chatbot
Connects to chatbot.py (core engine)
"""

import tkinter as tk
from tkinter import scrolledtext
from chatbot import MentalHealthChatbot

# =========================
# INIT CHATBOT
# =========================
bot = MentalHealthChatbot(name="Mental Wellness Bot")

# =========================
# SEND MESSAGE FUNCTION
# =========================
def send_message():
    user_input = user_entry.get().strip()

    if user_input == "":
        return

    # Display user message
    chat_window.insert(tk.END, "You: " + user_input + "\n")

    # Get bot response
    response = bot.get_reply(user_input)

    # Display bot response
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")

    # Clear input field
    user_entry.delete(0, tk.END)

# =========================
# CLEAR CHAT FUNCTION
# =========================
def clear_chat():
    chat_window.delete(1.0, tk.END)
    bot.clear_history()

# =========================
# TKINTER UI SETUP
# =========================
window = tk.Tk()
window.title("Mental Health Chatbot")
window.geometry("520x650")
window.configure(bg="#e6f2ff")

# Title
title_label = tk.Label(
    window,
    text="Mental Wellness Chatbot 💬",
    font=("Arial", 16, "bold"),
    bg="#e6f2ff"
)
title_label.pack(pady=10)

# Chat display area
chat_window = scrolledtext.ScrolledText(
    window,
    width=60,
    height=25,
    font=("Arial", 10),
    wrap=tk.WORD
)
chat_window.pack(pady=10)

chat_window.insert(tk.END, "Bot: Hello 👋 I'm here to listen and support you.\n\n")

# User input field
user_entry = tk.Entry(window, width=45, font=("Arial", 12))
user_entry.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(window, bg="#e6f2ff")
button_frame.pack()

# Send button
send_button = tk.Button(
    button_frame,
    text="Send",
    command=send_message,
    bg="#4CAF50",
    fg="white",
    width=10,
    font=("Arial", 10)
)
send_button.grid(row=0, column=0, padx=5)

# Clear button
clear_button = tk.Button(
    button_frame,
    text="Clear Chat",
    command=clear_chat,
    bg="#f44336",
    fg="white",
    width=10,
    font=("Arial", 10)
)
clear_button.grid(row=0, column=1, padx=5)

# Enter key support
window.bind("<Return>", lambda event: send_message())

# =========================
# RUN APPLICATION
# =========================
window.mainloop()