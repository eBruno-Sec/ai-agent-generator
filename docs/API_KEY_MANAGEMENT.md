# 🔐 API Key Management Guide

## Overview

The AI Agent Generator supports multiple methods for managing API keys and secrets securely.

---

## 🔑 Required API Keys

### LLM Provider Keys

| Provider | Key Name | Get Key |
|----------|----------|----------|
| **Anthropic** ⭐ | `ANTHROPIC_API_KEY` | https://console.anthropic.com/settings/keys |
| **OpenAI** | `OPENAI_API_KEY` | https://platform.openai.com/api-keys |
| **Azure OpenAI** | `AZURE_OPENAI_API_KEY` | Azure Portal |
| **Google** | `GOOGLE_API_KEY` | Google Cloud Console |
| **Groq** | `GROQ_API_KEY` | https://console.groq.com/keys |

---

## 📋 Method 1: Environment Variables (.env file)

**Best for:** Development, testing, Docker

### Setup:

```bash
cd output/your-agent-name

# Create .env file
cat > .env << 'EOF'
# LLM Provider
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here

# Optional: Tool Keys
SHODAN_API_KEY=your-shodan-key

# Configuration
LOG_LEVEL=INFO
EOF

# Secure the file
chmod 600 .env
```

### Usage in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('ANTHROPIC_API_KEY')
```

### Usage with Docker:

```bash
# Pass .env file
docker run --env-file .env your-agent

# Or pass individual variables
docker run -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY your-agent
```

---

## 📋 Method 2: Docker Secrets

**Best for:** Docker Swarm, production

```bash
# Create secrets
echo "sk-ant-api03-xxx" | docker secret create anthropic_key -

# Use in service
docker service create \
  --name agent \
  --secret anthropic_key \
  your-agent-image
```

**Read in code:**
```python
def read_docker_secret(name):
    path = f'/run/secrets/{name}'
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return None

api_key = read_docker_secret('anthropic_key')
```

---

## 📋 Method 3: Kubernetes Secrets

**Best for:** Kubernetes deployments

```bash
# Create secret
kubectl create secret generic api-keys \
  --from-literal=anthropic-key='sk-ant-xxx'
```

**deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: security-agent
spec:
  template:
    spec:
      containers:
      - name: agent
        env:
        - name: ANTHROPIC_API_KEY
          valueFrom:
            secretKeyRef:
              name: api-keys
              key: anthropic-key
```

---

## 🔒 Security Best Practices

### ✅ DO:
- Rotate keys every 90 days
- Use separate keys for dev/prod  
- Add .env to .gitignore
- Use secret management in production
- Monitor key usage

### ❌ DON'T:
- Never commit keys to git
- Never hardcode keys in code
- Never share keys via email/chat
- Never log API keys

---

## 📝 .env Template

```bash
# .env.example - Copy to .env and add your keys

# Anthropic (Recommended)
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here

# OpenAI (Optional)
# OPENAI_API_KEY=sk-proj-your-key-here

# Optional Tool Keys
# SHODAN_API_KEY=your-key
# VIRUSTOTAL_API_KEY=your-key

# Configuration
LOG_LEVEL=INFO
DEBUG=false
MAX_REQUESTS_PER_MINUTE=10
```

---

## 🧪 Test Your Keys

### Test Anthropic:
```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-3-5-sonnet-20241022","max_tokens":10,"messages":[{"role":"user","content":"Hi"}]}'
```

### Test OpenAI:
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{"model":"gpt-4","messages":[{"role":"user","content":"Hi"}]}'
```

---

## 🚨 Key Compromised?

1. **Revoke immediately** at provider console
2. **Generate new key**
3. **Update all environments**
4. **Review access logs**

---

## 📚 Get API Keys

- **Anthropic Claude:** https://console.anthropic.com/settings/keys
- **OpenAI:** https://platform.openai.com/api-keys
- **Shodan:** https://account.shodan.io/
- **VirusTotal:** https://www.virustotal.com/gui/my-apikey

---

**Remember: Treat API keys like passwords! 🔐**
