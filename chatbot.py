import re
from datetime import datetime

class Chatbot:
    def __init__(self, name="ChatBot"):
        self.name = name
        self.conversation_history = []
        self.patterns = [
            (r'hello|hi|hey', ['Hello! How can I help you today?', 'Hi there! What can I do for you?']),
            (r'how are you', ['I\'m doing great, thanks for asking!', 'I\'m functioning perfectly!']),
            (r'what is your name', [f'I am {name}!']),
            (r'what can you do', ['I can chat with you, answer questions, and help in various ways!', 'I can have conversations with you and provide information!']),
            (r'bye|goodbye|see you', ['Goodbye! Thanks for chatting!', 'See you later!']),
            (r'thank you|thanks', ['You\'re welcome!', 'Happy to help!']),
            (r'what is the time', [f'The current time is {datetime.now().strftime("%H:%M:%S")}']),
            (r'help|assist', ['I can answer questions, chat with you, and learn from our conversation. Just type your message!'])
        ]
    
    def get_response(self, user_input):
        """Generate a response based on user input"""
        for pattern, responses in self.patterns:
            if re.search(pattern, user_input.lower()):
                return responses[0]
        
        # Default response
        return "That's interesting! Tell me more about that."
    
    def chat(self, user_input):
        """Process user input and return response"""
        self.conversation_history.append({"user": user_input})
        response = self.get_response(user_input)
        self.conversation_history.append({"bot": response})
        return response
    
    def get_history(self):
        """Return conversation history"""
        return self.conversation_history
    
    def run(self):
        """Run the chatbot in interactive mode"""
        print(f"Welcome to {self.name}!")
        print("Type 'exit' or 'quit' to end the conversation.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print(f"{self.name}: Goodbye! Thanks for chatting!")
                break
            
            response = self.chat(user_input)
            print(f"{self.name}: {response}\n")


if __name__ == "__main__":
    bot = Chatbot("ChatBot")
    bot.run()