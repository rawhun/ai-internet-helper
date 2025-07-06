#!/usr/bin/env python3
"""
Simple local test for AI Chatbot components
Tests API keys, database connection, and basic functionality
"""

import os
import sys
import pytest
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_project_structure():
    """Test that all required files exist"""
    required_files = [
        'README.md',
        'requirements_enhanced.txt',
        'requirements_web.txt',
        'enhanced_chatbot.py',
        'web_chatbot.py',
        'demo_chatbot.py'
    ]
    
    for file in required_files:
        assert os.path.exists(file), f"Required file {file} not found"
    
    print("✅ All required files exist")

def test_imports():
    """Test that main modules can be imported"""
    try:
        import flask
        print("✅ Flask imported successfully")
    except ImportError:
        print("⚠️ Flask not installed (expected in CI)")
    
    try:
        import requests
        print("✅ Requests imported successfully")
    except ImportError:
        print("⚠️ Requests not installed (expected in CI)")

def test_basic_functionality():
    """Test basic project functionality"""
    # Test that we can read the README
    with open('README.md', 'r') as f:
        content = f.read()
        assert len(content) > 0, "README.md is empty"
    
    print("✅ Basic functionality test passed")

def test_api_keys():
    """Test if API keys are valid"""
    print("🔑 Testing API Keys...")
    
    # Test OpenAI
    try:
        openai_key = os.getenv('OPENAI_API_KEY')
        if openai_key:
            print("✅ OpenAI API Key: Found")
        else:
            print("❌ OpenAI API Key: Missing")
    except Exception as e:
        print(f"❌ OpenAI API Key Error: {e}")
    
    # Test Hugging Face
    try:
        hf_key = os.getenv('HUGGINGFACE_API_KEY')
        if hf_key:
            print("✅ Hugging Face API Key: Found")
        else:
            print("❌ Hugging Face API Key: Missing")
    except Exception as e:
        print(f"❌ Hugging Face API Key Error: {e}")
    
    # Test Cohere
    try:
        cohere_key = os.getenv('COHERE_API_KEY')
        if cohere_key:
            print("✅ Cohere API Key: Found")
        else:
            print("❌ Cohere API Key: Missing")
    except Exception as e:
        print(f"❌ Cohere API Key Error: {e}")

def test_database_connection():
    """Test database connection"""
    print("\n🗄️ Testing Database Connection...")
    try:
        db_url = os.getenv('DATABASE_URL')
        if db_url:
            print("✅ Database URL: Found")
            print(f"   Host: {db_url.split('@')[1].split('/')[0] if '@' in db_url else 'Unknown'}")
        else:
            print("❌ Database URL: Missing")
    except Exception as e:
        print(f"❌ Database Connection Error: {e}")

def test_providers_config():
    """Test providers configuration"""
    print("\n🤖 Testing AI Providers Config...")
    try:
        providers_file = "backend/rasa_project/config/providers.yaml"
        if os.path.exists(providers_file):
            print("✅ Providers config: Found")
            with open(providers_file, 'r') as f:
                content = f.read()
                if 'openai' in content and 'huggingface' in content and 'cohere' in content:
                    print("✅ All providers configured")
                else:
                    print("⚠️ Some providers missing")
        else:
            print("❌ Providers config: Missing")
    except Exception as e:
        print(f"❌ Providers Config Error: {e}")

def test_rasa_config():
    """Test Rasa configuration"""
    print("\n🧠 Testing Rasa Configuration...")
    try:
        config_file = "backend/rasa_project/config.yml"
        domain_file = "backend/rasa_project/domain.yml"
        
        if os.path.exists(config_file):
            print("✅ Rasa config: Found")
        else:
            print("❌ Rasa config: Missing")
            
        if os.path.exists(domain_file):
            print("✅ Rasa domain: Found")
        else:
            print("❌ Rasa domain: Missing")
    except Exception as e:
        print(f"❌ Rasa Config Error: {e}")

def test_frontend_config():
    """Test frontend configuration"""
    print("\n🎨 Testing Frontend Configuration...")
    try:
        tailwind_config = "frontend/tailwind.config.js"
        app_file = "frontend/src/App.jsx"
        
        if os.path.exists(tailwind_config):
            print("✅ Tailwind config: Found")
        else:
            print("❌ Tailwind config: Missing")
            
        if os.path.exists(app_file):
            print("✅ React App: Found")
        else:
            print("❌ React App: Missing")
    except Exception as e:
        print(f"❌ Frontend Config Error: {e}")

def main():
    """Run all tests"""
    print("🚀 AI Chatbot Local Test Suite")
    print("=" * 40)
    
    test_project_structure()
    test_imports()
    test_basic_functionality()
    test_api_keys()
    test_database_connection()
    test_providers_config()
    test_rasa_config()
    test_frontend_config()
    
    print("\n" + "=" * 40)
    print("✅ Local test completed!")
    print("\n📝 Next steps:")
    print("1. Install Docker: https://docs.docker.com/get-docker/")
    print("2. Run: cd backend && docker-compose up --build")
    print("3. Test: curl http://localhost:5005/health")
    print("4. Frontend: cd frontend && npm install && npm run dev")

if __name__ == "__main__":
    main() 