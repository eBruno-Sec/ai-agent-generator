# Contributing to AI Security Agent Generator

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

- Check existing issues before creating a new one
- Provide detailed information:
  - Agent type and configuration
  - Steps to reproduce
  - Expected vs actual behavior
  - Error messages and logs
  - Environment details (OS, Python version, etc.)

### Suggesting Features

- Open an issue with the "enhancement" label
- Describe the use case and expected behavior
- Explain why this feature would be valuable

### Adding New Agent Templates

1. Fork the repository
2. Create a new branch: `git checkout -b feature/new-agent-template`
3. Add your template in `templates/agents/[agent_type]/`
4. Include:
   - Python template with docstrings
   - Example configuration
   - Documentation
5. Test your template
6. Submit a pull request

### Adding Tool Integrations

1. Add tool wrapper in `templates/tools/`
2. Update questionnaire in `questionnaire/questions.json`
3. Add documentation
4. Test integration
5. Submit PR

### Improving Documentation

- Fix typos and clarify unclear sections
- Add examples and use cases
- Improve code comments
- Update guides in `docs/`

## Code Standards

### Python

- Follow PEP 8 style guide
- Use type hints where applicable
- Add docstrings to functions and classes
- Keep functions focused and modular
- Handle errors gracefully

### Security

- Never commit API keys or secrets
- Use environment variables for sensitive data
- Validate all user inputs
- Follow security best practices
- Test for common vulnerabilities

### Testing

- Add tests for new features
- Ensure existing tests pass
- Test on multiple platforms if possible

## Pull Request Process

1. **Fork** the repository
2. **Create a branch** for your changes
3. **Commit** with clear, descriptive messages
4. **Test** your changes thoroughly
5. **Document** new features or changes
6. **Submit** a pull request with:
   - Clear description of changes
   - Related issue numbers
   - Testing performed
   - Screenshots (if UI changes)

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/ai-agent-generator.git
cd ai-agent-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available

# Run tests
python -m pytest tests/
```

## Code Review

All submissions require review. We'll:
- Review code quality and style
- Test functionality
- Check documentation
- Verify security practices
- Provide constructive feedback

## Community

- Be respectful and professional
- Welcome newcomers
- Provide constructive feedback
- Focus on the issue, not the person
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)

## Questions?

Feel free to:
- Open an issue for discussion
- Ask questions in pull requests
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🙏**
