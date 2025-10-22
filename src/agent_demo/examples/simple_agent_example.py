"""Example: Simple agent with calculator tools."""

import os
from dotenv import load_dotenv
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.agents.simple_agent import create_simple_agent, run_simple_agent


def main():
    """Run the simple agent example."""
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please set your OpenAI API key in a .env file or as an environment variable.")
        return
    
    # Get tools
    tools = get_calculator_tools()
    
    print("=== Simple Agent with Calculator Tools ===\n")
    print(f"Available tools: {[tool.name for tool in tools]}\n")
    
    # Create the agent
    agent = create_simple_agent(tools)
    
    # Example queries
    queries = [
        "What is 25 + 17?",
        "Multiply 8 by 9",
        "What is (15 + 5) * 2?",
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        print("-" * 50)
        try:
            response = run_simple_agent(agent, query)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
