# Architecture Guide

This document explains the architecture and design decisions for the agent_demo repository.

## Overview

The agent_demo repository demonstrates how to build AI agents using LangChain and LangGraph. It provides:

- **Reusable Tools**: Modular tool implementations
- **Agent Patterns**: Different agent architectures
- **Practical Examples**: Ready-to-run demonstrations
- **Clear Documentation**: Comprehensive guides

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Application                          │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Agent Layer                                 │
│                                                                   │
│  ┌────────────────────┐         ┌──────────────────────┐        │
│  │  Simple Agent      │         │  Graph Agent         │        │
│  │  (ReAct Pattern)   │         │  (State Management)  │        │
│  └────────┬───────────┘         └───────────┬──────────┘        │
│           │                                  │                   │
└───────────┼──────────────────────────────────┼───────────────────┘
            │                                  │
            └──────────────┬───────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Tool Layer                                  │
│                                                                   │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐      │
│  │ Calculator  │  │  Search      │  │  Custom Tools     │      │
│  │ Tools       │  │  Tools       │  │  (Your Tools)     │      │
│  │             │  │              │  │                   │      │
│  │ • add       │  │ • search_web │  │ • Your custom    │      │
│  │ • multiply  │  │ • get_time   │  │   tools here     │      │
│  │ • subtract  │  │              │  │                   │      │
│  │ • divide    │  │              │  │                   │      │
│  └─────────────┘  └──────────────┘  └───────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LangChain/LangGraph                           │
│                    (Framework Layer)                             │
└───────────────────────────┬─────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    OpenAI API (LLM)                              │
└─────────────────────────────────────────────────────────────────┘
```

## Component Design

### 1. Tool Layer

**Purpose**: Provide atomic, reusable functionality

**Design Principles**:
- Single Responsibility: Each tool does one thing
- Clear Interface: Well-defined inputs and outputs
- Self-Documenting: Comprehensive docstrings
- Error Handling: Graceful failure modes

**Implementation Pattern**:
```python
@tool
def tool_name(param: type) -> return_type:
    """Clear description for the LLM."""
    # Implementation
    return result
```

**Tool Categories**:
- **Calculator Tools**: Mathematical operations
- **Search Tools**: Information retrieval (simulated)
- **Utility Tools**: Time, date, etc.
- **Custom Tools**: User-defined functionality

### 2. Agent Layer

**Purpose**: Orchestrate tools to solve complex tasks

#### Simple Agent (ReAct Pattern)

**Architecture**:
```
Query → LLM → Decision → Tool Call → Observation → LLM → Response
         ↑                                            │
         └────────────────────────────────────────────┘
```

**Components**:
- **LLM**: GPT-4 or similar
- **Tools**: Bound to the agent
- **Prompt**: System instructions
- **Executor**: Manages the loop

**Use Cases**:
- Quick prototypes
- Simple workflows
- Single-step tasks
- Development and testing

**Code Flow**:
1. User provides query
2. LLM analyzes query
3. LLM decides to use tool or respond
4. If tool: execute tool, observe result, repeat from step 2
5. If no tool: return response

#### Graph Agent (LangGraph)

**Architecture**:
```
                Start
                  ↓
            ┌─────────┐
            │  Agent  │ ← State: messages
            └────┬────┘
                 │
          ┌──────┴───────┐
          │              │
    Tool Calls?       No Tool
          │              │
         Yes             ↓
          ↓            End
    ┌──────────┐
    │  Tools   │
    └────┬─────┘
         │
         └─ Back to Agent
```

**Components**:
- **State**: Maintains conversation history
- **Nodes**: Processing stages (agent, tools)
- **Edges**: Control flow
- **Conditional Logic**: Dynamic routing

**State Management**:
```python
class AgentState(TypedDict):
    messages: List[BaseMessage]  # Conversation history
    # Add custom state as needed
```

**Use Cases**:
- Production applications
- Complex workflows
- Multi-step reasoning
- Memory requirements

**Code Flow**:
1. Initialize state with user query
2. Agent node: LLM processes state
3. Conditional edge: Check for tool calls
4. If tool calls: Execute tools, update state, go to agent
5. If no tool calls: End, return final state

### 3. Example Layer

**Purpose**: Demonstrate usage patterns

**Examples**:
1. **simple_agent_example.py**: Basic usage
2. **graph_agent_example.py**: Advanced patterns
3. **interactive_agent.py**: Real-time interaction

## Design Decisions

### 1. Why Two Agent Patterns?

**Simple Agent**:
- Easier to understand
- Lower barrier to entry
- Good for learning
- Suitable for simple tasks

**Graph Agent**:
- More powerful
- Better state management
- Production-ready
- Handles complexity

### 2. Why Separate Tools?

- **Modularity**: Tools can be reused across agents
- **Testability**: Tools can be tested independently
- **Flexibility**: Easy to add/remove tools
- **Organization**: Clear separation of concerns

### 3. Why Simulated Search?

- **No API Dependencies**: Works out of the box
- **Learning Focus**: Demonstrates patterns, not API integration
- **Easy to Replace**: Swap with real API when needed

### 4. Why Type Hints?

- **LLM Understanding**: Better tool selection
- **Developer Experience**: IDE support
- **Documentation**: Self-documenting code
- **Error Prevention**: Catch issues early

## Data Flow

### Query Processing Flow

```
1. User Input
   ↓
2. Message Creation (HumanMessage)
   ↓
3. Agent Receives Message
   ↓
4. LLM Processing
   ├─→ Generate Response (No tool needed)
   │   ↓
   │   Return to User
   │
   └─→ Generate Tool Call
       ↓
5. Tool Execution
   ↓
6. Tool Result (ToolMessage)
   ↓
7. Back to Agent (step 3)
```

### State Evolution (Graph Agent)

```
Initial State:
{
  messages: [HumanMessage("What is 5 + 3?")]
}
   ↓
After Agent Node:
{
  messages: [
    HumanMessage("What is 5 + 3?"),
    AIMessage(tool_calls=[add(5, 3)])
  ]
}
   ↓
After Tool Node:
{
  messages: [
    HumanMessage("What is 5 + 3?"),
    AIMessage(tool_calls=[add(5, 3)]),
    ToolMessage("8.0")
  ]
}
   ↓
After Agent Node (Final):
{
  messages: [
    HumanMessage("What is 5 + 3?"),
    AIMessage(tool_calls=[add(5, 3)]),
    ToolMessage("8.0"),
    AIMessage("The sum is 8")
  ]
}
```

## Extension Points

### Adding New Tools

1. Create file in `src/agent_demo/tools/`
2. Implement tools with `@tool` decorator
3. Create `get_*_tools()` function
4. Import and use in agents

### Adding New Agent Types

1. Create file in `src/agent_demo/agents/`
2. Implement `create_*_agent()` function
3. Implement `run_*_agent()` function
4. Document usage patterns

### Adding Memory

Extend the state to include conversation history:

```python
class AgentState(TypedDict):
    messages: List[BaseMessage]
    conversation_history: List[Dict]
    context: Dict  # Additional context
```

### Adding Streaming

Modify the run function to use streaming:

```python
def run_agent_streaming(agent, query: str):
    for chunk in agent.stream({"messages": [HumanMessage(query)]}):
        yield chunk
```

## Performance Considerations

### API Calls

- Each agent invocation = 1+ API calls
- Tool calls add additional API calls
- Graph agents may require more calls for complex queries

### Cost Optimization

1. Use `gpt-4o-mini` for development
2. Implement response caching
3. Set appropriate temperature (0.0 for consistency)
4. Limit tool descriptions to essentials
5. Consider batch processing

### Latency

- Simple tasks: 1-3 seconds
- Complex tasks: 5-10 seconds
- Tool-heavy tasks: Varies by tool execution time

## Security Considerations

### API Keys

- Never commit API keys
- Use environment variables
- Rotate keys regularly
- Use separate keys for dev/prod

### Input Validation

- Validate all user inputs
- Sanitize tool outputs
- Handle edge cases
- Implement rate limiting

### Tool Security

- Sandbox tool execution
- Validate tool inputs
- Limit tool capabilities
- Log tool usage

## Testing Strategy

### Unit Tests

- Test individual tools
- Mock LLM responses
- Verify tool descriptions

### Integration Tests

- Test agent-tool interaction
- Verify state management
- Test error handling

### End-to-End Tests

- Test complete workflows
- Verify user experience
- Test edge cases

## Future Enhancements

### Planned Features

1. **Memory System**: Persistent conversation history
2. **Multi-Agent**: Agent collaboration
3. **Streaming**: Real-time responses
4. **Async Support**: Non-blocking operations
5. **Vector Store**: Semantic search
6. **Web Interface**: UI for interaction
7. **Monitoring**: Usage analytics
8. **Caching**: Response caching

### Extensibility

The architecture is designed to support:
- Custom agent patterns
- New tool categories
- Alternative LLM providers
- Different state management strategies
- Custom memory implementations

## References

- [LangChain Architecture](https://python.langchain.com/docs/concepts/architecture)
- [LangGraph Concepts](https://langchain-ai.github.io/langgraph/concepts/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Tool Calling Guide](https://platform.openai.com/docs/guides/function-calling)

## Conclusion

This architecture provides a flexible foundation for building AI agents. The separation of concerns (tools, agents, examples) makes it easy to understand, extend, and maintain. The dual-agent approach (simple and graph) balances ease of use with power and flexibility.
