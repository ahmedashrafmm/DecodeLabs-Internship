# ============================================================
#  DecodeLabs | Batch 2026 | Project 1: Rule-Based AI Chatbot
#  Author   : Ahmed Ashraf Mohamed
#  Arch     : IPO Model  →  Input → Process → Output
# ============================================================

# ── KNOWLEDGE BASE (Dictionary O(1) lookup – not an if-elif ladder) ──
RESPONSES = {
    # Greetings
    "hello"        : "Hey there! 👋 I'm DecoBot. How can I assist you today?",
    "hi"           : "Hi! DecoBot online and ready. What's on your mind?",
    "hey"          : "Hey! What can I do for you?",

    # Identity
    "who are you"  : "I'm DecoBot 🤖 — a rule-based AI chatbot built at DecodeLabs.",
    "what are you" : "I'm a deterministic logic engine. Pure if-else, zero hallucination.",

    # About DecodeLabs
    "what is decodelabs" : "DecodeLabs is an AI training lab based in Greater Lucknow, India. 🚀",
    "decodelabs"         : "DecodeLabs — where AI engineers are made, one rule at a time.",

    # Help / capabilities
    "help"         : "I can answer questions about DecodeLabs, AI, or just chat. Try: 'what is ai', 'who are you', 'joke'.",
    "what can you do" : "I respond to greetings, answer FAQs, tell jokes, and shut down gracefully. Type 'help' for hints.",

    # AI concepts
    "what is ai"   : "AI is the simulation of human intelligence by machines — pattern recognition, decision-making, and learning.",
    "what is ml"   : "Machine Learning is a subset of AI where systems learn from data instead of being explicitly programmed.",
    "what is a rule based chatbot" : "A rule-based chatbot uses predefined if-else logic (or dictionary lookups) to respond — fully deterministic, zero guesswork.",

    # Small talk
    "how are you"  : "Running at 100% efficiency. All logic gates nominal. 🟢",
    "what is your name" : "DecoBot — intern-built, battle-tested.",
    "joke"         : "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "thank you"    : "Happy to help! Keep building. 💪",
    "thanks"       : "Anytime! That's what I'm here for.",

    # Farewells (handled separately via EXIT_COMMANDS for the break)
    "bye"          : "Goodbye! Keep pushing code. 👋",
    "goodbye"      : "See you next session. Stay curious!",
}

# ── EXIT TRIGGERS (kill command → breaks the infinite loop) ──
EXIT_COMMANDS = {"exit", "quit", "q", "stop", "bye", "goodbye"}


# ════════════════════════════════════════════════════════════
#  PHASE 1 — INPUT & SANITIZATION
# ════════════════════════════════════════════════════════════
def sanitize(raw: str) -> str:
    """Lowercase + strip whitespace  →  normalised token."""
    return raw.lower().strip()


# ════════════════════════════════════════════════════════════
#  PHASE 2 — PROCESS (Intent Matching)
# ════════════════════════════════════════════════════════════
def get_response(clean_input: str) -> str:
    """
    O(1) dictionary lookup with a graceful fallback.
    Uses .get() — the professional approach from the spec.
    """
    return RESPONSES.get(clean_input, "I don't understand that yet. Try 'help' for available commands.")


# ════════════════════════════════════════════════════════════
#  PHASE 3 — OUTPUT  (the infinite feedback loop)
# ════════════════════════════════════════════════════════════
def run_chatbot():
    print("=" * 55)
    print("  DecoLaBot v1.1  |  DecodeLabs Batch 2026")
    print("  Rule-Based AI Chatbot  |  Project 1")
    print("  Type 'help' for commands  |  'exit' to quit")
    print("=" * 55)

    # ── THE HEARTBEAT: infinite loop — lives until kill command ──
    while True:

        # Phase 1 — Raw input + sanitization
        raw_input   = input("\nYou: ")
        clean_input = sanitize(raw_input)

        # Guard: ignore empty input
        if not clean_input:
            continue

        # EXIT STRATEGY — clean break command
        if clean_input in EXIT_COMMANDS:
            farewell = RESPONSES.get(clean_input, "Goodbye! See you next time. 👋")
            print(f"\nDecoLaBot: {farewell}")
            print("-" * 55)
            break

        # Phase 2 & 3 — Process → Output
        reply = get_response(clean_input)
        print(f"\nDecoLaBot: {reply}")


# ── ENTRY POINT ──
if __name__ == "__main__":
    run_chatbot()