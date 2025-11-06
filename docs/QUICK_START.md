# 🚀 Quick Start Guide

## Installation

### Prerequisites

- Python 3.9 or higher
- Git
- Docker (optional, for containerized agents)

### Setup

```bash
# Clone the repository
git clone https://github.com/eBruno-Sec/ai-agent-generator.git
cd ai-agent-generator

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Method 1: Interactive Mode (Recommended)

The easiest way to get started:

```bash
python generator.py --interactive
```

This will guide you through all the questions with helpful prompts and examples.

**Example session:**

```
================================================================================
🤖 AI Security Agent Generator - Interactive Mode
================================================================================

============================================================
📋 Basic Information
============================================================

❓ Agent name?
   Example: recon-spider-v1
   > my-recon-agent

❓ Describe your agent
   > Automated reconnaissance for bug bounty hunting

❓ Version
   > 1.0.0

============================================================
📋 Agent Type & Capabilities
============================================================

❓ Primary agent type?

   Options:
   1. Reconnaissance - Information gathering and OSINT
   2. Vulnerability Assessment - Security weakness identification
   3. Exploitation Testing - Automated penetration testing
   ...

   Select (number): 1

...
```

---

### Method 2: Using a Configuration File

Create a YAML config file:

```yaml
# recon-config.yaml
agent_name: advanced-recon
agent_description: Advanced reconnaissance agent
version: 1.0.0
primary_agent_type: reconnaissance
agent_framework: hybrid_langchain_custom
architecture_pattern: single_agent
primary_targets:
  - web_applications
  - network_infrastructure
llm_provider: anthropic
report_formats:
  - json
  - html
deployment_target: docker
api_key_management: env_variables
```

Then run:

```bash
python generator.py --config recon-config.yaml
```

---

### Method 3: Using a JSON Answers File

Create a JSON file with all your answers:

```json
{
  "agent_name": "security-scanner",
  "agent_description": "Automated security scanner",
  "version": "1.0.0",
  "primary_agent_type": "vulnerability_assessment",
  "agent_framework": "custom_python",
  "architecture_pattern": "single_agent",
  "primary_targets": ["web_applications"],
  "llm_provider": "none",
  "report_formats": ["json", "html"],
  "deployment_target": "docker",
  "api_key_management": "env_variables"
}
```

Run:

```bash
python generator.py --answers answers.json
```

---

## What Gets Generated?

After generation, you'll have a complete agent directory:

```
output/my-recon-agent/
├── agent.py              # Main agent code
├── config.yaml           # Configuration
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── README.md            # Agent documentation
└── reports/             # Output directory (created on first run)
```

---

## Using Your Generated Agent

### 1. Standalone Execution

```bash
cd output/my-recon-agent

# Install dependencies
pip install -r requirements.txt

# Run the agent
python agent.py example.com
```

### 2. Docker Execution

```bash
cd output/my-recon-agent

# Build the Docker image
docker build -t my-recon-agent .

# Run the container
docker run -v $(pwd)/reports:/app/reports my-recon-agent example.com
```

### 3. With Configuration

```bash
# Edit config.yaml first, then:
python agent.py --config config.yaml example.com
```

---

## Example: Creating a Reconnaissance Agent

Let's create a complete reconnaissance agent step by step:

### Step 1: Generate the Agent

```bash
python generator.py --interactive
```

**Answer the questions:**
- Name: `bug-bounty-recon`
- Description: `Automated reconnaissance for bug bounty programs`
- Type: `Reconnaissance`
- Framework: `Hybrid: LangChain + Custom`
- Targets: `Web Applications`
- LLM: `Anthropic`
- Output: `JSON, HTML`
- Deployment: `Docker`

### Step 2: Configure Environment

```bash
cd output/bug-bounty-recon

# Create .env file
cat > .env << EOF
ANTHROPIC_API_KEY=your-api-key-here
EOF
```

### Step 3: Install and Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run on a target
python agent.py https://example.com

# Check the report
cat reports/report_*.json
```

---

## Example: Creating a Vulnerability Scanner

### Quick Setup

```bash
# Use the example config
python generator.py --config examples/vuln-scanner-config.yaml

cd output/vuln-scanner-pro

# Build Docker image
docker build -t vuln-scanner .

# Run scan
docker run -e OPENAI_API_KEY=your-key vuln-scanner https://example.com
```

---

## Common Workflows

### Workflow 1: Bug Bounty Reconnaissance

```yaml
agent_name: bug-bounty-recon
agent_type: reconnaissance
framework: hybrid_langchain_custom
capabilities:
  - subdomain_enumeration
  - port_scanning
  - web_crawling
targets: [web_applications]
llm: anthropic
output: [json, html, markdown]
deployment: docker
```

### Workflow 2: Continuous Vulnerability Scanning

```yaml
agent_name: continuous-scanner
agent_type: vulnerability_assessment
framework: custom_python
capabilities:
  - web_vulnerability_scan
  - dependency_scanning
  - ssl_tls_analysis
targets: [web_applications, api_endpoints]
llm: none
output: [json, sarif]
deployment: kubernetes
scheduling: cron (0 */6 * * *)
```

### Workflow 3: Red Team Simulation

```yaml
agent_name: red-team-sim
agent_type: red_team_simulation
framework: crewai
architecture: multi_agent_sequential
capabilities:
  - attack_path_planning
  - privilege_escalation
  - lateral_movement
targets: [network_infrastructure]
llm: openai
output: [json, pdf]
deployment: docker_compose
```

---

## Troubleshooting

### Issue: Import errors

```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Issue: Docker build fails

```bash
# Check Docker is running
docker ps

# Try building with no cache
docker build --no-cache -t my-agent .
```

### Issue: Agent runs but no output

```bash
# Check the reports directory
ls -la reports/

# Run with verbose logging
python agent.py --verbose example.com

# Check logs
tail -f agent.log
```

### Issue: LLM API errors

```bash
# Verify API key is set
echo $ANTHROPIC_API_KEY

# Check .env file
cat .env

# Test API connectivity
python -c "import os; from anthropic import Anthropic; client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY')); print('Connection OK')"
```

---

## Next Steps

1. **Customize your agent** - Edit the generated code to add specific features
2. **Add more tools** - Integrate additional security tools
3. **Configure scheduling** - Set up automated runs
4. **Integrate with CI/CD** - Add to your pipeline
5. **Share your templates** - Contribute back to the project!

---

## Advanced Usage

### Custom Templates

Create your own agent templates:

```bash
mkdir -p templates/agents/my_custom_agent
# Add your template files
```

### Extending the Generator

Add custom question sections:

```python
# In generator.py
def _ask_custom_questions(self):
    # Your custom logic
    pass
```

### Integration with MCP Server

```bash
# Use with Docker MCP server
docker run -v $(pwd):/workspace mcp-server python generator.py --interactive
```

---

## Resources

- [Complete Questionnaire Guide](docs/questionnaire-guide.md)
- [Agent Type Comparison](docs/agent-types.md)
- [Framework Selection Guide](docs/frameworks.md)
- [Example Configurations](examples/)
- [GitHub Issues](https://github.com/eBruno-Sec/ai-agent-generator/issues)

---

## Need Help?

- 📖 Check the [Documentation](docs/)
- 💬 Open an [Issue](https://github.com/eBruno-Sec/ai-agent-generator/issues)
- 🤝 See [Contributing](CONTRIBUTING.md)

---

**Happy Agent Building! 🚀**
