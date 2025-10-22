# Usage Guide

This guide provides detailed examples and usage patterns for the agent_demo package.

## Quick Start

### 1. Basic Setup

```bash
# Install the package
pip install -e .

# Set up your API key
export OPENAI_API_KEY="your-api-key-here"
# Or create a .env file with: OPENAI_API_KEY=your-api-key-here
```

### 2. Using the Simple Agent

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.agents.simple_agent import create_simple_agent, run_simple_agent

# Get tools
tools = get_calculator_tools()

# Create agent
agent = create_simple_agent(tools)

# Run a query
response = run_simple_agent(agent, "What is 15 + 27?")
print(response)
```

### 3. Using the Graph Agent

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.tools.search import get_search_tools
from agent_demo.agents.graph_agent import create_graph_agent, run_graph_agent

# Get tools
all_tools = get_calculator_tools() + get_search_tools()

# Create agent
app = create_graph_agent(all_tools)

# Run a query
response = run_graph_agent(app, "What is 25 * 4?")
print(response)
```

## Tool Development

### Creating a Custom Tool

Tools are the building blocks of agents. Here's how to create your own:

```python
from langchain_core.tools import tool

@tool
def my_tool(input: str) -> str:
    """Clear description of what the tool does.
    
    The description is crucial - the LLM uses it to decide when to use the tool.
    Be specific about:
    - What the tool does
    - What inputs it expects
    - What it returns
    
    Args:
        input: Description of the input parameter
        
    Returns:
        Description of what is returned
    """
    # Your implementation here
    result = process_input(input)
    return result
```

### Tool Best Practices

1. **Clear Descriptions**: The docstring is used by the LLM to understand the tool
2. **Type Hints**: Always include type hints for parameters and return values
3. **Error Handling**: Handle edge cases and invalid inputs gracefully
4. **Single Responsibility**: Each tool should do one thing well

### Example: Weather Tool

```python
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location.
    
    This tool provides weather information including temperature,
    conditions, and forecast for a given location.
    
    Args:
        location: The city or location name (e.g., "New York", "London")
        
    Returns:
        A string describing the current weather conditions
    """
    # In a real implementation, this would call a weather API
    return f"The weather in {location} is sunny with a temperature of 72°F."
```

## Agent Patterns

### Pattern 1: Multi-Step Reasoning

The agent can chain multiple tools together:

```python
# The agent can:
# 1. Call search_web to find information
# 2. Use calculator tools to perform calculations
# 3. Combine results to answer complex questions

response = run_graph_agent(app, 
    "Search for the population of Tokyo and divide it by 2")
```

### Pattern 2: Conditional Tool Use

The agent decides which tools to use based on the query:

```python
# Mathematical query -> uses calculator tools
run_graph_agent(app, "What is 50 * 20?")

# Information query -> uses search tools
run_graph_agent(app, "What is LangGraph?")

# Time-based query -> uses get_current_time
run_graph_agent(app, "What time is it?")
```

### Pattern 3: Tool-Free Queries

If the query doesn't require tools, the agent responds directly:

```python
# No tools needed for general knowledge
run_graph_agent(app, "What is the capital of France?")
```

## Agent Architectures

### Simple Agent (React Pattern)

The simple agent uses the ReAct (Reasoning and Acting) pattern:

1. **Reason**: Analyze the query and decide what to do
2. **Act**: Use a tool if needed
3. **Observe**: Look at the tool's output
4. **Repeat**: Continue until the answer is complete

**When to use:**
- Quick prototypes
- Simple workflows
- Single-step tasks

### Graph Agent (State Management)

The graph agent uses LangGraph for complex state management:

1. **State**: Maintains conversation history and context
2. **Nodes**: Different processing stages (agent, tools)
3. **Edges**: Control flow between stages
4. **Conditional Logic**: Dynamic routing based on state

**When to use:**
- Production applications
- Multi-step workflows
- Complex decision trees
- Memory requirements

## Advanced Configuration

### Customizing the Model

```python
# Use GPT-4 for better reasoning
agent = create_simple_agent(
    tools=tools,
    model_name="gpt-4",
    temperature=0.0  # More deterministic
)

# More creative responses
agent = create_simple_agent(
    tools=tools,
    model_name="gpt-4o-mini",
    temperature=0.7  # More creative
)
```

### Adding Multiple Tool Categories

```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.tools.search import get_search_tools
# from your_custom_tools import get_custom_tools

all_tools = (
    get_calculator_tools() + 
    get_search_tools() +
    # get_custom_tools() +
)

agent = create_graph_agent(all_tools)
```

### Streaming Responses

For real-time feedback, you can stream the agent's thinking:

```python
from langchain_core.messages import HumanMessage

# Create the agent
app = create_graph_agent(tools)

# Stream the response
for chunk in app.stream({"messages": [HumanMessage(content="What is 5 + 3?")]}):
    if "messages" in chunk:
        print(chunk["messages"][-1].content)
```

## Error Handling

### API Key Issues

```python
import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not set. Please set it in .env or environment.")
```

### Tool Errors

```python
@tool
def safe_divide(a: float, b: float) -> float:
    """Safely divide two numbers."""
    try:
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    except Exception as e:
        return f"Error: {str(e)}"
```

### Agent Timeout

```python
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Agent took too long to respond")

# Set a 30-second timeout
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(30)

try:
    response = run_graph_agent(app, query)
finally:
    signal.alarm(0)  # Cancel the alarm
```

## Testing

### Testing Tools

```python
def test_calculator_tools():
    from agent_demo.tools.calculator import add, multiply
    
    assert add.invoke({"a": 2, "b": 3}) == 5.0
    assert multiply.invoke({"a": 4, "b": 5}) == 20.0
```

### Testing Agents (Mock)

```python
from unittest.mock import Mock, patch

def test_agent_with_mock():
    # Mock the LLM to avoid API calls
    with patch('langchain_openai.ChatOpenAI') as mock_llm:
        mock_llm.return_value = Mock()
        
        agent = create_simple_agent(tools)
        # Test agent behavior without making API calls
```

## Performance Tips

1. **Model Selection**: Use `gpt-4o-mini` for cost-effective development
2. **Temperature**: Use 0.0 for consistent results in testing
3. **Tool Descriptions**: Better descriptions = fewer wasted API calls
4. **Caching**: Consider implementing response caching for repeated queries
5. **Parallel Tools**: LangGraph can call multiple tools in parallel when possible

## Common Pitfalls

1. **Vague Tool Descriptions**: The LLM needs clear descriptions to choose the right tool
2. **Too Many Tools**: More than 20 tools can confuse the agent
3. **Missing Type Hints**: Type hints help the LLM understand parameters
4. **No Error Handling**: Always handle edge cases in tools
5. **Forgetting API Key**: Always check the API key is set

## Production Checklist

- [ ] Set up proper error handling
- [ ] Implement logging for debugging
- [ ] Add rate limiting for API calls
- [ ] Use environment variables for configuration
- [ ] Add monitoring and alerting
- [ ] Implement response caching
- [ ] Set up proper testing
- [ ] Document custom tools thoroughly
- [ ] Consider cost optimization strategies
- [ ] Add user input validation

## Next Steps

1. Try the example scripts in `src/agent_demo/examples/`
2. Create your own custom tools
3. Experiment with different agent architectures
4. Build a multi-agent system
5. Add memory and conversation history
6. Integrate with external APIs

## Resources

- [LangChain Docs](https://python.langchain.com/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
