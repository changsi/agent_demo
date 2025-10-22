"""Simple agent using LangChain with tool calling."""

from typing import List
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate


def create_simple_agent(
    tools: List[BaseTool],
    model_name: str = "gpt-4o-mini",
    temperature: float = 0.0
) -> AgentExecutor:
    """Create a simple agent with tool calling capabilities.
    
    Args:
        tools: List of tools the agent can use
        model_name: Name of the OpenAI model to use
        temperature: Temperature for the model
        
    Returns:
        AgentExecutor ready to run
    """
    # Create the LLM
    llm = ChatOpenAI(model=model_name, temperature=temperature)
    
    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Use the available tools to answer questions."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    # Create the agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent_executor


def run_simple_agent(agent_executor: AgentExecutor, query: str) -> str:
    """Run the agent with a query.
    
    Args:
        agent_executor: The agent executor
        query: The query to process
        
    Returns:
        The agent's response
    """
    result = agent_executor.invoke({"input": query})
    return result["output"]
