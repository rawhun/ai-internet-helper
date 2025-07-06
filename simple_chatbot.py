#!/usr/bin/env python3
"""
Simple AI Chatbot that works with Python 3.13
Uses OpenAI, Hugging Face, and Cohere APIs directly
No complex dependencies required!
"""

import os
import json
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SimpleAIChatbot:
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.hf_key = os.getenv('HUGGINGFACE_API_KEY')
        self.cohere_key = os.getenv('COHERE_API_KEY')
        self.current_provider = 'openai'
        self.conversation_history = []
        
    def chat_with_openai(self, message):
        """Chat using OpenAI API"""
        try:
            headers = {
                'Authorization': f'Bearer {self.openai_key}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'model': 'gpt-3.5-turbo',
                'messages': [
                    {'role': 'system', 'content': 'You are a helpful AI assistant.'},
                    {'role': 'user', 'content': message}
                ],
                'max_tokens': 150
            }
            
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers=headers,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                return f"OpenAI Error: {response.status_code}"
                
        except Exception as e:
            return f"OpenAI Error: {str(e)}"
    
    def chat_with_huggingface(self, message):
        """Chat using Hugging Face API"""
        try:
            headers = {
                'Authorization': f'Bearer {self.hf_key}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'inputs': f"User: {message}\nAssistant:",
                'parameters': {
                    'max_new_tokens': 100,
                    'temperature': 0.7
                }
            }
            
            response = requests.post(
                'https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium',
                headers=headers,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', 'Sorry, I could not generate a response.')
                else:
                    return str(result)
            else:
                return f"Hugging Face Error: {response.status_code}"
                
        except Exception as e:
            return f"Hugging Face Error: {str(e)}"
    
    def chat_with_cohere(self, message):
        """Chat using Cohere API"""
        try:
            headers = {
                'Authorization': f'Bearer {self.cohere_key}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'model': 'command-xlarge-nightly',
                'prompt': f"User: {message}\nAssistant:",
                'max_tokens': 100,
                'temperature': 0.7
            }
            
            response = requests.post(
                'https://api.cohere.ai/v1/generate',
                headers=headers,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['generations'][0]['text']
            else:
                return f"Cohere Error: {response.status_code}"
                
        except Exception as e:
            return f"Cohere Error: {str(e)}"
    
    def get_response(self, message):
        """Get response from current provider, fallback to others if needed"""
        self.conversation_history.append(f"User: {message}")
        
        # Try current provider first
        if self.current_provider == 'openai':
            response = self.chat_with_openai(message)
            if 'Error' not in response:
                self.conversation_history.append(f"Assistant: {response}")
                return response
            else:
                print(f"⚠️ OpenAI failed, trying Hugging Face...")
                self.current_provider = 'huggingface'
        
        if self.current_provider == 'huggingface':
            response = self.chat_with_huggingface(message)
            if 'Error' not in response:
                self.conversation_history.append(f"Assistant: {response}")
                return response
            else:
                print(f"⚠️ Hugging Face failed, trying Cohere...")
                self.current_provider = 'cohere'
        
        if self.current_provider == 'cohere':
            response = self.chat_with_cohere(message)
            if 'Error' not in response:
                self.conversation_history.append(f"Assistant: {response}")
                return response
            else:
                print(f"⚠️ Cohere failed, switching back to OpenAI...")
                self.current_provider = 'openai'
                return "Sorry, all AI providers are currently unavailable. Please try again later."
    
    def show_status(self):
        """Show current provider status"""
        providers = {
            'openai': 'OpenAI GPT-3.5',
            'huggingface': 'Hugging Face DialoGPT',
            'cohere': 'Cohere Command'
        }
        print(f"🤖 Current Provider: {providers.get(self.current_provider, self.current_provider)}")
        print(f"💬 Messages in session: {len(self.conversation_history)}")

def main():
    print("🚀 Simple AI Chatbot Starting...")
    print("=" * 50)
    
    # Test API keys
    chatbot = SimpleAIChatbot()
    
    if not chatbot.openai_key:
        print("❌ OpenAI API key not found!")
        return
    
    print("✅ API keys loaded successfully!")
    print("💡 Type 'quit' to exit, 'status' to see provider info")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() == 'quit':
                print("👋 Goodbye!")
                break
            elif user_input.lower() == 'status':
                chatbot.show_status()
                continue
            elif not user_input:
                continue
            
            print("🤖 AI: ", end="", flush=True)
            response = chatbot.get_response(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 