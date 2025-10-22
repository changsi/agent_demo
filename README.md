# Agent Demo

A comprehensive demonstration repository for building AI agents using LangChain, LangGraph, and tool calling capabilities.

## Features

- **Simple Agents**: Basic agent implementation using LangChain's tool calling
- **Graph Agents**: Advanced agents with state management using LangGraph
- **Custom Tools**: Examples of custom tool implementations (calculator, search)
- **Interactive Mode**: Chat with agents in real-time
- **Multiple Examples**: Ready-to-run example scripts

## Project Structure

```
agent_demo/
├── src/
│   └── agent_demo/
│       ├── agents/          # Agent implementations
│       │   ├── simple_agent.py    # Basic LangChain agent
│       │   └── graph_agent.py     # LangGraph-based agent
│       ├── tools/           # Tool implementations
│       │   ├── calculator.py      # Math operations
│       │   └── search.py          # Search & utilities
│       └── examples/        # Usage examples
│           ├── simple_agent_example.py
│           ├── graph_agent_example.py
│           └── interactive_agent.py
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/api-keys)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/changsi/agent_demo.git
cd agent_demo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Simple Agent Example

Demonstrates a basic agent using LangChain with calculator tools:

```bash
python -m agent_demo.examples.simple_agent_example
```

This example shows:
- Creating a simple agent with tool calling
- Using calculator tools (add, multiply, subtract, divide)
- Processing mathematical queries

### Graph Agent Example

Demonstrates a LangGraph-based agent with state management:

```bash
python -m agent_demo.examples.graph_agent_example
```

This example shows:
- Building stateful agents with LangGraph
- Using multiple tool categories (calculator + search)
- State management across tool calls

### Interactive Agent

Chat with an agent in real-time:

```bash
python -m agent_demo.examples.interactive_agent
```

Type your queries and the agent will respond using available tools. Type 'quit' or 'exit' to end the session.

## Architecture

### Simple Agent (LangChain)

The simple agent uses LangChain's `create_tool_calling_agent` to:
1. Accept user input
2. Decide which tools to use
3. Execute tools
4. Return formatted responses

**Use case**: Quick prototyping, simple workflows

### Graph Agent (LangGraph)

The graph agent uses LangGraph's StateGraph for:
1. Complex state management
2. Multi-step reasoning
3. Conditional logic flows
4. Tool orchestration

**Use case**: Production applications, complex workflows

### Custom Tools

Tools are created using LangChain's `@tool` decorator:

```python
from langchain_core.tools import tool

@tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b
```

Each tool requires:
- Clear function name
- Type hints for parameters
- Descriptive docstring (used by the LLM)
- Return value

## Creating Custom Tools

To add your own tools:

1. Create a new file in `src/agent_demo/tools/`
2. Define tools using the `@tool` decorator
3. Add clear descriptions in docstrings
4. Import and use in your agent

Example:

```python
from langchain_core.tools import tool

@tool
def my_custom_tool(input: str) -> str:
    """Description of what this tool does."""
    # Your implementation
    return result
```

## Examples Walkthrough

### Calculator Tools

Located in `src/agent_demo/tools/calculator.py`:
- `add`: Add two numbers
- `multiply`: Multiply two numbers
- `subtract`: Subtract two numbers
- `divide`: Divide two numbers (with zero check)

### Search Tools

Located in `src/agent_demo/tools/search.py`:
- `search_web`: Simulated web search
- `get_current_time`: Get current timestamp

Note: The search tool is simulated for demonstration. In production, replace with actual search API.

## Advanced Usage

### Customizing the Agent

You can customize model parameters:

```python
from agent_demo.agents.simple_agent import create_simple_agent
from agent_demo.tools.calculator import get_calculator_tools

tools = get_calculator_tools()
agent = create_simple_agent(
    tools=tools,
    model_name="gpt-4",  # Use a different model
    temperature=0.7      # Adjust creativity
)
```

### Adding Memory

For conversation history, extend the state:

```python
from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: List[BaseMessage]
    conversation_history: List[str]  # Add custom state
```

## Troubleshooting

### API Key Issues

If you get authentication errors:
1. Verify your `.env` file contains `OPENAI_API_KEY`
2. Check the API key is valid at https://platform.openai.com/api-keys
3. Ensure the key has sufficient credits

### Import Errors

If modules aren't found:
1. Verify you're in the correct directory
2. Ensure virtual environment is activated
3. Run: `pip install -e .` to install in development mode

### Tool Calling Errors

If tools aren't being called:
1. Check tool descriptions are clear and detailed
2. Verify model supports tool calling (gpt-4o-mini, gpt-4, etc.)
3. Review the verbose output for debugging

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests if applicable
4. Submit a pull request

## License

MIT License - feel free to use this code for learning and projects.

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

## Future Enhancements

Potential additions:
- [ ] Add memory/conversation history
- [ ] Implement streaming responses
- [ ] Add more tool examples (file operations, API calls)
- [ ] Add unit tests
- [ ] Add vector store integration
- [ ] Add multi-agent examples
- [ ] Add async support
