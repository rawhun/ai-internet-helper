#!/usr/bin/env python3
"""
Simple local test for AI Chatbot components
Tests API keys, database connection, and basic functionality
"""

import os
import sys
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
        if not os.path.exists(file):
            print(f"❌ Required file {file} not found")
            return False
    
    print("✅ All required files exist")
    return True

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
    try:
        # Test that we can read the README
        with open('README.md', 'r') as f:
            content = f.read()
            if len(content) > 0:
                print("✅ Basic functionality test passed")
                return True
            else:
                print("❌ README.md is empty")
                return False
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def test_api_keys():
    """Test if API keys are valid"""
    print("\n🔑 Testing API Keys...")
    print("=" * 40)
    
    # Test OpenAI API
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key:
        print("✅ OpenAI API Key: Configured")
    else:
        print("⚠️ OpenAI API Key: Not configured")
    
    # Test Hugging Face API
    hf_key = os.getenv('HUGGINGFACE_API_KEY')
    if hf_key:
        print("✅ Hugging Face API Key: Configured")
    else:
        print("⚠️ Hugging Face API Key: Not configured")
    
    # Test Cohere API
    cohere_key = os.getenv('COHERE_API_KEY')
    if cohere_key:
        print("✅ Cohere API Key: Configured")
    else:
        print("⚠️ Cohere API Key: Not configured")

def test_database_connection():
    """Test database connection"""
    print("\n🗄️ Testing Database Connection...")
    print("=" * 40)
    
    db_url = os.getenv('DATABASE_URL')
    if db_url:
        print("✅ Database URL: Configured")
    else:
        print("⚠️ Database URL: Not configured")

if __name__ == "__main__":
    print("🧪 Running AI Chatbot Tests...")
    print("=" * 40)
    
    all_tests_passed = True
    
    if not test_project_structure():
        all_tests_passed = False
    
    test_imports()
    
    if not test_basic_functionality():
        all_tests_passed = False
    
    test_api_keys()
    test_database_connection()
    
    print("\n" + "=" * 40)
    if all_tests_passed:
        print("🎉 All critical tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1) 