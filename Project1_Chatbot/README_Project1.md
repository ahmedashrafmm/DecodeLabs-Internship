# 🤖 Project 1: Rule-Based AI Chatbot

**DecodeLabs | Industrial Training Kit | Batch 2026**

---

## 📌 Overview

A rule-based AI chatbot built using pure Python control flow and logic. This project demonstrates the foundational architecture of an intelligent interface — a deterministic system that simulates basic human interaction through explicit if-else decision-making, implemented efficiently using dictionary lookups.

> *"Before you build systems that learn on their own, you must master the art of teaching a machine through explicit instructions."* — DecodeLabs

---

## 🎯 Goal

Create a simple rule-based chatbot that responds to predefined user inputs using:
- A continuous input loop
- Input sanitization
- Dictionary-based response matching
- A graceful exit strategy

---

## ⚙️ Architecture: IPO Model

| Phase | Task | Implementation |
|---|---|---|
| **INPUT** | Capture & sanitize user input | `raw_input.lower().strip()` |
| **PROCESS** | Match intent to response | Dictionary O(1) lookup |
| **OUTPUT** | Print response & loop | `while True` feedback loop |

---

## 📋 Project Specification Checklist

| Requirement | Status |
|---|---|
| INPUT LOOP — continuous `while` cycle | ✅ |
| SANITIZATION — handle case & whitespace | ✅ |
| KNOWLEDGE BASE — dictionary with 5+ intents | ✅ 20+ intents |
| FALLBACK — default response for unknowns | ✅ |
| EXIT STRATEGY — clean break command | ✅ |

---

## 💡 Key Design Decisions

### Dictionary O(1) vs If-Elif Ladder O(n)
The chatbot uses a **Python dictionary** instead of a chain of `if-elif` statements.

| Approach | Complexity | Maintainability |
|---|---|---|
| If-Elif Ladder | O(n) — slows with scale | High technical debt |
| Dictionary Lookup | O(1) — instant regardless of size | Clean & scalable |

### `.get()` Method — The Professional Approach
```python
reply = responses.get(user_input, "I do not understand.")
```
Handles both lookup and fallback in a single atomic operation.

---

## 🗂️ Supported Intents

| Category | Keywords |
|---|---|
| Greetings | `hello`, `hi`, `hey` |
| Identity | `who are you`, `what are you` |
| About DecodeLabs | `what is decodelabs`, `decodelabs` |
| Help | `help`, `what can you do` |
| AI Concepts | `what is ai`, `what is ml`, `what is a rule based chatbot` |
| Small Talk | `how are you`, `joke`, `thank you`, `thanks` |
| Exit | `bye`, `goodbye`, `exit`, `quit`, `stop` |

---

## 🚀 How to Run

```bash
python Project1_Chatbot.py
```

**Example session:**
```
You: hello
DecoBot: Hey there! 👋 I'm DecoBot. How can I assist you today?

You: what is ai
DecoBot: AI is the simulation of human intelligence by machines...

You: joke
DecoBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: exit
DecoBot: Goodbye! Keep pushing code. 👋
```

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required — pure Python

---

## 📚 Key Skills Demonstrated

- Control flow & decision-making logic
- Dictionary-based O(1) lookup (vs if-elif anti-pattern)
- Input sanitization & normalization
- Infinite loop with graceful exit
- Basic AI / chatbot concepts
- IPO (Input → Process → Output) model

---

*DecodeLabs | Batch 2026 | Project 1 of the AI Engineering Track*
