#!/usr/bin/env python3
"""
API Key Tester
Tests all configured API keys to ensure they work correctly
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def print_header(text):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def test_openai():
    """Test OpenAI API key"""
    key = os.getenv('OPENAI_API_KEY')
    if not key:
        print("⏭️  OpenAI: Not configured (skipping)")
        return
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "test"}],
            max_tokens=5
        )
        print("✅ OpenAI: Connection successful!")
        print(f"   Model: gpt-3.5-turbo")
    except ImportError:
        print("⚠️  OpenAI: Package not installed (pip install openai)")
    except Exception as e:
        print(f"❌ OpenAI: Failed - {str(e)}")

def test_anthropic():
    """Test Anthropic API key"""
    key = os.getenv('ANTHROPIC_API_KEY')
    if not key:
        print("⏭️  Anthropic: Not configured (skipping)")
        return
    
    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=key)
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=10,
            messages=[{"role": "user", "content": "test"}]
        )
        print("✅ Anthropic: Connection successful!")
        print(f"   Model: claude-3-5-sonnet")
    except ImportError:
        print("⚠️  Anthropic: Package not installed (pip install anthropic)")
    except Exception as e:
        print(f"❌ Anthropic: Failed - {str(e)}")

def test_google():
    """Test Google API key"""
    key = os.getenv('GOOGLE_API_KEY')
    if not key:
        print("⏭️  Google Gemini: Not configured (skipping)")
        return
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("test")
        print("✅ Google Gemini: Connection successful!")
        print(f"   Model: gemini-pro")
    except ImportError:
        print("⚠️  Google: Package not installed (pip install google-generativeai)")
    except Exception as e:
        print(f"❌ Google Gemini: Failed - {str(e)}")

def test_ollama():
    """Test Ollama connection"""
    try:
        import requests
        response = requests.get('http://localhost:11434/api/tags', timeout=2)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print("✅ Ollama: Running locally")
            if models:
                print(f"   Available models: {len(models)}")
                for model in models[:3]:  # Show first 3
                    print(f"     - {model['name']}")
            else:
                print("   ⚠️  No models installed. Run: ollama pull llama3")
        else:
            print("❌ Ollama: Not responding correctly")
    except ImportError:
        print("⚠️  Ollama: requests package not installed")
    except Exception as e:
        print(f"⏭️  Ollama: Not running ({str(e)})")
        print("   Install from: https://ollama.com/download")

def test_shodan():
    """Test Shodan API key"""
    key = os.getenv('SHODAN_API_KEY')
    if not key:
        print("⏭️  Shodan: Not configured (skipping)")
        return
    
    try:
        import shodan
        api = shodan.Shodan(key)
        info = api.info()
        print("✅ Shodan: Connection successful!")
        print(f"   Query credits: {info.get('query_credits', 'N/A')}")
        print(f"   Scan credits: {info.get('scan_credits', 'N/A')}")
    except ImportError:
        print("⚠️  Shodan: Package not installed (pip install shodan)")
    except Exception as e:
        print(f"❌ Shodan: Failed - {str(e)}")

def test_virustotal():
    """Test VirusTotal API key"""
    key = os.getenv('VIRUSTOTAL_API_KEY')
    if not key:
        print("⏭️  VirusTotal: Not configured (skipping)")
        return
    
    try:
        import requests
        headers = {'x-apikey': key}
        response = requests.get(
            'https://www.virustotal.com/api/v3/users/current',
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            print("✅ VirusTotal: Connection successful!")
            data = response.json().get('data', {}).get('attributes', {})
            print(f"   Username: {data.get('username', 'N/A')}")
        else:
            print(f"❌ VirusTotal: Failed - Status {response.status_code}")
    except ImportError:
        print("⚠️  VirusTotal: requests package not installed")
    except Exception as e:
        print(f"❌ VirusTotal: Failed - {str(e)}")

def test_slack():
    """Test Slack webhook"""
    webhook = os.getenv('SLACK_WEBHOOK_URL')
    if not webhook:
        print("⏭️  Slack: Not configured (skipping)")
        return
    
    try:
        import requests
        # Don't actually send a test message, just validate the URL format
        if webhook.startswith('https://hooks.slack.com/'):
            print("✅ Slack: Webhook URL configured")
            print("   ℹ️  Webhook format looks valid")
            print("   ℹ️  Send a test message from your agent to verify")
        else:
            print("❌ Slack: Invalid webhook URL format")
    except Exception as e:
        print(f"❌ Slack: Failed - {str(e)}")

def check_env_file():
    """Check if .env file exists"""
    if os.path.exists('.env'):
        print("✅ .env file found")
        return True
    else:
        print("❌ .env file not found!")
        print("\n   Create it by running:")
        print("   ./scripts/setup_api_keys.sh")
        print("   or")
        print("   cp .env.example .env")
        return False

def main():
    print_header("🔐 API Key Tester")
    
    # Check for .env file
    if not check_env_file():
        sys.exit(1)
    
    print("\nTesting configured API keys...\n")
    
    # Test LLM providers
    print_header("🤖 LLM Providers")
    test_openai()
    test_anthropic()
    test_google()
    test_ollama()
    
    # Test security tools
    print_header("🛠️  Security Tools")
    test_shodan()
    test_virustotal()
    
    # Test notifications
    print_header("📬 Notification Services")
    test_slack()
    
    # Summary
    print_header("✅ Testing Complete")
    print("Summary:")
    print("  - If you see ✅, that service is working correctly")
    print("  - If you see ❌, check your API key configuration")
    print("  - If you see ⏭️, that service is not configured (optional)")
    print("  - If you see ⚠️, you need to install a Python package")
    print("\nNext steps:")
    print("  1. Fix any ❌ errors above")
    print("  2. Install missing packages with: pip install <package>")
    print("  3. Generate your first agent: python generator.py --interactive")
    print("\n📚 For help, see: docs/API_KEYS_SETUP.md\n")

if __name__ == "__main__":
    main()
