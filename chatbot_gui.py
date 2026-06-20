import tkinter as tk
from tkinter import scrolledtext
import random
 
# ----------------------------
# KNOWLEDGE BASE
# ----------------------------
responses = {
    "hello": ["Hi there! How can I help you today?", "Hey! Great to see you.", "Hello, hello! What's on your mind?"],
    "hi": ["Hello! What can I do for you?", "Hi! Ready when you are."],
    "hey": ["Hey hey! What's up?", "Yo! How's it going?"],
    "good morning": ["Good morning! Hope you have a great day ahead.", "Morning! Coffee first, or jumping right in?"],
    "good night": "Good night! Sleep well.",
    "how are you": ["I'm just a bunch of if-else logic, but I'm doing great!", "Running smoothly, thanks for asking!"],
    "what is your name": "I'm RuleBot, your friendly DecodeLabs chatbot.",
    "who made you": "I was built by an AI Engineer intern at DecodeLabs!",
    "help": "I can chat about greetings, my name, jokes, or how I'm doing. Type 'bye' to exit.",
    "thank you": ["You're welcome!", "Anytime!", "No problem at all."],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "I told my computer I needed a break, and it said 'no problem, I'll go to sleep.'"
    ]
}
 
message_count = 0
 
 
def get_reply(raw_input_text):
    """Same rule-based logic as the console version: sanitize, look up, fallback."""
    global message_count
    clean_input = raw_input_text.lower().strip()
 
    if clean_input == "bye":
        return f"Goodbye! We chatted {message_count} time(s). Have a great day.", True
 
    message_count += 1
    reply = responses.get(clean_input, "I do not understand that yet. Try saying 'help'.")
 
    if isinstance(reply, list):
        reply = random.choice(reply)
 
    return reply, False
 
 
# ----------------------------
# GUI SETUP
# ----------------------------
root = tk.Tk()
root.title("RuleBot - DecodeLabs")
root.geometry("420x520")
root.configure(bg="#0a0d10")
 
CYAN = "#4fd8e8"
ORANGE = "#ff7a45"
BG = "#0a0d10"
PANEL = "#10151a"
TEXT = "#d7e6e8"
 
# Header
header = tk.Label(root, text="RULEBOT  //  RULE-BASED ENGINE",
                   bg=PANEL, fg=CYAN, font=("Consolas", 11, "bold"), pady=10)
header.pack(fill="x")
 
# Chat display
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg=PANEL, fg=TEXT,
                                       font=("Consolas", 10), state="disabled",
                                       borderwidth=0, padx=10, pady=10)
chat_area.pack(fill="both", expand=True, padx=10, pady=10)
chat_area.tag_config("bot", foreground=CYAN)
chat_area.tag_config("user", foreground=ORANGE)
 
 
def display_message(sender, text):
    chat_area.config(state="normal")
    tag = "bot" if sender == "RuleBot" else "user"
    chat_area.insert(tk.END, f"{sender}: ", tag)
    chat_area.insert(tk.END, f"{text}\n\n")
    chat_area.config(state="disabled")
    chat_area.see(tk.END)
 
 
def send_message(event=None):
    user_text = entry.get()
    if not user_text.strip():
        return
    display_message("You", user_text)
    entry.delete(0, tk.END)
 
    reply, should_exit = get_reply(user_text)
    display_message("RuleBot", reply)
 
    if should_exit:
        entry.config(state="disabled")
        send_btn.config(state="disabled")
 
 
# Input row
input_frame = tk.Frame(root, bg=BG)
input_frame.pack(fill="x", padx=10, pady=(0, 10))
 
entry = tk.Entry(input_frame, font=("Consolas", 11), bg=PANEL, fg=TEXT,
                  insertbackground=TEXT, borderwidth=0)
entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 6))
entry.bind("<Return>", send_message)
entry.focus()
 
send_btn = tk.Button(input_frame, text="Send", command=send_message,
                      bg=CYAN, fg="#0a0d10", font=("Consolas", 10, "bold"),
                      borderwidth=0, padx=14, activebackground="#7be8f2")
send_btn.pack(side="right")
 
# Initial greeting
display_message("RuleBot", "Hello! Type 'bye' anytime to exit.")
 
root.mainloop()