#!/bin/bash

# Create .env file with user's API keys
cat > .env << EOF
# Backend API Keys
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
COHERE_API_KEY=your_cohere_api_key_here

# Database
DATABASE_URL=your_database_url_here

# JWT Secret (for frontend auth)
JWT_SECRET=your_jwt_secret_here

# Docker Hub
DOCKERHUB_USERNAME=your_dockerhub_username
DOCKERHUB_TOKEN=your_dockerhub_token_here

# Frontend
NEXT_PUBLIC_API_BASE_URL=https://your-app.onrender.com
EOF

echo "✅ .env file created with your API keys!"
echo "🔒 Remember to add .env to .gitignore to keep your keys secure" 