def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    # Asking name
    elif "your name" in user_input:
        return "I am DecodeBot, your AI assistant."

    # Asking about AI
    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence. It enables machines to simulate human intelligence."

    # Asking about python
    elif "python" in user_input:
        return "Python is a popular programming language used in AI, Data Science, and Web Development."

    # Time
    elif "time" in user_input:
        from datetime import datetime
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"

    # Date
    elif "date" in user_input:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    # Help
    elif "help" in user_input:
        return """
I can answer:
- Hello / Hi
- What is AI
- What is Python
- Date
- Time
- Your Name
- Exit
"""

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    # Default response
    else:
        return "Sorry, I don't understand that. Type 'help' to see available commands."


print("=" * 50)
print("🤖 Welcome to DecodeBot")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() in ["bye", "exit", "quit"]:
        break