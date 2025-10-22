"""Example: LangGraph agent with multiple tools."""

import os
from dotenv import load_dotenv
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.tools.search import get_search_tools
from agent_demo.agents.graph_agent import create_graph_agent, run_graph_agent


def main():
    """Run the graph agent example."""
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please set your OpenAI API key in a .env file or as an environment variable.")
        return
    
    # Get tools
    calculator_tools = get_calculator_tools()
    search_tools = get_search_tools()
    all_tools = calculator_tools + search_tools
    
    print("=== LangGraph Agent with Multiple Tools ===\n")
    print(f"Available tools: {[tool.name for tool in all_tools]}\n")
    
    # Create the graph agent
    app = create_graph_agent(all_tools)
    
    # Example queries
    queries = [
        "What is 45 + 55?",
        "Search for information about LangChain",
        "What time is it now?",
        "Calculate 12 * 8 and then add 10 to the result",
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        print("-" * 50)
        try:
            response = run_graph_agent(app, query)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
