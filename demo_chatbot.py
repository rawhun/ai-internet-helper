#!/usr/bin/env python3
"""
Demo AI Chatbot - Works immediately without external APIs
Has predefined responses and conversation flow
"""

import random
import time
from datetime import datetime

class DemoChatbot:
    def __init__(self):
        self.conversation_history = []
        self.user_name = None
        self.current_topic = "general"
        
        # Predefined responses for different topics
        self.responses = {
            "greeting": [
                "Hello! How can I help you today?",
                "Hi there! Nice to meet you!",
                "Hey! What can I do for you?",
                "Greetings! How are you doing?"
            ],
            "weather": [
                "I can't check real-time weather, but I hope it's nice where you are!",
                "Weather is always changing, isn't it?",
                "I'd love to know about the weather too!"
            ],
            "jokes": [
                "Why don't scientists trust atoms? Because they make up everything! 😄",
                "What do you call a fake noodle? An impasta! 🍝",
                "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
                "I told my wife she was drawing her eyebrows too high. She looked surprised! 😲"
            ],
            "help": [
                "I can chat about various topics, tell jokes, help with questions, or just have a conversation!",
                "Try asking me about the weather, for a joke, or just chat normally!",
                "I'm here to help! What would you like to talk about?"
            ],
            "unknown": [
                "That's interesting! Tell me more about that.",
                "I'm not sure about that, but I'd love to learn more!",
                "Interesting point! What made you think of that?",
                "I'm still learning, but I find that fascinating!"
            ]
        }
    
    def get_response(self, message):
        """Generate a response based on the user's message"""
        message_lower = message.lower()
        self.conversation_history.append(f"User: {message}")
        
        # Add some thinking time for realism
        time.sleep(0.5)
        
        # Determine response type based on message content
        if any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            response = random.choice(self.responses["greeting"])
            if not self.user_name and 'name' in message_lower:
                response += " What's your name?"
        
        elif any(word in message_lower for word in ['weather', 'temperature', 'rain', 'sunny']):
            response = random.choice(self.responses["weather"])
        
        elif any(word in message_lower for word in ['joke', 'funny', 'humor', 'laugh']):
            response = random.choice(self.responses["jokes"])
        
        elif any(word in message_lower for word in ['help', 'what can you do', 'capabilities']):
            response = random.choice(self.responses["help"])
        
        elif any(word in message_lower for word in ['name', 'call you', 'who are you']):
            response = "I'm DemoBot, your friendly AI assistant! Nice to meet you!"
        
        elif any(word in message_lower for word in ['time', 'date', 'today']):
            now = datetime.now()
            response = f"Right now it's {now.strftime('%I:%M %p on %B %d, %Y')}"
        
        elif any(word in message_lower for word in ['bye', 'goodbye', 'see you', 'exit']):
            response = "Goodbye! It was nice chatting with you! 👋"
        
        elif any(word in message_lower for word in ['how are you', 'how do you feel']):
            response = "I'm doing great! Thanks for asking. How about you?"
        
        elif '?' in message:
            response = "That's a great question! I'm a demo chatbot, so I have limited knowledge, but I'm happy to chat!"
        
        else:
            response = random.choice(self.responses["unknown"])
        
        self.conversation_history.append(f"Bot: {response}")
        return response
    
    def show_status(self):
        """Show chatbot status"""
        print(f"🤖 Bot Name: DemoBot")
        print(f"💬 Messages in session: {len(self.conversation_history)}")
        print(f"📅 Session started: {datetime.now().strftime('%I:%M %p')}")
        print(f"🎯 Current topic: {self.current_topic}")
    
    def show_history(self):
        """Show conversation history"""
        if not self.conversation_history:
            print("No conversation history yet!")
            return
        
        print("\n📜 Conversation History:")
        print("-" * 40)
        for i, msg in enumerate(self.conversation_history, 1):
            print(f"{i}. {msg}")
        print("-" * 40)

def main():
    print("🚀 Demo AI Chatbot Starting...")
    print("=" * 50)
    print("🤖 This is a demo chatbot with predefined responses")
    print("💡 Commands: 'quit' to exit, 'status' for info, 'history' for chat log")
    print("=" * 50)
    
    chatbot = DemoChatbot()
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() == 'quit':
                print("👋 Goodbye! Thanks for chatting!")
                break
            elif user_input.lower() == 'status':
                chatbot.show_status()
                continue
            elif user_input.lower() == 'history':
                chatbot.show_history()
                continue
            elif not user_input:
                continue
            
            print("🤖 Bot: ", end="", flush=True)
            response = chatbot.get_response(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 