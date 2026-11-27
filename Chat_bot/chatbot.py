
import json
import os
from datetime import datetime
class ChatBot:
    def __init__(self, name):
        self.name = name
        self.history = []
        self.history_file = "chat_history.json"

        self.replies = {
            "hello": "Hello! Nice to meet you.",
            "hi": "Hi! How can I help you?",
            "hey": "Hey! What's going on?",
            "how are you": "I'm doing great! Thanks for asking.",
            "your name": f"My name is {self.name}.",
            "who are you": f"I am {self.name}, your Python chatbot.",
            "python": "Python is a beginner-friendly programming language.",
            "ai": "AI means Artificial Intelligence. It helps machines perform intelligent tasks.",
            "study": "Keep learning every day. Small progress leads to big results!",
            "help": "You can ask me about Python, AI, studying, or just chat with me.",
            "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
            "time": f"The current time is {datetime.now().strftime('%I:%M %p')}",
            "date": f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"
        }
        self.load_history()
    def add_message(self, role, content):
        message = {
            "role": role,
            "content": content,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.history.append(message)
        self.save_history()


    # reply
    def get_reply(self, message):
        message = message.lower().strip()
        # date and time
        if "time" in message:
            return datetime.now().strftime("The current time is %I:%M %p.")

        if "date" in message or "today" in message:
            return datetime.now().strftime("Today's date is %d-%m-%Y.")


        for keyword, reply in self.replies.items():
            if keyword in message:
                return reply

        return "I'm not sure about that. Type 'help' to see what I can do."
    # Save conversation t
    def save_history(self):
        try:
            with open(self.history_file, "w") as file:
                json.dump(self.history, file, indent=4)

        except OSError as e:
            print("Error saving chat history:", e)

    # Load previous conversation
    def load_history(self):
        try:
            with open(self.history_file, "r") as file:
                self.history = json.load(file)

            print("Previous chat history loaded.")

        except FileNotFoundError:
            self.history = []
            print("No previous chat history found.")

        except json.JSONDecodeError:
            self.history = []
            print("Chat history file is corrupted. Starting fresh.")

        except OSError as e:
            self.history = []
            print("Error loading history:", e)


    def show_history(self):
        if not self.history:
            print("No chat history available.")
            return

        print("\n--- Previous Chat History ---")

        for message in self.history:
            role = message["role"].capitalize()
            content = message["content"]
            print(f"{role}: {content}")
