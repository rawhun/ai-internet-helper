#!/usr/bin/env python3
"""
Advanced AI Chatbot with Real-Time Internet Information
Fetches current data from multiple sources for accurate responses
"""

import requests
import json
import random
import time
from datetime import datetime
import os
from flask import Flask, render_template, request, jsonify
import re
import urllib.parse
from bs4 import BeautifulSoup
import wikipedia
import feedparser
from newsapi import NewsApiClient

app = Flask(__name__)

class AdvancedInternetAI:
    def __init__(self):
        self.conversation_history = []
        self.knowledge_base = {}
        self.search_cache = {}
        
        # API Keys (you can add your own keys for better results)
        self.news_api_key = "demo"  # Replace with your NewsAPI key
        self.wikipedia_lang = "en"
        
        # Search engines and APIs
        self.search_engines = {
            "duckduckgo": "https://api.duckduckgo.com/",
            "wikipedia": "https://en.wikipedia.org/api/rest_v1/",
            "news": "https://newsapi.org/v2/",
            "weather": "https://api.openweathermap.org/data/2.5/",
            "currency": "https://api.exchangerate-api.com/v4/latest/"
        }
        
        # Initialize news API client
        try:
            self.news_api = NewsApiClient(api_key=self.news_api_key)
        except:
            self.news_api = None
        
        # Enhanced knowledge base
        self.knowledge = {
            "ai_concepts": {
                "machine_learning": "Machine learning is a subset of AI that enables computers to learn and improve from experience without being explicitly programmed.",
                "deep_learning": "Deep learning uses neural networks with multiple layers to model complex patterns in data.",
                "neural_networks": "Neural networks are computing systems inspired by biological brains that can learn to recognize patterns.",
                "nlp": "Natural Language Processing helps computers understand, interpret, and generate human language.",
                "computer_vision": "Computer vision enables computers to interpret and understand visual information from images and videos."
            }
        }
    
    def search_duckduckgo(self, query):
        """Search DuckDuckGo for current information"""
        try:
            url = "https://api.duckduckgo.com/"
            params = {
                'q': query,
                'format': 'json',
                'no_html': '1',
                'skip_disambig': '1'
            }
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return {
                    'abstract': data.get('Abstract', ''),
                    'related_topics': data.get('RelatedTopics', [])[:3],
                    'answer': data.get('Answer', ''),
                    'definition': data.get('Definition', '')
                }
            return None
        except Exception as e:
            print(f"DuckDuckGo search error: {e}")
            return None
    
    def search_wikipedia(self, query):
        """Search Wikipedia for detailed information"""
        try:
            # Search for pages
            search_results = wikipedia.search(query, results=3)
            if search_results:
                # Get summary of first result
                page = wikipedia.page(search_results[0])
                return {
                    'title': page.title,
                    'summary': wikipedia.summary(search_results[0], sentences=3),
                    'url': page.url,
                    'categories': page.categories[:5]
                }
            return None
        except Exception as e:
            print(f"Wikipedia search error: {e}")
            return None
    
    def get_news(self, query, country='us'):
        """Get current news related to the query"""
        try:
            if self.news_api:
                articles = self.news_api.get_everything(q=query, language='en', sort_by='relevancy', page_size=5)
                return articles.get('articles', [])
            else:
                # Fallback to RSS feeds
                return self.get_rss_news(query)
        except Exception as e:
            print(f"News API error: {e}")
            return []
    
    def get_rss_news(self, query):
        """Get news from RSS feeds as fallback"""
        try:
            feeds = [
                "https://feeds.bbci.co.uk/news/rss.xml",
                "https://rss.cnn.com/rss/edition.rss",
                "https://feeds.reuters.com/reuters/topNews"
            ]
            news_items = []
            for feed_url in feeds:
                try:
                    feed = feedparser.parse(feed_url)
                    for entry in feed.entries[:3]:
                        if query.lower() in entry.title.lower() or query.lower() in entry.get('summary', '').lower():
                            news_items.append({
                                'title': entry.title,
                                'description': entry.get('summary', ''),
                                'url': entry.link,
                                'published': entry.get('published', '')
                            })
                except:
                    continue
            return news_items
        except Exception as e:
            print(f"RSS news error: {e}")
            return []
    
    def get_weather(self, location):
        """Get current weather information"""
        try:
            # Using OpenWeatherMap API (free tier)
            url = f"https://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': location,
                'appid': 'demo',  # Replace with your API key
                'units': 'metric'
            }
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return {
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed']
                }
            return None
        except Exception as e:
            print(f"Weather API error: {e}")
            return None
    
    def get_currency_rate(self, from_currency, to_currency):
        """Get current currency exchange rates"""
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                rate = data['rates'].get(to_currency.upper(), 0)
                return {
                    'rate': rate,
                    'date': data['date'],
                    'base': data['base']
                }
            return None
        except Exception as e:
            print(f"Currency API error: {e}")
            return None
    
    def search_web(self, query):
        """Comprehensive web search combining multiple sources"""
        results = {
            'duckduckgo': None,
            'wikipedia': None,
            'news': [],
            'weather': None,
            'currency': None
        }
        
        # Check cache first
        cache_key = query.lower().strip()
        if cache_key in self.search_cache:
            return self.search_cache[cache_key]
        
        # Search DuckDuckGo for general information
        results['duckduckgo'] = self.search_duckduckgo(query)
        
        # Search Wikipedia for detailed information
        results['wikipedia'] = self.search_wikipedia(query)
        
        # Get current news
        results['news'] = self.get_news(query)
        
        # Check if it's a weather query
        weather_keywords = ['weather', 'temperature', 'forecast', 'climate']
        if any(keyword in query.lower() for keyword in weather_keywords):
            # Extract location from query
            location = query.replace('weather', '').replace('temperature', '').replace('forecast', '').strip()
            if location:
                results['weather'] = self.get_weather(location)
        
        # Check if it's a currency query
        currency_keywords = ['currency', 'exchange rate', 'convert', 'dollar', 'euro', 'pound']
        if any(keyword in query.lower() for keyword in currency_keywords):
            # Extract currencies from query
            currencies = re.findall(r'\b(usd|eur|gbp|jpy|cad|aud|chf|cny|inr)\b', query.lower())
            if len(currencies) >= 2:
                results['currency'] = self.get_currency_rate(currencies[0], currencies[1])
        
        # Cache results for 5 minutes
        self.search_cache[cache_key] = results
        return results
    
    def generate_informed_response(self, message, search_results):
        """Generate a response based on real-time information"""
        message_lower = message.lower()
        
        # Build comprehensive response
        response_parts = []
        
        # Add DuckDuckGo information
        if search_results['duckduckgo']:
            ddg = search_results['duckduckgo']
            if ddg.get('answer'):
                response_parts.append(f"**Direct Answer:** {ddg['answer']}")
            if ddg.get('abstract'):
                response_parts.append(f"**Information:** {ddg['abstract']}")
            if ddg.get('definition'):
                response_parts.append(f"**Definition:** {ddg['definition']}")
        
        # Add Wikipedia information
        if search_results['wikipedia']:
            wiki = search_results['wikipedia']
            response_parts.append(f"**Wikipedia Summary:** {wiki['summary']}")
            response_parts.append(f"*Source: [Wikipedia - {wiki['title']}]({wiki['url']})*")
        
        # Add current news
        if search_results['news']:
            response_parts.append("**Recent News:**")
            for i, article in enumerate(search_results['news'][:3], 1):
                response_parts.append(f"{i}. **{article['title']}**")
                if article.get('description'):
                    response_parts.append(f"   {article['description'][:150]}...")
                response_parts.append(f"   *Source: {article.get('url', 'N/A')}*")
        
        # Add weather information
        if search_results['weather']:
            weather = search_results['weather']
            response_parts.append(f"**Current Weather:**")
            response_parts.append(f"Temperature: {weather['temperature']}°C")
            response_parts.append(f"Conditions: {weather['description']}")
            response_parts.append(f"Humidity: {weather['humidity']}%")
            response_parts.append(f"Wind Speed: {weather['wind_speed']} m/s")
        
        # Add currency information
        if search_results['currency']:
            currency = search_results['currency']
            response_parts.append(f"**Exchange Rate:**")
            response_parts.append(f"1 {currency['base']} = {currency['rate']} (as of {currency['date']})")
        
        # If no specific information found, provide general response
        if not response_parts:
            response_parts.append("I've searched for current information about your query, but I couldn't find specific real-time data. However, I can provide general information about this topic.")
            
            # Add knowledge base information if relevant
            for concept, description in self.knowledge['ai_concepts'].items():
                if concept.replace('_', ' ') in message_lower:
                    response_parts.append(f"**General Information:** {description}")
                    break
        
        # Add timestamp and source information
        response_parts.append(f"\n*Information gathered on {datetime.now().strftime('%B %d, %Y at %I:%M %p')} from multiple sources including DuckDuckGo, Wikipedia, and news APIs.*")
        
        return "\n\n".join(response_parts)
    
    def get_response(self, message):
        """Generate an informed response based on real-time internet data"""
        message_lower = message.lower()
        self.conversation_history.append({"user": message, "bot": "", "timestamp": datetime.now().strftime("%H:%M")})
        
        # Handle simple greetings without internet search
        if any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            response = "Hello! I'm an AI assistant with access to real-time information from the internet. I can search for current news, weather, currency rates, and general information to provide you with accurate, up-to-date answers. What would you like to know about?"
        
        # Handle goodbye
        elif any(word in message_lower for word in ['bye', 'goodbye', 'see you', 'exit']):
            response = "Goodbye! Thanks for using my real-time information services. Feel free to come back anytime for current and accurate information!"
        
        # For all other queries, search the internet
        else:
            print(f"🔍 Searching internet for: {message}")
            search_results = self.search_web(message)
            response = self.generate_informed_response(message, search_results)
        
        # Update the last message with bot response
        if self.conversation_history:
            self.conversation_history[-1]["bot"] = response
        
        return response

# Create advanced AI instance
ai_assistant = AdvancedInternetAI()

@app.route('/')
def home():
    return render_template('enhanced_chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    
    if message.strip():
        response = ai_assistant.get_response(message)
        return jsonify({
            'response': response,
            'timestamp': datetime.now().strftime("%H:%M")
        })
    
    return jsonify({'response': 'Please enter a message!', 'timestamp': datetime.now().strftime("%H:%M")})

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    
    if query.strip():
        results = ai_assistant.search_web(query)
        return jsonify({
            'results': results,
            'query': query
        })
    
    return jsonify({'results': {}, 'error': 'Please provide a search query'})

@app.route('/history')
def history():
    return jsonify(ai_assistant.conversation_history)

@app.route('/status')
def status():
    return jsonify({
        'bot_name': 'Advanced Internet AI',
        'messages_count': len(ai_assistant.conversation_history),
        'status': 'online',
        'features': ['Real-time Web Search', 'Current News', 'Weather Data', 'Currency Rates', 'Wikipedia Integration']
    })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("🚀 Advanced Internet AI Assistant Starting...")
    print("🌐 Open your browser and go to: http://localhost:8080")
    print("🤖 Features: Real-time web search, current news, weather, currency rates")
    print("📡 APIs: DuckDuckGo, Wikipedia, NewsAPI, OpenWeatherMap, ExchangeRate-API")
    print("=" * 70)
    
    app.run(debug=True, host='0.0.0.0', port=8080) 