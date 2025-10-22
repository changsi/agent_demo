# Quick Start Guide

Get started with agent_demo in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation

```bash
# Clone the repository
git clone https://github.com/changsi/agent_demo.git
cd agent_demo

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Configuration

Create a `.env` file in the root directory:

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
echo "OPENAI_API_KEY=your-key-here" > .env
```

Or export it directly:

```bash
export OPENAI_API_KEY="your-key-here"
```

## Your First Agent

### Option 1: Run Pre-built Examples

Try the calculator agent:

```bash
python -m agent_demo.examples.simple_agent_example
```

Try the multi-tool agent:

```bash
python -m agent_demo.examples.graph_agent_example
```

Try interactive mode:

```bash
python -m agent_demo.examples.interactive_agent
```

### Option 2: Write Your Own (5 lines!)

Create a file called `my_agent.py`:

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.agents.simple_agent import create_simple_agent, run_simple_agent

agent = create_simple_agent(get_calculator_tools())
response = run_simple_agent(agent, "What is 25 + 17?")
print(response)
```

Run it:

```bash
python my_agent.py
```

## Common Use Cases

### Calculator Agent

Perfect for mathematical queries:

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.agents.simple_agent import create_simple_agent, run_simple_agent

agent = create_simple_agent(get_calculator_tools())
response = run_simple_agent(agent, "Calculate (15 + 5) * 2")
print(response)  # Output: The result is 40
```

### Multi-Tool Agent

Combines multiple tool types:

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.tools.search import get_search_tools
from agent_demo.agents.graph_agent import create_graph_agent, run_graph_agent

tools = get_calculator_tools() + get_search_tools()
agent = create_graph_agent(tools)
response = run_graph_agent(agent, "What time is it?")
print(response)
```

### Interactive Chat

Chat with your agent:

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.tools.search import get_search_tools
from agent_demo.agents.graph_agent import create_graph_agent, run_graph_agent

tools = get_calculator_tools() + get_search_tools()
agent = create_graph_agent(tools)

while True:
    query = input("You: ")
    if query.lower() in ["quit", "exit"]:
        break
    response = run_graph_agent(agent, query)
    print(f"Agent: {response}")
```

## Creating Your Own Tool

Add custom functionality in 3 steps:

**Step 1**: Create your tool

```python
from langchain_core.tools import tool

@tool
def get_joke() -> str:
    """Tell a programming joke."""
    return "Why do programmers prefer dark mode? Because light attracts bugs!"
```

**Step 2**: Use it in an agent

```python
from agent_demo.agents.simple_agent import create_simple_agent, run_simple_agent

tools = [get_joke]
agent = create_simple_agent(tools)
```

**Step 3**: Run it

```python
response = run_simple_agent(agent, "Tell me a joke")
print(response)
```

## Customization

### Use a Different Model

```python
agent = create_simple_agent(
    tools=tools,
    model_name="gpt-4",  # More capable but slower
    temperature=0.7      # More creative
)
```

### Add Multiple Tools

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.tools.search import get_search_tools

all_tools = get_calculator_tools() + get_search_tools()
agent = create_simple_agent(all_tools)
```

## Troubleshooting

### "OPENAI_API_KEY not found"

**Solution**: Make sure you've set the API key:
```bash
export OPENAI_API_KEY="your-key-here"
# Or create a .env file with the key
```

### "Module not found: agent_demo"

**Solution**: Install the package:
```bash
pip install -e .
```

### "Rate limit exceeded"

**Solution**: You've exceeded your API quota. Wait a moment or check your OpenAI account.

### "Tool not being called"

**Solution**: Make sure your tool has a clear description:
```python
@tool
def my_tool(input: str) -> str:
    """This description should be VERY clear about what the tool does."""
    return result
```

## Next Steps

- **Read the docs**: Check out [README.md](README.md) for overview
- **Learn patterns**: Read [USAGE.md](USAGE.md) for advanced usage
- **Understand architecture**: Read [ARCHITECTURE.md](ARCHITECTURE.md)
- **Contribute**: Read [CONTRIBUTING.md](CONTRIBUTING.md)

## Quick Reference

### Simple Agent Pattern

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.agents.simple_agent import create_simple_agent, run_simple_agent

agent = create_simple_agent(get_calculator_tools())
response = run_simple_agent(agent, "your query")
```

### Graph Agent Pattern

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.agents.graph_agent import create_graph_agent, run_graph_agent

agent = create_graph_agent(get_calculator_tools())
response = run_graph_agent(agent, "your query")
```

### Custom Tool Pattern

```python
from langchain_core.tools import tool

@tool
def my_tool(param: str) -> str:
    """Clear description of what this tool does."""
    return result
```

## Examples Summary

| Example | Description | Command |
|---------|-------------|---------|
| Simple Agent | Basic calculator agent | `python -m agent_demo.examples.simple_agent_example` |
| Graph Agent | Multi-tool agent | `python -m agent_demo.examples.graph_agent_example` |
| Interactive | Chat interface | `python -m agent_demo.examples.interactive_agent` |

## Need Help?

- **Issues**: [Open an issue](https://github.com/changsi/agent_demo/issues)
- **Discussions**: Start a discussion on GitHub
- **Documentation**: Check [README.md](README.md) and [USAGE.md](USAGE.md)

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

**That's it!** You're ready to build AI agents. Start with the examples and modify them to suit your needs.

Happy building! 🚀
