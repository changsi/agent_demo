"""Simple agent using LangChain with tool calling."""

from typing import List
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent


def create_simple_agent(
    tools: List[BaseTool],
    model_name: str = "gpt-4o-mini",
    temperature: float = 0.0
):
    """Create a simple agent with tool calling capabilities.
    
    Args:
        tools: List of tools the agent can use
        model_name: Name of the OpenAI model to use
        temperature: Temperature for the model
        
    Returns:
        Compiled agent graph ready to run
    """
    # Create the LLM
    llm = ChatOpenAI(model=model_name, temperature=temperature)
    
    # Create the agent using LangGraph's prebuilt create_react_agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier="You are a helpful assistant. Use the available tools to answer questions."
    )
    
    return agent


def run_simple_agent(agent, query: str) -> str:
    """Run the agent with a query.
    
    Args:
        agent: The agent executor
        query: The query to process
        
    Returns:
        The agent's response
    """
    # Create messages
    messages = [HumanMessage(content=query)]
    
    # Run the agent
    result = agent.invoke({"messages": messages})
    
    # Extract the final response
    final_message = result["messages"][-1]
    return final_message.content
