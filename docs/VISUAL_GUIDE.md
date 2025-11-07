# 🎨 VISUAL STEP-BY-STEP GUIDE

**Never done this before? Perfect! Follow along exactly.**

---

## 📦 STEP 1: GET THE CODE

### Windows:
1. Press `Windows Key + R`
2. Type `cmd` and press Enter
3. Copy and paste this (right-click to paste in Command Prompt):
```
git clone https://github.com/eBruno-Sec/ai-agent-generator.git
cd ai-agent-generator
```

### Mac:
1. Press `Command + Space`
2. Type `terminal` and press Enter
3. Copy and paste this:
```bash
git clone https://github.com/eBruno-Sec/ai-agent-generator.git
cd ai-agent-generator
```

### Linux:
1. Open Terminal (usually `Ctrl + Alt + T`)
2. Copy and paste this:
```bash
git clone https://github.com/eBruno-Sec/ai-agent-generator.git
cd ai-agent-generator
```

### Don't have Git?
1. Go to https://github.com/eBruno-Sec/ai-agent-generator
2. Click green **"Code"** button
3. Click **"Download ZIP"**
4. Unzip the file
5. Open Terminal/Command Prompt
6. Type `cd ` (with space)
7. Drag the folder into the terminal
8. Press Enter

**✅ You should see your prompt change to show you're in the folder**

---

## 🔧 STEP 2: INSTALL STUFF

Copy and paste this:

```bash
pip install -r requirements.txt
```

**What you'll see:**
```
Collecting pyyaml>=6.0
Downloading pyyaml-6.0.1...
Installing collected packages: pyyaml, requests...
Successfully installed pyyaml-6.0 requests-2.31.0...
```

**If you see "pip: command not found"** try this instead:
```bash
python -m pip install -r requirements.txt
```

**✅ Wait until you see "Successfully installed"**

---

## 🚀 STEP 3: RUN THE GENERATOR

Copy and paste this:

```bash
python generator.py --interactive
```

**If that doesn't work, try:**
```bash
python3 generator.py --interactive
```

**✅ You should see:**
```
================================================================================
🤖 AI Security Agent Generator - Interactive Mode
================================================================================
```

---

## 💬 STEP 4: ANSWER THE QUESTIONS

**The generator will ask questions. Here's a simple example:**

### Question 1: Agent name?
```
❓ What is the name of your agent?
   Example: recon-spider-v1
   > 
```
**Type something simple like:** `my-test-agent`
**Press Enter**

---

### Question 2: Describe your agent
```
❓ Describe what your agent does
   > 
```
**Type:** `My first security agent for testing`
**Press Enter**

---

### Question 3: Version
```
❓ Version number
   > 
```
**Just press Enter** (it uses 1.0.0 automatically)

---

### Question 4: Agent type
```
❓ What is the primary type of your agent?

   Options:
   1. Reconnaissance - Information gathering and OSINT
   2. Vulnerability Assessment - Security weakness identification
   3. Exploitation Testing - Automated penetration testing
   4. Security Monitoring - Real-time threat detection
   5. Red Team Simulation - Adversary emulation
   6. Security Analysis - Code/artifact/malware analysis
   7. Incident Response - Automated IR workflows
   8. Compliance Audit - Security policy compliance

   Select (number): 
```
**Type:** `1` (for Reconnaissance)
**Press Enter**

---

### Question 5: Framework
```
❓ Which framework should your agent use?

   Options:
   1. Custom Python - Pure Python (most flexible, no framework overhead)
   2. LangChain - Best for LLM reasoning + tools
   3. CrewAI - Multi-agent orchestration
   4. AutoGen - Microsoft AutoGen (code execution + multi-agent)
   5. Hybrid: LangChain + Custom - LangChain for reasoning, custom for tools

   Select (number): 
```
**Type:** `1` (Custom Python - simplest option)
**Press Enter**

---

### Question 6: Architecture
```
❓ What architecture pattern should your agent use?

   Options:
   1. Single Agent - One autonomous agent
   2. Multi-Agent Parallel - Multiple agents running in parallel
   3. Multi-Agent Sequential - Agents in sequence (pipeline)

   Select (number): 
```
**Type:** `1` (Single Agent - simplest)
**Press Enter**

---

### Question 7: Target environments
```
❓ What are the primary target environments?

   Options (comma-separated numbers):
   1. Web Applications
   2. Network Infrastructure
   3. Cloud Environments
   4. API Endpoints

   Select (e.g., 1,3,5): 
```
**Type:** `1` (just web applications)
**Press Enter**

---

### Question 8: LLM Provider
```
❓ LLM Provider?

   Options:
   1. OpenAI - OpenAI (GPT-4, GPT-3.5)
   2. Anthropic - Anthropic (Claude)
   3. Azure OpenAI - Azure OpenAI
   4. Google - Google (Gemini)
   5. Local Ollama - Local Ollama models
   6. None - No LLM (rule-based only)

   Select (number): 
```
**Type:** `6` (None - no API key needed!)
**Press Enter**

---

### Question 9: Report formats
```
❓ Report formats?

   Options (comma-separated numbers):
   1. JSON
   2. HTML
   3. PDF
   4. Markdown

   Select (e.g., 1,2): 
```
**Type:** `1,2` (JSON and HTML)
**Press Enter**

---

### Question 10: Deployment
```
❓ Deployment?

   Options:
   1. Docker
   2. Kubernetes
   3. Standalone Python
   4. Docker Compose

   Select (number): 
```
**Type:** `3` (Standalone - easiest)
**Press Enter**

---

### Question 11: API key management
```
❓ API key management?

   Options:
   1. Environment Variables
   2. Docker Secrets
   3. Kubernetes Secrets
   4. HashiCorp Vault

   Select (number): 
```
**Type:** `1` (Environment Variables)
**Press Enter**

---

## ✨ STEP 5: DONE!

**You'll see:**
```
🔨 Generating agent: my-test-agent
   Type: reconnaissance
   Framework: custom_python
   Output: output/my-test-agent

   ✓ Generated: agent.py
   ✓ Generated: config.yaml
   ✓ Generated: requirements.txt
   ✓ Generated: README.md

✅ Agent generated successfully!

📂 Location: output/my-test-agent

🚀 Next steps:
   1. cd output/my-test-agent
   2. pip install -r requirements.txt
   3. python agent.py --help
```

**✅ Your agent is ready!**

---

## 🎮 STEP 6: RUN YOUR AGENT

```bash
cd output/my-test-agent
pip install -r requirements.txt
python agent.py --help
```

**You'll see:**
```
usage: agent.py [-h] [--config CONFIG] target

Security Agent

positional arguments:
  target                Target to scan

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Config file
```

**Try it:**
```bash
python agent.py example.com
```

**✅ Your agent runs and creates a report!**

---

## 🎁 EVEN EASIER: USE A TEMPLATE

**Don't want to answer questions? Use a ready-made template:**

```bash
python generator.py --config configs/reconnaissance-agent.yaml
```

**That's it! No questions. Instant agent.**

**Available templates:**
- `configs/reconnaissance-agent.yaml` - Bug bounty recon
- `configs/vulnerability-scanner.yaml` - Vuln scanner
- `configs/monitoring-agent.yaml` - Security monitor
- `configs/red-team-agent.yaml` - Red team simulator

---

## 🆘 HELP! SOMETHING WENT WRONG

### "python: command not found"
**Try:** `python3` everywhere you see `python`

### "pip: command not found"
**Try:** `python -m pip` everywhere you see `pip`

### "Permission denied"
**Mac/Linux:** Add `sudo` at the start:
```bash
sudo pip install -r requirements.txt
```

**Windows:** Run Command Prompt as Administrator

### "Module not found"
```bash
pip install pyyaml requests python-dotenv --user
```

### Still stuck?
1. Check [docs/QUICK_START.md](docs/QUICK_START.md)
2. Open an issue: https://github.com/eBruno-Sec/ai-agent-generator/issues

---

## 📸 VISUAL SUMMARY

```
┌─────────────────────────────────────────┐
│  1. Get Code                            │
│     git clone https://...               │
│     cd ai-agent-generator               │
└─────────────────────────────────────────┘
              ⬇️
┌─────────────────────────────────────────┐
│  2. Install                             │
│     pip install -r requirements.txt     │
└─────────────────────────────────────────┘
              ⬇️
┌─────────────────────────────────────────┐
│  3. Run Generator                       │
│     python generator.py --interactive   │
└─────────────────────────────────────────┘
              ⬇️
┌─────────────────────────────────────────┐
│  4. Answer Questions                    │
│     (or use template)                   │
└─────────────────────────────────────────┘
              ⬇️
┌─────────────────────────────────────────┐
│  5. Agent Created! ✅                   │
│     cd output/your-agent                │
│     python agent.py                     │
└─────────────────────────────────────────┘
```

---

## ⏱️ HOW LONG DOES THIS TAKE?

- **Get code:** 30 seconds
- **Install:** 1-2 minutes
- **Answer questions:** 2-3 minutes
- **Total:** ~5 minutes

**Using template:** ~2 minutes total

---

## 🎯 WHAT DID YOU JUST MAKE?

Your agent can:
- ✅ Scan targets
- ✅ Generate reports
- ✅ Run automatically
- ✅ Be customized
- ✅ Be deployed anywhere

**All with no coding!**

---

## 🏆 YOU DID IT!

**You just created a custom security agent!**

**Next steps:**
1. Try the templates: `python generator.py --config configs/reconnaissance-agent.yaml`
2. Read the docs: Check `docs/` folder
3. Customize: Edit the generated code
4. Share: Show others what you built!

---

## 📞 NEED MORE HELP?

- 📖 Read: [docs/QUICK_START.md](docs/QUICK_START.md)
- 📖 Read: [docs/questionnaire-guide.md](docs/questionnaire-guide.md)
- 💬 Ask: https://github.com/eBruno-Sec/ai-agent-generator/issues

---

**Remember: If you can copy-paste, you can do this! 🚀**
