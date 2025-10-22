# Agent Demo Documentation

Welcome to the Agent Demo documentation! This repository demonstrates how to build AI agents using LangChain, LangGraph, and tool calling.

## 📚 Documentation

### Getting Started
- **[Quick Start Guide](../QUICKSTART.md)** - Get up and running in 5 minutes
- **[README](../README.md)** - Project overview and setup instructions

### Learning
- **[Usage Guide](../USAGE.md)** - Detailed usage patterns and examples
- **[Architecture Guide](../ARCHITECTURE.md)** - Deep dive into design and architecture

### Contributing
- **[Contributing Guide](../CONTRIBUTING.md)** - How to contribute to the project

## 🚀 Quick Links

### For Beginners
1. Start with [QUICKSTART.md](../QUICKSTART.md)
2. Try the [examples](../src/agent_demo/examples/)
3. Read [USAGE.md](../USAGE.md) for patterns

### For Developers
1. Read [ARCHITECTURE.md](../ARCHITECTURE.md)
2. Check [CONTRIBUTING.md](../CONTRIBUTING.md)
3. Explore the [source code](../src/agent_demo/)

### For Advanced Users
1. Study [ARCHITECTURE.md](../ARCHITECTURE.md)
2. Review [USAGE.md](../USAGE.md) advanced sections
3. Build custom agents and tools

## 📖 Documentation Structure

```
agent_demo/
├── QUICKSTART.md          # 5-minute getting started guide
├── README.md              # Project overview
├── USAGE.md               # Detailed usage guide
├── ARCHITECTURE.md        # Architecture and design
├── CONTRIBUTING.md        # Contribution guidelines
└── docs/
    └── index.md           # This file
```

## 🛠️ Code Structure

```
src/agent_demo/
├── agents/                # Agent implementations
│   ├── simple_agent.py   # ReAct pattern agent
│   └── graph_agent.py    # LangGraph state agent
├── tools/                 # Tool implementations
│   ├── calculator.py     # Math operations
│   └── search.py         # Search utilities
└── examples/              # Usage examples
    ├── simple_agent_example.py
    ├── graph_agent_example.py
    └── interactive_agent.py
```

## 📝 Common Tasks

### Run Examples
```bash
# Simple agent with calculator
python -m agent_demo.examples.simple_agent_example

# Graph agent with multiple tools
python -m agent_demo.examples.graph_agent_example

# Interactive chat
python -m agent_demo.examples.interactive_agent
```

### Create Custom Agent
```python
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.agents.simple_agent import create_simple_agent, run_simple_agent

agent = create_simple_agent(get_calculator_tools())
response = run_simple_agent(agent, "What is 10 + 5?")
```

### Create Custom Tool
```python
from langchain_core.tools import tool

@tool
def my_tool(input: str) -> str:
    """Description for the LLM."""
    return result
```

## 🎯 Learning Path

### Level 1: Beginner
- [ ] Complete [QUICKSTART.md](../QUICKSTART.md)
- [ ] Run all examples
- [ ] Understand basic tool usage
- [ ] Create your first custom tool

### Level 2: Intermediate
- [ ] Read [USAGE.md](../USAGE.md) completely
- [ ] Understand agent patterns
- [ ] Create custom agents
- [ ] Combine multiple tools

### Level 3: Advanced
- [ ] Study [ARCHITECTURE.md](../ARCHITECTURE.md)
- [ ] Understand state management
- [ ] Build multi-agent systems
- [ ] Contribute to the project

## 🔍 Find What You Need

### I want to...

**...get started quickly**
→ [QUICKSTART.md](../QUICKSTART.md)

**...understand how agents work**
→ [ARCHITECTURE.md](../ARCHITECTURE.md)

**...see usage examples**
→ [USAGE.md](../USAGE.md)

**...create custom tools**
→ [USAGE.md - Tool Development](../USAGE.md#tool-development)

**...build custom agents**
→ [USAGE.md - Agent Patterns](../USAGE.md#agent-patterns)

**...contribute code**
→ [CONTRIBUTING.md](../CONTRIBUTING.md)

**...understand the architecture**
→ [ARCHITECTURE.md](../ARCHITECTURE.md)

**...troubleshoot issues**
→ [USAGE.md - Troubleshooting](../USAGE.md#troubleshooting)

## 💡 Key Concepts

### Tools
Atomic functions that agents can use. Each tool should:
- Do one thing well
- Have a clear description
- Include type hints
- Handle errors gracefully

### Agents
Orchestrators that use tools to solve problems. Two types:
- **Simple Agent**: Basic ReAct pattern
- **Graph Agent**: Advanced state management

### State
In graph agents, state maintains:
- Conversation history
- Tool results
- Context information

## 🌟 Best Practices

1. **Start Simple**: Begin with simple_agent, move to graph_agent
2. **Clear Descriptions**: Tool descriptions guide the LLM
3. **Type Hints**: Always use type hints
4. **Error Handling**: Handle edge cases gracefully
5. **Test Tools**: Test tools independently before using in agents

## 📚 Additional Resources

### Official Documentation
- [LangChain Docs](https://python.langchain.com/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Docs](https://platform.openai.com/docs/)

### Research Papers
- [ReAct: Reasoning and Acting](https://arxiv.org/abs/2210.03629)
- [Tool Calling with LLMs](https://platform.openai.com/docs/guides/function-calling)

### Community
- [GitHub Issues](https://github.com/changsi/agent_demo/issues)
- [GitHub Discussions](https://github.com/changsi/agent_demo/discussions)

## 🤝 Getting Help

1. **Check Documentation**: Start with [QUICKSTART.md](../QUICKSTART.md)
2. **Review Examples**: Look at [examples/](../src/agent_demo/examples/)
3. **Search Issues**: Check [existing issues](https://github.com/changsi/agent_demo/issues)
4. **Ask Questions**: Open a new issue or discussion

## 🚀 What's Next?

After reading the documentation:

1. **Try Examples**: Run the provided examples
2. **Experiment**: Modify examples to learn
3. **Build**: Create your own agents and tools
4. **Share**: Contribute back to the project

---

Ready to start? Head over to [QUICKSTART.md](../QUICKSTART.md)!
