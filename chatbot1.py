def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a computer program, but thanks for asking!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand. Can you please rephrase your question?")
            
chatbot()
