"""LangGraph-based agent with state management."""

from typing import TypedDict, Annotated, List
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """State of the agent."""
    messages: Annotated[List[BaseMessage], add_messages]


def create_graph_agent(
    tools: List[BaseTool],
    model_name: str = "gpt-4o-mini",
    temperature: float = 0.0
):
    """Create a LangGraph-based agent with state management.
    
    Args:
        tools: List of tools the agent can use
        model_name: Name of the OpenAI model to use
        temperature: Temperature for the model
        
    Returns:
        Compiled graph ready to run
    """
    # Create the LLM with tools bound
    llm = ChatOpenAI(model=model_name, temperature=temperature)
    llm_with_tools = llm.bind_tools(tools)
    
    # Define the agent node
    def call_model(state: AgentState):
        """Call the model with the current state."""
        messages = state["messages"]
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}
    
    # Define the conditional edge
    def should_continue(state: AgentState):
        """Determine if we should continue or end."""
        messages = state["messages"]
        last_message = messages[-1]
        
        # If there are no tool calls, we're done
        if not hasattr(last_message, "tool_calls") or not last_message.tool_calls:
            return "end"
        return "continue"
    
    # Create the graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", ToolNode(tools))
    
    # Set the entry point
    workflow.set_entry_point("agent")
    
    # Add edges
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "continue": "tools",
            "end": END
        }
    )
    workflow.add_edge("tools", "agent")
    
    # Compile the graph
    app = workflow.compile()
    
    return app


def run_graph_agent(app, query: str) -> str:
    """Run the graph agent with a query.
    
    Args:
        app: The compiled graph
        query: The query to process
        
    Returns:
        The agent's response
    """
    # Create initial state
    initial_state = {"messages": [HumanMessage(content=query)]}
    
    # Run the graph
    result = app.invoke(initial_state)
    
    # Extract the final response
    final_message = result["messages"][-1]
    return final_message.content
