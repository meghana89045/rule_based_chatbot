# Rule-Based AI Chatbot 🤖
 
**Industrial Training Kit — Project 1**
Built as part of the DecodeLabs AI Engineering Internship (Batch 2026).
 
## Overview
 
This project is a foundational AI chatbot built using **pure rule-based logic** — no machine learning, no APIs. It simulates conversation through deterministic control flow: input sanitization, dictionary-based intent matching, and a fallback response system.
 
The goal of this milestone is to master **control flow and decision-making logic** before progressing to probabilistic, learning-based AI systems.
 
## Features
 
- 🔁 Continuous input loop (`while True`)
- 🧹 Input sanitization (case-insensitive, whitespace-trimmed)
- 📖 Dictionary-based knowledge base with 10+ intents
- 🎲 Randomized replies for a more natural personality
- 🔢 Live message counter
- 🚪 Clean exit command (`bye`)
- 🖥️ Two interfaces:
  - `chatbot.py` — console version
  - `chatbot_gui.py` — desktop GUI version (built with Tkinter)
## How It Works
 
1. **Input** — user types a message.
2. **Sanitization** — text is lowercased and stripped of extra whitespace.
3. **Process** — the cleaned input is looked up in a response dictionary using `.get()`, which returns a matching reply or a fallback message if no match is found.
4. **Output** — the bot replies; if the reply has multiple options, one is chosen at random.
5. The loop continues until the user types `bye`, which ends the session with a summary.
## Run It
 
### Console version
```bash
python chatbot.py
```
 
### GUI version
```bash
python chatbot_gui.py
```
 
No external libraries required — built entirely with Python's standard library (`random`, `tkinter`).
 
## Example Conversation
 
```
RuleBot: Hello! Type 'bye' anytime to exit.
You: hello
RuleBot: Hi there! How can I help you today?
You: joke
RuleBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: bye
RuleBot: Goodbye! We chatted 2 time(s). Have a great day.
```
 
## Tech Stack
 
- Python 3
- Tkinter (for GUI)
## Author
 
Built by an AI Engineering Intern at **DecodeLabs** as part of the 2026 Industrial Training Kit.
 
---
📍 DecodeLabs · Greater Lucknow, India
🌎 www.decodelabs.tech
