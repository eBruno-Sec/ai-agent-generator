#!/bin/bash
# API Key Setup Script for AI Security Agent Generator

set -e

echo "============================================"
echo "🔐 API Key Setup Wizard"
echo "============================================"
echo ""

# Check if .env already exists
if [ -f .env ]; then
    echo "⚠️  .env file already exists!"
    read -p "Do you want to overwrite it? (y/N): " overwrite
    if [[ ! $overwrite =~ ^[Yy]$ ]]; then
        echo "Exiting without changes."
        exit 0
    fi
    cp .env .env.backup
    echo "✓ Backed up existing .env to .env.backup"
fi

# Copy template
cp .env.example .env
echo "✓ Created .env file from template"
echo ""

# Function to update env var
update_env() {
    local key=$1
    local value=$2
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s|^${key}=.*|${key}=${value}|" .env
    else
        sed -i "s|^${key}=.*|${key}=${value}|" .env
    fi
}

echo "============================================"
echo "📋 LLM Provider Setup (Choose at least one)"
echo "============================================"
echo ""

# OpenAI
read -p "Do you want to configure OpenAI? (y/N): " setup_openai
if [[ $setup_openai =~ ^[Yy]$ ]]; then
    echo ""
    echo "Get your OpenAI API key from: https://platform.openai.com/api-keys"
    read -p "Enter your OpenAI API key (starts with sk-): " openai_key
    if [ ! -z "$openai_key" ]; then
        update_env "OPENAI_API_KEY" "$openai_key"
        echo "✓ OpenAI API key configured"
    fi
fi

echo ""

# Anthropic
read -p "Do you want to configure Anthropic Claude? (y/N): " setup_anthropic
if [[ $setup_anthropic =~ ^[Yy]$ ]]; then
    echo ""
    echo "Get your Anthropic API key from: https://console.anthropic.com/"
    read -p "Enter your Anthropic API key (starts with sk-ant-): " anthropic_key
    if [ ! -z "$anthropic_key" ]; then
        update_env "ANTHROPIC_API_KEY" "$anthropic_key"
        echo "✓ Anthropic API key configured"
    fi
fi

echo ""

# Google
read -p "Do you want to configure Google Gemini? (y/N): " setup_google
if [[ $setup_google =~ ^[Yy]$ ]]; then
    echo ""
    echo "Get your Google API key from: https://makersuite.google.com/app/apikey"
    read -p "Enter your Google API key: " google_key
    if [ ! -z "$google_key" ]; then
        update_env "GOOGLE_API_KEY" "$google_key"
        echo "✓ Google API key configured"
    fi
fi

echo ""

# Local Ollama
read -p "Are you using Local Ollama? (y/N): " use_ollama
if [[ $use_ollama =~ ^[Yy]$ ]]; then
    echo ""
    echo "Checking if Ollama is installed..."
    if command -v ollama &> /dev/null; then
        echo "✓ Ollama is installed"
        echo ""
        echo "Available models:"
        ollama list
        echo ""
        echo "To pull a new model, run: ollama pull <model-name>"
        echo "Recommended models: llama3, mistral, codellama"
    else
        echo "⚠️  Ollama is not installed"
        echo "Install from: https://ollama.com/download"
    fi
fi

echo ""
echo "============================================"
echo "🛠️  Security Tools (Optional)"
echo "============================================"
echo ""

# Shodan
read -p "Do you want to configure Shodan? (y/N): " setup_shodan
if [[ $setup_shodan =~ ^[Yy]$ ]]; then
    echo ""
    echo "Get your Shodan API key from: https://account.shodan.io/"
    read -p "Enter your Shodan API key: " shodan_key
    if [ ! -z "$shodan_key" ]; then
        update_env "SHODAN_API_KEY" "$shodan_key"
        echo "✓ Shodan API key configured"
    fi
fi

echo ""

# VirusTotal
read -p "Do you want to configure VirusTotal? (y/N): " setup_vt
if [[ $setup_vt =~ ^[Yy]$ ]]; then
    echo ""
    echo "Get your VirusTotal API key from: https://www.virustotal.com/gui/my-apikey"
    read -p "Enter your VirusTotal API key: " vt_key
    if [ ! -z "$vt_key" ]; then
        update_env "VIRUSTOTAL_API_KEY" "$vt_key"
        echo "✓ VirusTotal API key configured"
    fi
fi

echo ""
echo "============================================"
echo "📬 Notifications (Optional)"
echo "============================================"
echo ""

# Slack
read -p "Do you want to configure Slack notifications? (y/N): " setup_slack
if [[ $setup_slack =~ ^[Yy]$ ]]; then
    echo ""
    echo "Create a webhook at: https://api.slack.com/apps"
    read -p "Enter your Slack webhook URL: " slack_url
    if [ ! -z "$slack_url" ]; then
        update_env "SLACK_WEBHOOK_URL" "$slack_url"
        read -p "Enter Slack channel (e.g., #security-alerts): " slack_channel
        if [ ! -z "$slack_channel" ]; then
            update_env "SLACK_CHANNEL" "$slack_channel"
        fi
        echo "✓ Slack notifications configured"
    fi
fi

echo ""
echo "============================================"
echo "✅ Setup Complete!"
echo "============================================"
echo ""
echo "Your API keys have been saved to .env"
echo ""
echo "⚠️  IMPORTANT SECURITY REMINDERS:"
echo "1. Never commit .env to version control"
echo "2. Keep your API keys secret"
echo "3. Rotate keys regularly"
echo "4. Use separate keys for dev/prod"
echo ""
echo "Next steps:"
echo "1. Review your .env file: cat .env"
echo "2. Test your setup: python scripts/test_api_keys.py"
echo "3. Generate your first agent: python generator.py --interactive"
echo ""
echo "📚 For more details, see: docs/API_KEYS_SETUP.md"
echo ""
