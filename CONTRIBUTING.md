# Contributing to Agent Demo

Thank you for your interest in contributing to Agent Demo! This document provides guidelines and instructions for contributing.

## Getting Started

### Development Setup

1. Fork and clone the repository:
```bash
git clone https://github.com/your-username/agent_demo.git
cd agent_demo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

4. Set up your environment:
```bash
cp .env.example .env
# Add your OPENAI_API_KEY to .env
```

## Project Structure

```
agent_demo/
├── src/agent_demo/        # Main package
│   ├── agents/            # Agent implementations
│   ├── tools/             # Tool implementations
│   └── examples/          # Usage examples
├── tests/                 # Unit tests (to be added)
├── requirements.txt       # Dependencies
└── setup.py              # Package setup
```

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and package versions
- Error messages or logs

### Suggesting Features

For feature requests, please create an issue describing:
- The use case and problem it solves
- Proposed solution or API
- Examples of how it would be used
- Any alternative solutions considered

### Contributing Code

1. **Create an issue** first to discuss the change
2. **Fork the repository** and create a branch
3. **Make your changes** following the guidelines below
4. **Test your changes** thoroughly
5. **Submit a pull request**

## Coding Guidelines

### Python Style

- Follow PEP 8 style guide
- Use type hints for function parameters and returns
- Write docstrings for all public functions and classes
- Use clear, descriptive variable names

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """Short description of the function.
    
    Longer description if needed, explaining the purpose,
    behavior, and any important details.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When and why this is raised
    """
    pass
```

### Creating Tools

When adding new tools:

1. Create a new file in `src/agent_demo/tools/`
2. Use the `@tool` decorator
3. Provide clear, detailed descriptions
4. Include type hints
5. Handle errors gracefully
6. Add a `get_*_tools()` function

Example:

```python
"""Module description."""

from langchain_core.tools import tool


@tool
def my_tool(param: str) -> str:
    """Clear description that the LLM will use.
    
    Be specific about what the tool does, what inputs it expects,
    and what it returns. The LLM uses this to decide when to use the tool.
    
    Args:
        param: Description of the parameter
        
    Returns:
        Description of return value
    """
    # Implementation
    return result


def get_my_tools():
    """Get all tools from this module.
    
    Returns:
        List of tools
    """
    return [my_tool]
```

### Creating Agents

When adding new agent types:

1. Create a new file in `src/agent_demo/agents/`
2. Provide a `create_*_agent()` function
3. Provide a `run_*_agent()` function
4. Document the agent's architecture and use cases
5. Include type hints

### Adding Examples

When adding examples:

1. Create a new file in `src/agent_demo/examples/`
2. Include a `main()` function
3. Add a `if __name__ == "__main__":` block
4. Check for API key before running
5. Provide clear output and error messages

## Testing

### Running Tests

```bash
python test_structure.py
```

### Adding Tests

When adding features, include tests that verify:
- Imports work correctly
- Tools execute properly
- Error handling works
- Edge cases are handled

Example test:

```python
def test_my_feature():
    """Test description."""
    from agent_demo.tools.my_tool import my_tool
    
    result = my_tool.invoke({"param": "test"})
    assert result == expected_value
```

## Pull Request Process

1. **Update documentation** if you're adding features
2. **Update README.md** if needed
3. **Update USAGE.md** with examples if relevant
4. **Ensure all tests pass**
5. **Write a clear PR description** explaining:
   - What problem this solves
   - How it's implemented
   - Any breaking changes
   - How to test it

## Types of Contributions

We welcome various types of contributions:

### New Tools
- File operations (read, write, list)
- API integrations (weather, news, etc.)
- Database operations
- Web scraping
- Data processing

### New Agent Architectures
- Multi-agent systems
- Agents with memory
- Streaming agents
- Async agents
- Specialized agents (coding, analysis, etc.)

### Examples and Tutorials
- Jupyter notebooks
- Real-world use cases
- Integration examples
- Best practices

### Documentation
- Tutorial improvements
- API documentation
- Architecture explanations
- Use case guides

### Infrastructure
- Testing framework
- CI/CD setup
- Docker support
- Deployment examples

## Code Review

All contributions will be reviewed for:
- Code quality and style
- Test coverage
- Documentation completeness
- Security considerations
- Performance implications

## Security

- Never commit API keys or secrets
- Validate user inputs in tools
- Handle errors securely
- Report security issues privately

## Questions?

- Open an issue for questions
- Start a discussion for brainstorming
- Tag maintainers for urgent issues

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes
- Git commit history

Thank you for contributing to Agent Demo!
