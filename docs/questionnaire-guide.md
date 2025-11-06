# 📚 Complete Questionnaire Guide

## Overview

This guide explains every question in the AI Security Agent Generator questionnaire to help you create the perfect agent for your needs.

---

## Section 1: Basic Information

### Q: Agent name?
**Type:** Text  
**Required:** Yes  
**Format:** lowercase, numbers, and hyphens only  
**Example:** `recon-spider-v1`, `vuln-scanner-pro`

Choose a descriptive name that indicates:
- What the agent does
- Version number (optional)
- Your naming convention

**Tips:**
- Keep it short and memorable
- Use semantic versioning (v1, v2, etc.)
- Avoid spaces and special characters

---

### Q: Describe your agent
**Type:** Textarea  
**Required:** Yes  
**Length:** 10-500 characters

Write a brief description explaining:
- Primary purpose
- Key capabilities
- Target use case

**Example:**
```
Automated reconnaissance agent for subdomain enumeration and port 
scanning with intelligent threat intelligence correlation
```

---

### Q: Version
**Type:** Text  
**Default:** 1.0.0  
**Format:** Semantic versioning (MAJOR.MINOR.PATCH)

**Guidelines:**
- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes

---

## Section 2: Agent Type & Capabilities

### Q: Primary agent type?
**Type:** Single choice  
**Required:** Yes

#### **Reconnaissance**
Information gathering and OSINT

**Best for:**
- Subdomain discovery
- Port scanning
- DNS enumeration
- OSINT collection
- Certificate transparency monitoring

**Use cases:**
- Bug bounty reconnaissance
- Red team intelligence gathering
- Asset discovery
- Attack surface mapping

---

#### **Vulnerability Assessment**
Security weakness identification

**Best for:**
- CVE matching
- Configuration auditing
- Dependency scanning
- Web vulnerability detection
- Cloud security audits

**Use cases:**
- Continuous vulnerability management
- Compliance scanning
- Pre-deployment security checks
- Patch management prioritization

---

#### **Exploitation Testing**
Automated penetration testing

**Best for:**
- Payload generation
- Exploit chain orchestration
- Credential testing
- Privilege escalation testing
- Lateral movement simulation

**Use cases:**
- Penetration testing automation
- Security validation
- Red team exercises
- Security training

---

#### **Security Monitoring**
Real-time threat detection

**Best for:**
- Log analysis
- Anomaly detection
- Threat hunting
- Alert triage
- Behavioral analysis

**Use cases:**
- SOC automation
- Incident detection
- Threat intelligence correlation
- Real-time alerting

---

#### **Red Team Simulation**
Adversary emulation

**Best for:**
- Attack path planning
- C2 simulation
- Defense evasion
- Data exfiltration testing
- Malware simulation

**Use cases:**
- Purple team exercises
- Defense validation
- Security awareness training
- Adversary tactics testing

---

#### **Security Analysis**
Code/artifact/malware analysis

**Best for:**
- Malware analysis
- Code security review
- Binary analysis
- Network forensics
- Threat report generation

**Use cases:**
- Malware research
- Code auditing
- Incident investigation
- Threat intelligence production

---

#### **Incident Response**
Automated IR workflows

**Best for:**
- Automated containment
- Evidence collection
- Playbook execution
- Threat remediation

**Use cases:**
- Incident response automation
- Forensics collection
- Breach containment
- Recovery automation

---

#### **Compliance Audit**
Security policy compliance checking

**Best for:**
- PCI DSS auditing
- HIPAA compliance
- GDPR assessment
- CIS benchmarking
- NIST framework validation

**Use cases:**
- Regulatory compliance
- Audit preparation
- Policy enforcement
- Control validation

---

## Section 3: Framework & Architecture

### Q: Framework?
**Type:** Single choice  
**Required:** Yes

#### **Custom Python**
Pure Python implementation

**Pros:**
- Maximum flexibility
- No framework overhead
- Full control over security operations
- Lightweight and fast

**Cons:**
- More code to write
- No built-in LLM integration
- Manual tool orchestration

**Best for:**
- Performance-critical agents
- Simple workflows
- Direct tool integration
- When you don't need LLM reasoning

---

#### **LangChain**
LangChain framework

**Pros:**
- Excellent tool integration
- Built-in memory management
- Strong LLM support
- Large community

**Cons:**
- Framework overhead
- Can be complex for simple tasks
- Additional dependencies

**Best for:**
- Agents needing LLM reasoning
- Complex decision-making
- Multi-tool orchestration
- Agents with memory requirements

---

#### **CrewAI**
Multi-agent orchestration

**Pros:**
- Role-based agent design
- Hierarchical task management
- Multi-agent collaboration
- Built for complex workflows

**Cons:**
- Requires multiple LLM calls
- Higher resource usage
- More complex setup

**Best for:**
- Complex multi-stage attacks
- Red team simulations
- Collaborative agent systems
- Workflow orchestration

---

#### **Hybrid: LangChain + Custom** ⭐ Recommended
Combines LangChain reasoning with custom tools

**Pros:**
- Best of both worlds
- LLM for decisions, custom for execution
- Flexible architecture
- Performance optimized

**Best for:**
- Most security agents
- Production deployments
- Balanced approach

---

### Q: Architecture?
**Type:** Single choice  
**Required:** Yes

#### **Single Agent**
One autonomous agent

**Best for:**
- Simple workflows
- Focused tasks
- Quick execution
- Low resource usage

---

#### **Multi-Agent Parallel**
Multiple agents running simultaneously

**Best for:**
- Scanning multiple targets
- Distributed scanning
- Fast execution
- Independent tasks

---

#### **Multi-Agent Sequential**
Agents in sequence (pipeline)

**Best for:**
- Recon → Scan → Exploit workflows
- Data pipeline processing
- Stage-by-stage execution
- Complex multi-step operations

---

## Section 4: Target Environment

### Q: Target environments?
**Type:** Multi-choice  
**Required:** Yes  
**Multiple selections allowed**

#### Options:
- **Web Applications** - Web apps, websites, web APIs
- **Network Infrastructure** - Routers, switches, firewalls, servers
- **Cloud Environments** - AWS, Azure, GCP resources
- **API Endpoints** - REST, GraphQL, SOAP APIs

**Select all that apply to your use case**

---

## Section 5: LLM Configuration

### Q: LLM Provider?
**Type:** Single choice  
**Required:** Yes

#### **OpenAI**
GPT-4, GPT-3.5

**Pros:**
- Most capable
- Best tool use
- Strong reasoning

**Cons:**
- Expensive
- Cloud-based (privacy)
- API key required

**Best for:** Production agents needing advanced reasoning

---

#### **Anthropic** ⭐ Recommended
Claude Sonnet, Opus

**Pros:**
- Excellent for security tasks
- Strong analysis capabilities
- Better safety guardrails

**Cons:**
- API key required
- Cloud-based

**Best for:** Security analysis, compliance, complex reasoning

---

#### **Local Ollama**
Local LLM models

**Pros:**
- No API costs
- Full privacy
- Offline capable

**Cons:**
- Slower inference
- Less capable
- Requires local GPU

**Best for:** Privacy-sensitive tasks, offline operations

---

#### **None (Rule-based)**
No LLM, pure automation

**Pros:**
- Fastest execution
- No API costs
- Fully deterministic

**Cons:**
- No reasoning
- No adaptation
- Rigid workflows

**Best for:** Simple scanning, known workflows, performance-critical

---

## Section 6: Output & Reporting

### Q: Report formats?
**Type:** Multi-choice  
**Required:** Yes

#### Options:
- **JSON** - Structured data, API-friendly, automation
- **HTML** - Rich reports, dashboards, human-readable
- **PDF** - Professional reports, deliverables, clients
- **Markdown** - Documentation, GitHub, simple formatting

**Recommendation:** Select JSON + HTML for most use cases

---

## Section 7: Deployment

### Q: Deployment?
**Type:** Single choice  
**Required:** Yes

#### **Docker** ⭐ Recommended
Single container

**Pros:**
- Isolated environment
- Easy distribution
- Consistent execution

**Best for:** Most deployments

---

#### **Kubernetes**
K8s orchestration

**Pros:**
- Scalable
- Production-grade
- Auto-scaling
- High availability

**Best for:** Enterprise deployments, continuous scanning

---

#### **Standalone Python**
Direct Python execution

**Pros:**
- Simple setup
- No containers
- Direct execution

**Best for:** Development, testing, simple scripts

---

#### **Docker Compose**
Multi-container orchestration

**Pros:**
- Multiple services
- Database integration
- Easy local development

**Best for:** Complex agents, microservices

---

## Section 8: Security & Compliance

### Q: API key management?
**Type:** Single choice  
**Required:** Yes

#### **Environment Variables** ⭐ Recommended for development
Simple .env file

**Pros:**
- Easy setup
- Standard approach
- Works everywhere

**Cons:**
- Less secure
- Manual rotation

**Best for:** Development, testing

---

#### **Docker Secrets**
Docker swarm secrets

**Pros:**
- Encrypted storage
- Automatic injection
- Docker-native

**Best for:** Docker deployments

---

#### **Kubernetes Secrets**
K8s secret management

**Pros:**
- K8s-native
- Role-based access
- Encrypted at rest

**Best for:** Kubernetes deployments

---

#### **HashiCorp Vault**
Enterprise secret management

**Pros:**
- Centralized management
- Dynamic secrets
- Audit logging
- Auto-rotation

**Cons:**
- Complex setup
- Additional infrastructure

**Best for:** Enterprise, production, compliance requirements

---

## Quick Selection Guide

### 🔍 I want to build a **Reconnaissance Agent**

```yaml
Agent Type: reconnaissance
Framework: custom_python or hybrid_langchain_custom
Architecture: single_agent
Targets: web_applications, network_infrastructure
LLM: none or anthropic
Output: json, html
Deployment: docker
Secrets: env_variables
```

---

### 🛡️ I want to build a **Vulnerability Scanner**

```yaml
Agent Type: vulnerability_assessment
Framework: hybrid_langchain_custom
Architecture: single_agent
Targets: web_applications, cloud_environments
LLM: anthropic
Output: json, pdf, html
Deployment: docker
Secrets: docker_secrets
```

---

### 🎯 I want to build a **Red Team Agent**

```yaml
Agent Type: red_team_simulation
Framework: crewai
Architecture: multi_agent_sequential
Targets: network_infrastructure, web_applications
LLM: anthropic or openai
Output: json, html, markdown
Deployment: docker_compose
Secrets: vault
```

---

### 📊 I want to build a **Monitoring Agent**

```yaml
Agent Type: security_monitoring
Framework: hybrid_langchain_custom
Architecture: single_agent
Targets: network_infrastructure
LLM: anthropic
Output: json, html
Deployment: kubernetes
Secrets: kubernetes_secrets
```

---

## Need Help?

- Check [examples/](../examples/) for pre-configured answers
- See generated agents in [output/](../output/)
- Open an issue on GitHub for questions

---

**Next:** Run `python generator.py --interactive` to start!
