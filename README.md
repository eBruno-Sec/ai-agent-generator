# 🤖 AI Security Agent Generator

**Create custom security agents in 3 minutes. No coding required.**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Easy](https://img.shields.io/badge/Difficulty-Beginner-brightgreen.svg)

---

## 🎯 What Does This Do?

This tool creates custom AI security agents for you. Just answer some questions, and you get:
- ✅ A complete security agent
- ✅ All the code files
- ✅ Docker setup
- ✅ Documentation
- ✅ Ready to run

**No programming needed!**

---

## 🚀 Super Simple 3-Step Guide

### Step 1: Get the Code

**Option A: If you have Git** (recommended)
```bash
git clone https://github.com/eBruno-Sec/ai-agent-generator.git
cd ai-agent-generator
```

**Option B: No Git? Download it**
1. Go to https://github.com/eBruno-Sec/ai-agent-generator
2. Click the green "Code" button
3. Click "Download ZIP"
4. Unzip the file
5. Open Terminal/Command Prompt
6. Type: `cd ` (with a space at the end)
7. Drag the unzipped folder into the terminal window
8. Press Enter

---

### Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

**If that doesn't work, try:**
```bash
pip3 install -r requirements.txt
```

**Still doesn't work?**
```bash
python -m pip install -r requirements.txt
```

---

### Step 3: Run the Generator

```bash
python generator.py --interactive
```

**If that doesn't work, try:**
```bash
python3 generator.py --interactive
```

---

## 📝 Follow the Questions

The generator will ask you questions. Just answer them!

### Example Conversation:

```
❓ Agent name?
   Example: recon-spider-v1
   > my-first-agent

❓ Describe your agent
   > This is my first security agent

❓ Primary agent type?
   1. Reconnaissance
   2. Vulnerability Assessment
   3. Exploitation Testing
   ...
   Select (number): 1

❓ Framework?
   1. Custom Python
   2. LangChain
   ...
   Select (number): 1

❓ Target environments?
   Options (comma-separated numbers):
   1. Web Applications
   2. Network Infrastructure
   ...
   Select (e.g., 1,3,5): 1

❓ LLM Provider?
   1. OpenAI
   2. Anthropic
   3. None
   ...
   Select (number): 3

❓ Report formats?
   1. JSON
   2. HTML
   ...
   Select (e.g., 1,2): 1,2

❓ Deployment?
   1. Docker
   2. Kubernetes
   ...
   Select (number): 1

❓ API key management?
   1. Environment Variables
   2. Docker Secrets
   ...
   Select (number): 1
```

**Done!** Your agent is created in the `output/` folder!

---

## 🎉 Your Agent is Ready!

After answering the questions, you'll see:

```
✅ Agent generated successfully!

📂 Location: output/my-first-agent

🚀 Next steps:
   1. cd output/my-first-agent
   2. pip install -r requirements.txt
   3. python agent.py --help
```

---

## 🔑 If You Need API Keys

**Only needed if you picked "Anthropic" or "OpenAI" as your LLM provider.**

### Get Your API Key:

**For Anthropic (Claude):**
1. Go to https://console.anthropic.com/settings/keys
2. Click "Create Key"
3. Copy the key (starts with `sk-ant-`)

**For OpenAI (GPT-4):**
1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-proj-`)

### Add Your API Key:

```bash
cd output/my-first-agent

# Create .env file
echo "ANTHROPIC_API_KEY=sk-ant-your-key-here" > .env

# Or for OpenAI
echo "OPENAI_API_KEY=sk-proj-your-key-here" > .env
```

**Done!** Your agent can now use AI.

---

## 🎮 Running Your Agent

### Basic Run:
```bash
cd output/my-first-agent
python agent.py example.com
```

### With Docker:
```bash
cd output/my-first-agent
docker build -t my-agent .
docker run my-agent example.com
```

---

## 🎁 Use Pre-Made Templates

**Too many questions? Use our templates!**

### Reconnaissance Agent (Bug Bounty):
```bash
python generator.py --config configs/reconnaissance-agent.yaml
```

### Vulnerability Scanner:
```bash
python generator.py --config configs/vulnerability-scanner.yaml
```

### Security Monitor:
```bash
python generator.py --config configs/monitoring-agent.yaml
```

### Red Team Simulator:
```bash
python generator.py --config configs/red-team-agent.yaml
```

**That's it!** No questions asked. Agent created instantly.

---

## 🆘 Common Problems & Fixes

### "python: command not found"
**Try:** `python3` instead of `python`

### "pip: command not found"
**Try:** `python -m pip install -r requirements.txt`

### "Permission denied"
**Try:** `sudo pip install -r requirements.txt` (Mac/Linux)
**Or:** Run as Administrator (Windows)

### "Module not found"
**Fix:**
```bash
pip install pyyaml requests python-dotenv
```

### Agent runs but does nothing
**Check:** Did you create the `.env` file with your API key?
```bash
cat .env  # Should show your API key
```

---

## 📚 Want More Details?

**Super detailed guides:**
- [QUICK_START.md](docs/QUICK_START.md) - Full installation guide
- [questionnaire-guide.md](docs/questionnaire-guide.md) - What each question means
- [COMPLETE_ANSWERS.md](docs/COMPLETE_ANSWERS.md) - All possible answers
- [API_KEYS_SETUP.md](docs/API_KEYS_SETUP.md) - API key help

---

## 🎯 What Can You Make?

### 🔍 Reconnaissance Agents
- Find subdomains
- Scan ports
- Collect OSINT data
- Map attack surfaces

### 🛡️ Vulnerability Scanners
- Check for security issues
- Scan web applications
- Find misconfigurations
- Test APIs

### 📊 Security Monitors
- Watch logs in real-time
- Detect threats
- Alert on suspicious activity
- Analyze patterns

### 🎯 Red Team Tools
- Test defenses
- Simulate attacks
- Find weaknesses
- Generate reports

---

## 💡 Examples

### Example 1: Simple Port Scanner
```bash
# Generate agent
python generator.py --interactive

# Answers:
# Name: simple-scanner
# Type: Reconnaissance
# Framework: Custom Python
# LLM: None
# Output: JSON

# Use it
cd output/simple-scanner
python agent.py 192.168.1.1
```

### Example 2: AI-Powered Vulnerability Scanner
```bash
# Use template
python generator.py --config configs/vulnerability-scanner.yaml

# Add API key
cd output/vuln-scanner-pro
echo "ANTHROPIC_API_KEY=sk-ant-your-key" > .env

# Run scan
python agent.py https://example.com
```

### Example 3: Docker Deployment
```bash
# Generate agent
python generator.py --config configs/reconnaissance-agent.yaml

# Build Docker image
cd output/recon-master
docker build -t recon-agent .

# Run anywhere
docker run recon-agent example.com
```

---

## 🤝 Need Help?

1. **Read the guides:** Check the `docs/` folder
2. **Check examples:** Look in `examples/` and `configs/`
3. **Open an issue:** https://github.com/eBruno-Sec/ai-agent-generator/issues
4. **Read FAQs:** See below ⬇️

---

## ❓ Frequently Asked Questions

### Q: Do I need to know how to code?
**A:** No! Just answer questions.

### Q: Is it free?
**A:** Yes! MIT License. Use it anywhere.

### Q: Do I need an API key?
**A:** Only if you want AI features (Anthropic/OpenAI). Otherwise, no.

### Q: What's the easiest option?
**A:** Pick "None" for LLM and "Custom Python" for framework. No API key needed!

### Q: Can I modify the generated code?
**A:** Yes! It's yours. Change anything you want.

### Q: Does it work on Windows/Mac/Linux?
**A:** Yes! Works on all operating systems.

### Q: How long does it take?
**A:** 2-3 minutes to generate. Instant if using templates.

### Q: Is it secure?
**A:** The generator is safe. Generated agents are for authorized testing only.

---

## ⚠️ Important Notice

**For authorized security testing only!**

- ✅ Test your own systems
- ✅ Test with permission
- ✅ Use for learning
- ❌ Don't hack others
- ❌ No unauthorized testing
- ❌ Know the law

**Unauthorized access is illegal everywhere.**

---

## 🎓 Learning Path

**Total Beginner:**
1. Use a template: `python generator.py --config configs/reconnaissance-agent.yaml`
2. Look at the generated code in `output/`
3. Try running it: `python agent.py --help`

**Some Experience:**
1. Run interactive mode: `python generator.py --interactive`
2. Pick "Custom Python" and "None" for LLM
3. Modify the generated code

**Advanced:**
1. Try LangChain or CrewAI frameworks
2. Add API keys for AI features
3. Deploy with Docker/Kubernetes
4. Create custom templates

---

## 🏆 Success Stories

**"I made my first security agent in 3 minutes!"** - First-time user

**"No coding background. This made it so easy."** - Beginner

**"Used the templates. Had agents running in seconds."** - Quick user

---

## 📋 Quick Command Reference

```bash
# Generate interactively
python generator.py --interactive

# Use a template
python generator.py --config configs/reconnaissance-agent.yaml

# Use example answers
python generator.py --answers examples/recon-agent-answers.json

# Run your agent
cd output/your-agent-name
python agent.py <target>

# Get help
python agent.py --help
```

---

## 🎉 That's It!

You're ready to create security agents!

**Start now:**
```bash
python generator.py --interactive
```

**Questions?** Check `docs/` or open an issue!

---

## 📞 Support

- 📖 **Documentation:** [docs/](docs/)
- 💬 **Issues:** https://github.com/eBruno-Sec/ai-agent-generator/issues
- 🤝 **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📄 License

MIT License - Use it freely! See [LICENSE](LICENSE)

---

**Made with ❤️ for the security community**

**Start creating agents now! 🚀**
