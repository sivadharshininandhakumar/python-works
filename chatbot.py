def chatbot_response(user_input):
    if "hi" in user_input.lower() or "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a chatbot, so I don't have feelings, but thanks for asking!"
    elif "goodbye" in user_input.lower() or "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase your question?"

# Main loop for chatting with the user
while True:
    user_input = input("User: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
