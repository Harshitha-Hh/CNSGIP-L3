from chatterbot.trainers import ListTrainer

# Custom training data
training_data = [
    "Hi, how can I help you?",
    "I need assistance with my order.",
    "Sure, I can help with that. Can you provide your order number?",
    "Yes, it's 123456.",
    "Thank you. I am looking up your order now.",
    # Add more conversation pairs as needed
]

# Train the chatbot with custom data
trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Example usage
if __name__ == "__main__":
    print("Hello! I am your AssistantBot. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("AssistantBot: Goodbye! Have a nice day.")
            break
        response = get_response(user_input)
        print(f"AssistantBot: {response}")
