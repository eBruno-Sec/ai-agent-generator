#!/usr/bin/env python3
"""
AI Security Agent Generator
Main generator script for creating customized security agents
"""

import json
import os
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, List
import yaml

class AgentGenerator:
    """Main generator class for creating security agents"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.templates_dir = self.base_dir / "templates"
        self.output_dir = self.base_dir / "output"
        self.questionnaire_file = self.base_dir / "questionnaire" / "questions.json"
        
    def load_questionnaire(self) -> Dict[str, Any]:
        """Load the questionnaire definition"""
        with open(self.questionnaire_file, 'r') as f:
            return json.load(f)
    
    def interactive_mode(self) -> Dict[str, Any]:
        """Run interactive questionnaire"""
        questionnaire = self.load_questionnaire()
        answers = {}
        
        print("\n" + "="*80)
        print("🤖 AI Security Agent Generator - Interactive Mode")
        print("="*80 + "\n")
        
        for section in questionnaire['sections']:
            print(f"\n{'='*60}")
            print(f"📋 {section['name']}")
            print(f"{'='*60}\n")
            
            for question in section['questions']:
                answer = self._ask_question(question)
                answers[question['id']] = answer
        
        return answers
    
    def _ask_question(self, question: Dict[str, Any]) -> Any:
        """Ask a single question and get answer"""
        print(f"\n❓ {question['question']}")
        
        if question.get('description'):
            print(f"   ℹ️  {question['description']}")
        
        if question['type'] == 'text' or question['type'] == 'textarea':
            if question.get('example'):
                print(f"   Example: {question['example']}")
            answer = input("   > ").strip()
            
            if not answer and question.get('default'):
                answer = question['default']
                print(f"   Using default: {answer}")
            
            return answer
        
        elif question['type'] == 'single_choice':
            print("\n   Options:")
            for idx, option in enumerate(question['options'], 1):
                label = option['label']
                desc = option.get('description', '')
                print(f"   {idx}. {label}" + (f" - {desc}" if desc else ""))
            
            while True:
                try:
                    choice = input("\n   Select (number): ").strip()
                    choice_idx = int(choice) - 1
                    if 0 <= choice_idx < len(question['options']):
                        return question['options'][choice_idx]['value']
                    print("   ❌ Invalid selection. Try again.")
                except ValueError:
                    print("   ❌ Please enter a number.")
        
        elif question['type'] == 'multi_choice':
            print("\n   Options (comma-separated numbers):")
            for idx, option in enumerate(question['options'], 1):
                print(f"   {idx}. {option['label']}")
            
            choice = input("\n   Select (e.g., 1,3,5): ").strip()
            if not choice:
                return []
            
            try:
                indices = [int(x.strip()) - 1 for x in choice.split(',')]
                return [question['options'][i]['value'] for i in indices if 0 <= i < len(question['options'])]
            except:
                print("   ❌ Invalid input. Skipping.")
                return []
    
    def generate_agent(self, answers: Dict[str, Any]) -> Path:
        """Generate the agent based on answers"""
        agent_name = answers.get('agent_name', 'security-agent')
        agent_type = answers.get('primary_agent_type', 'reconnaissance')
        framework = answers.get('agent_framework', 'custom_python')
        
        # Create output directory
        agent_dir = self.output_dir / agent_name
        agent_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n🔨 Generating agent: {agent_name}")
        print(f"   Type: {agent_type}")
        print(f"   Framework: {framework}")
        print(f"   Output: {agent_dir}")
        
        # Generate files
        self._generate_main_script(agent_dir, answers)
        self._generate_config(agent_dir, answers)
        self._generate_requirements(agent_dir, answers)
        self._generate_dockerfile(agent_dir, answers)
        self._generate_readme(agent_dir, answers)
        
        print("\n✅ Agent generated successfully!")
        print(f"\n📂 Location: {agent_dir}")
        print("\n🚀 Next steps:")
        print(f"   1. cd {agent_dir}")
        print("   2. pip install -r requirements.txt")
        print("   3. python agent.py --help")
        
        return agent_dir
    
    def _generate_main_script(self, agent_dir: Path, answers: Dict[str, Any]):
        """Generate the main agent script"""
        agent_type = answers.get('primary_agent_type', 'reconnaissance')
        framework = answers.get('agent_framework', 'custom_python')
        
        if framework == 'custom_python':
            template = self._get_custom_python_template(agent_type)
        elif framework == 'langchain':
            template = self._get_langchain_template(agent_type)
        elif framework == 'crewai':
            template = self._get_crewai_template(agent_type)
        else:
            template = self._get_custom_python_template(agent_type)
        
        script_path = agent_dir / "agent.py"
        with open(script_path, 'w') as f:
            f.write(template)
        
        # Make executable
        os.chmod(script_path, 0o755)
        print(f"   ✓ Generated: agent.py")
    
    def _get_custom_python_template(self, agent_type: str) -> str:
        """Get custom Python template for agent type"""
        base_template = '''#!/usr/bin/env python3
"""
Security Agent - {agent_type}
Generated by AI Security Agent Generator
"""

import argparse
import json
import logging
from datetime import datetime
from pathlib import Path

class SecurityAgent:
    """Main agent class"""
    
    def __init__(self, config_file: str = "config.yaml"):
        self.config = self._load_config(config_file)
        self._setup_logging()
        
    def _load_config(self, config_file: str):
        """Load configuration"""
        import yaml
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    
    def _setup_logging(self):
        """Setup logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def run(self, target: str):
        """Main execution method"""
        self.logger.info(f"Starting security agent on target: {{target}}")
        
        results = {{
            "timestamp": datetime.now().isoformat(),
            "target": target,
            "agent_type": "{agent_type}",
            "findings": []
        }}
        
        # Execute agent logic
        findings = self._execute_scan(target)
        results["findings"] = findings
        
        # Generate report
        self._generate_report(results)
        
        return results
    
    def _execute_scan(self, target: str):
        """Execute the security scan"""
        findings = []
        
        # Add your scan logic here
        self.logger.info(f"Scanning {{target}}...")
        
        # Example finding
        findings.append({{
            "severity": "info",
            "title": "Scan completed",
            "description": f"Successfully scanned {{target}}"
        }})
        
        return findings
    
    def _generate_report(self, results):
        """Generate report from results"""
        output_dir = Path("reports")
        output_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = output_dir / f"report_{{timestamp}}.json"
        
        with open(report_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        self.logger.info(f"Report saved to: {{report_file}}")

def main():
    parser = argparse.ArgumentParser(description="Security Agent")
    parser.add_argument("target", help="Target to scan")
    parser.add_argument("--config", default="config.yaml", help="Config file")
    
    args = parser.parse_args()
    
    agent = SecurityAgent(config_file=args.config)
    agent.run(args.target)

if __name__ == "__main__":
    main()
'''
        return base_template.format(agent_type=agent_type)
    
    def _get_langchain_template(self, agent_type: str) -> str:
        """Get LangChain template"""
        return '''#!/usr/bin/env python3
"""
LangChain Security Agent
"""

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

class LangChainSecurityAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.3,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.tools = self._setup_tools()
        self.agent = self._create_agent()
    
    def _setup_tools(self):
        """Setup agent tools"""
        tools = [
            Tool(
                name="scan_ports",
                func=self._scan_ports,
                description="Scan ports on a target"
            )
        ]
        return tools
    
    def _scan_ports(self, target: str) -> str:
        """Example port scanning tool"""
        return f"Scanned ports on {target}"
    
    def _create_agent(self):
        """Create LangChain agent"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a security testing agent."),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        agent = create_openai_functions_agent(self.llm, self.tools, prompt)
        return AgentExecutor(agent=agent, tools=self.tools, verbose=True)
    
    def run(self, task: str):
        """Execute agent task"""
        return self.agent.invoke({"input": task})

if __name__ == "__main__":
    agent = LangChainSecurityAgent()
    result = agent.run("Scan example.com for vulnerabilities")
    print(result)
'''
    
    def _get_crewai_template(self, agent_type: str) -> str:
        """Get CrewAI template"""
        return '''#!/usr/bin/env python3
"""
CrewAI Multi-Agent Security System
"""

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

class SecurityCrew:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.3,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.agents = self._create_agents()
        self.crew = self._create_crew()
    
    def _create_agents(self):
        """Create specialized agents"""
        recon_agent = Agent(
            role="Reconnaissance Specialist",
            goal="Gather information about targets",
            backstory="Expert in OSINT and reconnaissance",
            llm=self.llm
        )
        
        analysis_agent = Agent(
            role="Security Analyst",
            goal="Analyze findings and identify vulnerabilities",
            backstory="Expert in vulnerability analysis",
            llm=self.llm
        )
        
        return [recon_agent, analysis_agent]
    
    def _create_crew(self):
        """Create the crew"""
        return Crew(
            agents=self.agents,
            verbose=True
        )
    
    def run(self, target: str):
        """Execute security assessment"""
        task = Task(
            description=f"Perform security assessment on {target}",
            agent=self.agents[0]
        )
        
        return self.crew.kickoff(tasks=[task])

if __name__ == "__main__":
    crew = SecurityCrew()
    result = crew.run("example.com")
    print(result)
'''
    
    def _generate_config(self, agent_dir: Path, answers: Dict[str, Any]):
        """Generate configuration file"""
        config = {
            "agent": {
                "name": answers.get('agent_name'),
                "type": answers.get('primary_agent_type'),
                "version": answers.get('version', '1.0.0')
            },
            "llm": {
                "provider": answers.get('llm_provider', 'none'),
                "model": "gpt-4" if answers.get('llm_provider') == 'openai' else None
            },
            "output": {
                "formats": answers.get('report_formats', ['json'])
            },
            "security": {
                "rate_limit": 10,
                "timeout": 30
            }
        }
        
        config_path = agent_dir / "config.yaml"
        with open(config_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)
        
        print(f"   ✓ Generated: config.yaml")
    
    def _generate_requirements(self, agent_dir: Path, answers: Dict[str, Any]):
        """Generate requirements.txt"""
        framework = answers.get('agent_framework', 'custom_python')
        
        base_reqs = [
            "pyyaml>=6.0",
            "requests>=2.31.0",
            "python-dotenv>=1.0.0"
        ]
        
        if framework == 'langchain' or framework == 'hybrid_langchain_custom':
            base_reqs.extend([
                "langchain>=0.1.0",
                "langchain-openai>=0.0.5",
                "openai>=1.0.0"
            ])
        elif framework == 'crewai' or framework == 'hybrid_crewai_custom':
            base_reqs.extend([
                "crewai>=0.1.0",
                "langchain>=0.1.0",
                "openai>=1.0.0"
            ])
        
        req_path = agent_dir / "requirements.txt"
        with open(req_path, 'w') as f:
            f.write('\n'.join(base_reqs))
        
        print(f"   ✓ Generated: requirements.txt")
    
    def _generate_dockerfile(self, agent_dir: Path, answers: Dict[str, Any]):
        """Generate Dockerfile"""
        if answers.get('deployment_target') not in ['docker', 'kubernetes', 'docker_compose']:
            return
        
        dockerfile_content = '''FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    nmap \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY . .

# Run agent
CMD ["python", "agent.py"]
'''
        
        dockerfile_path = agent_dir / "Dockerfile"
        with open(dockerfile_path, 'w') as f:
            f.write(dockerfile_content)
        
        print(f"   ✓ Generated: Dockerfile")
    
    def _generate_readme(self, agent_dir: Path, answers: Dict[str, Any]):
        """Generate README"""
        agent_name = answers.get('agent_name')
        agent_type = answers.get('primary_agent_type')
        
        readme_content = f'''# {agent_name}

**Type:** {agent_type}

Generated by AI Security Agent Generator

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run agent
python agent.py <target>
```

## Configuration

Edit `config.yaml` to customize agent behavior.

## Docker

```bash
docker build -t {agent_name} .
docker run {agent_name}
```

## License

MIT
'''
        
        readme_path = agent_dir / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        print(f"   ✓ Generated: README.md")

def main():
    parser = argparse.ArgumentParser(description="AI Security Agent Generator")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("--config", help="Load config file")
    parser.add_argument("--answers", help="Load answers JSON")
    
    args = parser.parse_args()
    
    generator = AgentGenerator()
    
    if args.interactive or (not args.config and not args.answers):
        answers = generator.interactive_mode()
    elif args.answers:
        with open(args.answers, 'r') as f:
            answers = json.load(f)
    elif args.config:
        with open(args.config, 'r') as f:
            answers = yaml.safe_load(f)
    
    generator.generate_agent(answers)

if __name__ == "__main__":
    main()
