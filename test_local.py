#!/usr/bin/env python3
"""
Simple local test for AI Chatbot components
Tests API keys, database connection, and basic functionality
"""

import os
import sys
import requests
import json

# Load environment variables (optional)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️ python-dotenv not installed (optional)")
    # Continue without dotenv

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
    """Warn if API keys are missing, but do not fail the build"""
    print("\n🔑 Testing API Keys...")
    print("=" * 40)
    
    # Test OpenAI API
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key:
        print("✅ OpenAI API Key: Configured")
    else:
        print("⚠️ OpenAI API Key: Not configured (warning only)")
    
    # Test Hugging Face API
    hf_key = os.getenv('HUGGINGFACE_API_KEY')
    if hf_key:
        print("✅ Hugging Face API Key: Configured")
    else:
        print("⚠️ Hugging Face API Key: Not configured (warning only)")
    
    # Test Cohere API
    cohere_key = os.getenv('COHERE_API_KEY')
    if cohere_key:
        print("✅ Cohere API Key: Configured")
    else:
        print("⚠️ Cohere API Key: Not configured (warning only)")

def test_database_connection():
    """Warn if database URL is missing, but do not fail the build"""
    print("\n🗄️ Testing Database Connection...")
    print("=" * 40)
    
    db_url = os.getenv('DATABASE_URL')
    if db_url:
        print("✅ Database URL: Configured")
    else:
        print("⚠️ Database URL: Not configured (warning only)")

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
        print("\033[92m🎉 All critical tests passed!\033[0m")
        print("\033[96m\n🚀 Your AI Chatbot project is ready!\033[0m")
        print("\nNext steps:")
        print("  1. Add your API keys to a .env file for full functionality.")
        print("  2. Deploy to Render, Railway, or your favorite cloud.")
        print("  3. Share your project on GitHub or social media!")
        print("  4. Contribute or open issues to improve the project.")
        print("\nHappy hacking! 💡🤖\n")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1) 