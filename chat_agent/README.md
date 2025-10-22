# LangGraph Demo with Azure OpenAI

This project demonstrates how to build an AI agent using **LangChain**, **LangGraph**, and **Azure OpenAI API** with tool calling capabilities.

## 🎯 What This Demo Does

The demo showcases a LangGraph agent that:
1. **Receives user queries** through a conversational interface
2. **Decides automatically** whether to use tools or respond directly
3. **Calls tools** (like getting weather information) when needed
4. **Synthesizes responses** based on tool results
5. **Handles multi-turn conversations** with state management

## 🏗️ Architecture

The agent uses a state graph with two main nodes:
- **Agent Node**: Calls Azure OpenAI to decide the next action
- **Tool Node**: Executes the requested tools

The flow:
```
User Input → Agent (LLM) → Tool Call? 
                          ├─ Yes → Execute Tool → Agent (LLM) → Response
                          └─ No → Response
```

## 📋 Prerequisites

- Python 3.8+
- Azure OpenAI account with:
  - An endpoint URL
  - An API key
  - A deployed chat model (e.g., GPT-4, GPT-3.5-turbo)

## 🚀 Quick Start

### 1. Clone and Setup

```bash
cd /path/to/agent_demo
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Azure OpenAI Credentials

Copy the example environment file:
```bash
cp env.example .env
```

Edit `.env` and fill in your Azure OpenAI credentials:
```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
OPENAI_API_VERSION=2024-02-01
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your-deployment-name
```

### 3. Run the Demo

Once your `.env` file is configured:
```bash
python chat_agent_demo.py
```

## 📦 Project Structure

```
agent_demo/
├── chat_agent/
│   ├── chat_agent_demo.py   # Main demo script with Azure OpenAI
│   └── README.md            # This file
├── requirements.txt         # Python dependencies
├── env.example             # Template for environment variables
├── .env                    # Your credentials (create from env.example)
└── venv/                   # Virtual environment (created by you)
```

## 🔧 Key Components

### Tools
The demo includes a mock `get_weather` tool that returns weather information for cities:
```python
@tool
def get_weather(city: str) -> str:
    """Get the current weather for a specific city."""
    # Returns mock weather data
```

### State Management
The agent state tracks the conversation history:
```python
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
```

### Graph Structure
```python
graph_builder = StateGraph(AgentState)
graph_builder.add_node("agent", call_model)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges("agent", tools_condition)
graph_builder.add_edge("tools", "agent")
```

## 📊 Example Output

### Demo 1: Query with Tool Call
```
User: "What is the weather in San Francisco?"

Agent → Decides to call get_weather tool
Tool → Returns: {"city": "San Francisco", "temperature": "15°C", "conditions": "Foggy"}
Agent → "Right now in San Francisco it's 15°C (59°F) and foggy. 
         Expect reduced visibility — a light jacket or layers are recommended."
```

### Demo 2: Query without Tool Call
```
User: "Hi, my name is Bob."

Agent → "Hi Bob — nice to meet you! How can I help you today?"
```

## 🛠️ Dependencies

- `langchain` - Core LangChain library
- `langchain-core` - Core abstractions
- `langchain-openai` - Azure OpenAI integration
- `langgraph` - Graph-based agent framework
- `python-dotenv` - Environment variable management
- `typing-extensions` - Enhanced type hints

## 📝 Customizing the Demo

### Adding New Tools

```python
@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Add to tools list
tools = [get_weather, calculate]
```

### Changing the LLM Settings

```python
llm = AzureChatOpenAI(
    api_version=os.environ["OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    # Note: Some models (like gpt-5-mini) only support default temperature
    # temperature=0.7,  # Uncomment if your model supports it
    # max_tokens=500,   # Limit response length
)
```

## 🐛 Troubleshooting

### Import Errors
- Ensure you've activated the virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

### Azure API Errors
- Verify your `.env` file has correct credentials
- Check that your Azure deployment is active
- Ensure your API version matches your deployment
- **Temperature errors**: Some models (like gpt-5-mini) only support default temperature values

### Tool Not Being Called
- Check that the tool has a clear docstring
- Ensure the tool is added to the `tools` list
- Try being more explicit in your query

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

## 🎓 Learning Points

This demo teaches:
- ✅ Setting up LangGraph with Azure OpenAI
- ✅ Defining and using tools with function calling
- ✅ Building state graphs for agents
- ✅ Handling conditional flows
- ✅ Managing conversation state
- ✅ Real-world API integration and testing

## 📄 License

This is a demo project for educational purposes.

---

**Happy Building! 🚀**
