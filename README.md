# 🤖 Advanced Internet AI Assistant

A sophisticated AI chatbot that fetches real-time information from multiple internet sources to provide accurate, up-to-date responses like modern AI assistants.

## 🌟 Features

### 🔍 Real-Time Information Gathering
- **DuckDuckGo Integration**: Instant answers and web search
- **Wikipedia API**: Detailed information and summaries
- **News API**: Breaking news and current events
- **Weather Data**: Real-time weather for any location
- **Currency Rates**: Live exchange rates and financial data
- **Multiple Source Verification**: Combines information from various APIs

### 🎨 Modern Web Interface
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark Mode**: Beautiful dark theme with gradients
- **Real-time Chat**: Smooth scrolling and animations
- **Auto-resize Input**: Dynamic textarea that grows with content
- **Typing Indicators**: Visual feedback during AI processing

### 🚀 Advanced Capabilities
- **Context Analysis**: Understands user intent and topic
- **Smart Caching**: Improves response speed for repeated queries
- **Error Handling**: Graceful fallbacks when APIs are unavailable
- **Source Attribution**: Shows where information comes from
- **Timestamped Responses**: Displays when data was gathered

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Ai-Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip3 install flask requests wikipedia newsapi-python beautifulsoup4 feedparser
   ```

3. **Run the application**
   ```bash
   python3 enhanced_chatbot.py
   ```

4. **Open in browser**
   ```
   http://localhost:8080
   ```

## 📡 API Configuration

The application uses several free APIs. For enhanced functionality, you can add your own API keys:

### Optional API Keys
- **NewsAPI**: Get a free key from [newsapi.org](https://newsapi.org)
- **OpenWeatherMap**: Get a free key from [openweathermap.org](https://openweathermap.org/api)

To use API keys, edit the `enhanced_chatbot.py` file and replace the demo keys:
```python
self.news_api_key = "your_news_api_key_here"
```

## 🎯 Usage Examples

### Weather Queries
- "What's the weather in New York?"
- "Temperature in London today"
- "Weather forecast for Tokyo"

### Current Events
- "Latest news about AI"
- "What's happening in technology today?"
- "Breaking news about space exploration"

### Financial Data
- "Current Bitcoin price"
- "Convert 100 USD to EUR"
- "Latest stock market news"

### General Information
- "Who won the latest election?"
- "Current COVID-19 statistics"
- "Latest SpaceX launch details"

### Currency & Finance
- "USD to EUR exchange rate"
- "Bitcoin price today"
- "Stock market performance"

## 🏗️ Project Structure

```
Ai-Chatbot/
├── enhanced_chatbot.py      # Main application file
├── templates/
│   └── enhanced_chat.html   # Web interface template
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 🔧 Technical Details

### Backend Technologies
- **Flask**: Web framework for the API
- **Requests**: HTTP library for API calls
- **Wikipedia**: Python library for Wikipedia access
- **NewsAPI**: News aggregation service
- **BeautifulSoup**: HTML parsing for web scraping

### Frontend Technologies
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **JavaScript**: Dynamic interactions and API calls
- **Responsive Design**: Mobile-first approach

### APIs Integrated
- **DuckDuckGo**: Instant answers and web search
- **Wikipedia**: Knowledge base and detailed information
- **NewsAPI**: Current events and breaking news
- **OpenWeatherMap**: Real-time weather data
- **ExchangeRate-API**: Currency conversion rates
- **RSS Feeds**: Fallback news sources

## 🚀 Deployment

### Local Development
```bash
python3 enhanced_chatbot.py
```

### Production Deployment
For production deployment, consider using:
- **Gunicorn**: WSGI server
- **Nginx**: Reverse proxy
- **Docker**: Containerization
- **Cloud Platforms**: Render, Railway, or Heroku

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Hugging Face**: For AI model inspiration
- **DuckDuckGo**: For privacy-focused search
- **Wikipedia**: For comprehensive knowledge base
- **NewsAPI**: For current events data
- **OpenWeatherMap**: For weather information

## 📞 Support

If you encounter any issues or have questions:
- Create an issue in the GitHub repository
- Check the troubleshooting section below
- Review the API documentation for external services

## 🔍 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change port in enhanced_chatbot.py
   app.run(debug=True, host='0.0.0.0', port=8081)
   ```

2. **API rate limits**
   - The application includes fallback mechanisms
   - Consider adding your own API keys for better performance

3. **Module not found errors**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Network connectivity issues**
   - Check your internet connection
   - Verify firewall settings
   - Try using a VPN if needed

## 🔮 Future Enhancements

- [ ] Voice input/output capabilities
- [ ] Image recognition and analysis
- [ ] Multi-language support
- [ ] Advanced conversation memory
- [ ] Integration with more APIs
- [ ] Mobile app development
- [ ] Advanced analytics and insights
- [ ] Custom model training capabilities

---

**Built with ❤️ by rawhun**

*Connect with me: txrun@rediffmail.com*
