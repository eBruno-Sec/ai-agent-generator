# 🔐 API Keys Setup Guide

This guide explains how to obtain and configure all API keys needed for the AI Security Agent Generator.

---

## 📋 Table of Contents

1. [Quick Setup](#quick-setup)
2. [LLM Provider Keys](#llm-provider-keys)
3. [Security Tool Keys](#security-tool-keys)
4. [Secret Management](#secret-management)
5. [Notification Services](#notification-services)
6. [Security Best Practices](#security-best-practices)

---

## Quick Setup

### Step 1: Copy the Example File

```bash
cp .env.example .env
```

### Step 2: Edit the .env File

```bash
# Use your preferred editor
nano .env
# or
vim .env
# or
code .env
```

### Step 3: Add Your Keys

Fill in at least one LLM provider key (required if using LLM-based agents).

---

## LLM Provider Keys

### 🤖 OpenAI (GPT-4, GPT-3.5)

**Get your key:**
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)

**Add to .env:**
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

**Cost:** Pay-as-you-go (GPT-4: ~$0.03/1K tokens, GPT-3.5: ~$0.002/1K tokens)

---

### 🧠 Anthropic Claude (Recommended for Security)

**Get your key:**
1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Navigate to API Keys
4. Create a new API key
5. Copy the key (starts with `sk-ant-`)

**Add to .env:**
```bash
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

**Why Claude for Security?**
- Better at analysis and reasoning
- Stronger safety guardrails
- Excellent for security context
- Good at structured output

**Cost:** Pay-as-you-go (Claude Sonnet: ~$0.015/1K tokens)

---

### ☁️ Azure OpenAI

**Get your keys:**
1. Go to https://portal.azure.com/
2. Create an Azure OpenAI resource
3. Get your endpoint and key
4. Deploy a model (e.g., gpt-4)

**Add to .env:**
```bash
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_API_VERSION=2023-05-15
```

---

### 🔷 Google Gemini

**Get your key:**
1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

**Add to .env:**
```bash
GOOGLE_API_KEY=your-google-key-here
```

---

### ⚡ Groq (Fast Inference)

**Get your key:**
1. Go to https://console.groq.com/
2. Sign up for an account
3. Navigate to API Keys
4. Create a new key

**Add to .env:**
```bash
GROQ_API_KEY=your-groq-key-here
```

**Benefit:** Very fast inference speeds

---

### 🏠 Local Ollama (No API Key Needed)

**Setup:**
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3

# Or for coding
ollama pull codellama
```

**No .env configuration needed!**

Just select "Local Ollama" when generating your agent.

---

## Security Tool Keys

### 🔍 Shodan (IoT/Device Search)

**Get your key:**
1. Go to https://account.shodan.io/
2. Sign up for an account
3. Navigate to "My Account"
4. Copy your API key

**Add to .env:**
```bash
SHODAN_API_KEY=your-shodan-key
```

**Cost:** Free tier available, Premium $59/month

---

### 🌐 Censys (Internet Scanning)

**Get your credentials:**
1. Go to https://censys.io/
2. Sign up for an account
3. Navigate to API settings
4. Copy API ID and Secret

**Add to .env:**
```bash
CENSYS_API_ID=your-api-id
CENSYS_API_SECRET=your-api-secret
```

---

### 🦠 VirusTotal (Malware Analysis)

**Get your key:**
1. Go to https://www.virustotal.com/
2. Sign up or log in
3. Navigate to your profile → API Key
4. Copy the key

**Add to .env:**
```bash
VIRUSTOTAL_API_KEY=your-virustotal-key
```

**Limits:** Free tier: 4 requests/minute

---

### 🔎 SecurityTrails (DNS/Domain Intelligence)

**Get your key:**
1. Go to https://securitytrails.com/
2. Sign up for an account
3. Navigate to Account → API
4. Generate an API key

**Add to .env:**
```bash
SECURITYTRAILS_API_KEY=your-key
```

---

## Secret Management

### Environment Variables (Development)

**Pros:**
- Simple to use
- Works everywhere
- Good for development

**Cons:**
- Less secure
- Manual rotation
- Risk of exposure

**Usage:**
```bash
# Load from .env file
source .env

# Or use in Python
from dotenv import load_dotenv
load_dotenv()
```

---

### Docker Secrets (Docker Swarm)

**Create secret:**
```bash
echo "sk-your-api-key" | docker secret create openai_api_key -
```

**Use in docker-compose.yml:**
```yaml
services:
  agent:
    image: my-agent
    secrets:
      - openai_api_key

secrets:
  openai_api_key:
    external: true
```

**Access in code:**
```python
with open('/run/secrets/openai_api_key', 'r') as f:
    api_key = f.read().strip()
```

---

### Kubernetes Secrets

**Create secret:**
```bash
kubectl create secret generic agent-secrets \
  --from-literal=openai-api-key=sk-your-key \
  --from-literal=anthropic-api-key=sk-ant-your-key
```

**Use in deployment:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-agent
spec:
  containers:
  - name: agent
    image: my-agent
    env:
    - name: OPENAI_API_KEY
      valueFrom:
        secretKeyRef:
          name: agent-secrets
          key: openai-api-key
```

---

### HashiCorp Vault (Enterprise)

**Setup:**
```bash
# Install Vault
brew install vault

# Start dev server
vault server -dev

# Set environment
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='your-token'

# Store secret
vault kv put secret/agent openai_key=sk-your-key
```

**Access in Python:**
```python
import hvac

client = hvac.Client(url='http://127.0.0.1:8200', token='your-token')
secret = client.secrets.kv.v2.read_secret_version(path='agent')
api_key = secret['data']['data']['openai_key']
```

---

### AWS Secrets Manager

**Create secret:**
```bash
aws secretsmanager create-secret \
  --name agent/openai-key \
  --secret-string sk-your-key
```

**Access in Python:**
```python
import boto3

client = boto3.client('secretsmanager')
response = client.get_secret_value(SecretId='agent/openai-key')
api_key = response['SecretString']
```

---

### Azure Key Vault

**Create secret:**
```bash
az keyvault secret set \
  --vault-name MyKeyVault \
  --name openai-api-key \
  --value sk-your-key
```

**Access in Python:**
```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://MyKeyVault.vault.azure.net/", credential=credential)
secret = client.get_secret("openai-api-key")
api_key = secret.value
```

---

## Notification Services

### 💬 Slack

**Setup:**
1. Go to https://api.slack.com/apps
2. Create a new app
3. Enable Incoming Webhooks
4. Add webhook to workspace
5. Copy webhook URL

**Add to .env:**
```bash
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
SLACK_CHANNEL=#security-alerts
```

---

### 🎮 Discord

**Setup:**
1. Open Discord server settings
2. Go to Integrations → Webhooks
3. Create new webhook
4. Copy webhook URL

**Add to .env:**
```bash
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR/WEBHOOK
```

---

### 📧 Email (SMTP)

**Gmail Example:**
1. Enable 2FA on your Google account
2. Generate an App Password:
   - Go to https://myaccount.google.com/security
   - App passwords
   - Generate new password

**Add to .env:**
```bash
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

---

## Security Best Practices

### ✅ DO:

1. **Use .env files for development only**
2. **Never commit .env files to Git** (already in .gitignore)
3. **Use secret management for production** (Vault, AWS Secrets, etc.)
4. **Rotate keys regularly** (every 90 days minimum)
5. **Use separate keys for dev/staging/production**
6. **Limit API key permissions** (principle of least privilege)
7. **Monitor API key usage** (detect anomalies)
8. **Use key expiration** when available
9. **Encrypt keys at rest** in production
10. **Log key access** for audit trails

### ❌ DON'T:

1. **Never hardcode API keys in source code**
2. **Never commit keys to version control**
3. **Never share keys in chat/email**
4. **Never use production keys in development**
5. **Never log API keys** (even in debug mode)
6. **Never include keys in error messages**
7. **Never expose keys in URLs or query parameters**
8. **Never use the same key across multiple projects**

---

## Testing Your Setup

### Test LLM Connection

**OpenAI:**
```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "test"}]
)
print("✅ OpenAI connection successful!")
```

**Anthropic:**
```python
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=10,
    messages=[{"role": "user", "content": "test"}]
)
print("✅ Anthropic connection successful!")
```

### Test Tool Keys

**Shodan:**
```python
import shodan
import os

api = shodan.Shodan(os.getenv('SHODAN_API_KEY'))
info = api.info()
print(f"✅ Shodan connected! Query credits: {info['query_credits']}")
```

---

## Troubleshooting

### "API key not found" Error

```bash
# Check if .env file exists
ls -la .env

# Check if keys are set
env | grep API_KEY

# Load .env manually
source .env

# Or in Python
from dotenv import load_dotenv
load_dotenv()
import os
print(os.getenv('OPENAI_API_KEY'))
```

### "Invalid API key" Error

1. Check for extra spaces or newlines
2. Verify key hasn't expired
3. Ensure key has correct prefix (sk-, sk-ant-, etc.)
4. Check if key is enabled in provider dashboard
5. Verify billing is set up (for paid APIs)

### "Rate limit exceeded" Error

1. Check your API usage dashboard
2. Implement rate limiting in your code
3. Upgrade to higher tier if needed
4. Use caching to reduce API calls

---

## Cost Management

### Monitor Usage

**OpenAI:**
- Dashboard: https://platform.openai.com/usage
- Set up usage limits
- Enable billing alerts

**Anthropic:**
- Console: https://console.anthropic.com/
- Monitor token usage
- Set budget limits

### Reduce Costs

1. **Use cheaper models** (GPT-3.5 instead of GPT-4)
2. **Implement caching** (don't re-process same data)
3. **Reduce token usage** (shorter prompts, lower max_tokens)
4. **Use local models** for non-critical tasks
5. **Batch requests** when possible
6. **Set rate limits** in your agents

---

## Quick Reference

| Provider | Key Prefix | Cost (approx) | Best For |
|----------|-----------|---------------|----------|
| OpenAI GPT-4 | `sk-` | $0.03/1K tokens | General purpose |
| Anthropic Claude | `sk-ant-` | $0.015/1K tokens | Security analysis |
| Azure OpenAI | various | Pay-as-you-go | Enterprise |
| Google Gemini | various | Free tier available | Experimentation |
| Local Ollama | N/A | Free | Privacy, offline |
| Groq | various | Free tier | Speed |

---

## Need Help?

- Check the [Quick Start Guide](QUICK_START.md)
- Review [Security Best Practices](https://owasp.org/www-project-api-security/)
- Open an issue on GitHub

---

**Pro Tip:** Start with Anthropic Claude for security agents - it's specifically good at analysis and reasoning tasks, which are core to security operations.
