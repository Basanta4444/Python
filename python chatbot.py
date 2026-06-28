class SimpleChatbot:
    def __init__(self):
        # Dictionary of inputs and their responses
        self.responses = {
            "hello": "world",
            "hi": "there",
            "hey": "friend",
            "bye": "goodbye",
            "thanks": "welcome",
            "ok": "cool",
            "yes": "no",
            "no": "yes",
        }
    
    def get_response(self, user_input):
        # Clean the input: lowercase, strip spaces
        cleaned = user_input.lower().strip()
        
        # Return matching response or default
        if cleaned in self.responses:
            return self.responses[cleaned]
        else:
            return "I don't know that word yet."

    def chat(self):
        print("🤖 Simple Chatbot (type 'quit' to exit)")
        print("-" * 30)
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ["quit", "exit"]:
                print("Bot: bye!")
                break
            
            response = self.get_response(user_input)
            print(f"Bot: {response}")

# Run it
if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.chat()