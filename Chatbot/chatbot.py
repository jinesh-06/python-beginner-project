print("=" * 10, "Chatbot", "=" * 10)

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "name": "I am a Python chatbot.",
    "python": "Python is a popular programming language.",
    "help": "I can answer simple questions using keywords.",
    "how are you": "I am doing great! Thanks for asking."
}

conversation = []

def chatbot():
    while True:
        user_input = input("You: ").strip()
        conversation.append({
            "role": "user",
            "content": user_input
        })

        if user_input.lower() == "bye":
            reply = "Goodbye! Have a nice day."

            conversation.append({
                "role": "bot",
                "content": reply
            })

            print("Bot:", reply)
            break

        reply = "Sorry, I don't understand."


        for keyword in responses:
            if keyword in user_input.lower():
                reply = responses[keyword]
                break

  
        conversation.append({
            "role": "bot",
            "content": reply
        })

        print("Bot:", reply)


def calculate_marks(marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return average, highest, lowest

chatbot()


print("\nConversation History:")
for message in conversation:
    print(message)

student_marks = [85, 90, 72, 96, 65]

average, highest, lowest = calculate_marks(student_marks)

print("\nStudent Marks Analysis")
print("Marks:", student_marks)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)