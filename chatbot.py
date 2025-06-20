# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm a Python chatbot!"
    elif "help" in user_input:
        return "Sure, I'm here to assist you. What do you need help with?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I didn't understand that."

# Chat Loop
print("Welcome to ChatBot! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
