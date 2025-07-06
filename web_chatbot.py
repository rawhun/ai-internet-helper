#!/usr/bin/env python3
"""
Web AI Chatbot - Browser interface for the demo chatbot
Uses Flask to create a web server
"""

from flask import Flask, render_template, request, jsonify
import random
import time
from datetime import datetime
import os

app = Flask(__name__)

class WebChatbot:
    def __init__(self):
        self.conversation_history = []
        
        # Predefined responses for different topics
        self.responses = {
            "greeting": [
                "Hello! How can I help you today?",
                "Hi there! Nice to meet you!",
                "Hey! What can I do for you?",
                "Greetings! How are you doing?",
                "Welcome! I'm excited to chat with you! 😊"
            ],
            "weather": [
                "I can't check real-time weather, but I hope it's nice where you are!",
                "Weather is always changing, isn't it?",
                "I'd love to know about the weather too!",
                "Whether it's sunny or rainy, I'm here to brighten your day! ☀️🌧️"
            ],
            "jokes": [
                "Why don't scientists trust atoms? Because they make up everything! 😄",
                "What do you call a fake noodle? An impasta! 🍝",
                "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
                "I told my wife she was drawing her eyebrows too high. She looked surprised! 😲",
                "Why don't eggs tell jokes? They'd crack each other up! 🥚",
                "What do you call a bear with no teeth? A gummy bear! 🐻",
                "Why did the math book look so sad? Because it had too many problems! 📚"
            ],
            "help": [
                "I can chat about various topics, tell jokes, help with questions, or just have a conversation!",
                "Try asking me about the weather, for a joke, or just chat normally!",
                "I'm here to help! What would you like to talk about?",
                "I can tell jokes, chat about weather, tell time, or just have a friendly conversation! 🤖",
                "Ask me anything! I'm good at jokes, small talk, and keeping you company! 💬"
            ],
            "music": [
                "I love music! What's your favorite genre?",
                "Music is amazing! It can change your mood instantly! 🎵",
                "I'd love to hear about your favorite songs!",
                "Music makes everything better, don't you think? 🎶"
            ],
            "food": [
                "Food is one of life's greatest pleasures! What's your favorite?",
                "I love talking about food! What's the best meal you've ever had? 🍕",
                "Cooking and eating are such wonderful experiences!",
                "Food brings people together! What's your comfort food? 🍜"
            ],
            "technology": [
                "Technology is fascinating! What interests you most about it?",
                "I'm a product of technology myself! 🤖",
                "The future of tech is so exciting!",
                "What's your favorite piece of technology? 💻"
            ],
            "unknown": [
                "That's interesting! Tell me more about that.",
                "I'm not sure about that, but I'd love to learn more!",
                "Interesting point! What made you think of that?",
                "I'm still learning, but I find that fascinating!",
                "That's a great topic! I'd love to hear your thoughts on it.",
                "You have such interesting ideas! Tell me more! 🤔",
                "I'm curious about your perspective on this!",
                "That's something I haven't thought about before. What else can you share?"
            ]
        }
    
    def get_response(self, message):
        """Generate a response based on the user's message"""
        message_lower = message.lower()
        self.conversation_history.append({"user": message, "bot": "", "timestamp": datetime.now().strftime("%H:%M")})
        
        # Determine response type based on message content
        if any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']):
            response = random.choice(self.responses["greeting"])
        
        elif any(word in message_lower for word in ['weather', 'temperature', 'rain', 'sunny', 'cold', 'hot', 'forecast']):
            response = random.choice(self.responses["weather"])
        
        elif any(word in message_lower for word in ['joke', 'funny', 'humor', 'laugh', 'comedy', 'hilarious']):
            response = random.choice(self.responses["jokes"])
        
        elif any(word in message_lower for word in ['help', 'what can you do', 'capabilities', 'features']):
            response = random.choice(self.responses["help"])
        
        elif any(word in message_lower for word in ['music', 'song', 'genre', 'artist', 'band', 'concert']):
            response = random.choice(self.responses["music"])
        
        elif any(word in message_lower for word in ['food', 'eat', 'cook', 'meal', 'restaurant', 'pizza', 'burger', 'sushi']):
            response = random.choice(self.responses["food"])
        
        elif any(word in message_lower for word in ['technology', 'tech', 'computer', 'phone', 'app', 'software', 'ai', 'artificial intelligence']):
            response = random.choice(self.responses["technology"])
        
        elif any(word in message_lower for word in ['name', 'call you', 'who are you', 'your name']):
            response = "I'm WebBot, your friendly AI assistant! Nice to meet you! 🤖"
        
        elif any(word in message_lower for word in ['time', 'date', 'today', 'clock']):
            now = datetime.now()
            response = f"Right now it's {now.strftime('%I:%M %p on %B %d, %Y')} ⏰"
        
        elif any(word in message_lower for word in ['bye', 'goodbye', 'see you', 'exit', 'farewell']):
            response = "Goodbye! It was nice chatting with you! 👋 Come back anytime!"
        
        elif any(word in message_lower for word in ['how are you', 'how do you feel', 'are you ok']):
            response = "I'm doing great! Thanks for asking. How about you? 😊"
        
        elif any(word in message_lower for word in ['yes', 'yeah', 'yep', 'sure', 'ok', 'okay']):
            response = "Great! I'm glad you agree! What would you like to talk about next?"
        
        elif any(word in message_lower for word in ['no', 'nope', 'nah', 'not really']):
            response = "That's totally fine! What would you prefer to discuss instead?"
        
        elif any(word in message_lower for word in ['thank', 'thanks', 'appreciate']):
            response = "You're very welcome! I'm happy to help! 😊"
        
        elif any(word in message_lower for word in ['love', 'like', 'enjoy', 'favorite']):
            response = "That's wonderful! I love hearing about things people enjoy! What else do you like?"
        
        elif '?' in message:
            response = "That's a great question! I'm a demo chatbot, so I have limited knowledge, but I'm happy to chat and learn from you!"
        
        else:
            response = random.choice(self.responses["unknown"])
        
        # Update the last message with bot response
        if self.conversation_history:
            self.conversation_history[-1]["bot"] = response
        
        return response

# Create chatbot instance
chatbot = WebChatbot()

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    
    if message.strip():
        response = chatbot.get_response(message)
        return jsonify({
            'response': response,
            'timestamp': datetime.now().strftime("%H:%M")
        })
    
    return jsonify({'response': 'Please enter a message!', 'timestamp': datetime.now().strftime("%H:%M")})

@app.route('/history')
def history():
    return jsonify(chatbot.conversation_history)

@app.route('/status')
def status():
    return jsonify({
        'bot_name': 'WebBot',
        'messages_count': len(chatbot.conversation_history),
        'status': 'online'
    })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("🚀 Web AI Chatbot Starting...")
    print("🌐 Open your browser and go to: http://localhost:8080")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=8080) 