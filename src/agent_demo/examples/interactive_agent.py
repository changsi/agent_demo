"""Example: Interactive agent with user input."""

import os
from dotenv import load_dotenv
from agent_demo.tools.calculator import get_calculator_tools
from agent_demo.tools.search import get_search_tools
from agent_demo.agents.graph_agent import create_graph_agent, run_graph_agent


def main():
    """Run an interactive agent session."""
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
    
    print("=== Interactive Agent ===\n")
    print(f"Available tools: {[tool.name for tool in all_tools]}")
    print("\nType 'quit' or 'exit' to end the session.\n")
    
    # Create the graph agent
    app = create_graph_agent(all_tools)
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        # Process the query
        try:
            print("\nAgent: ", end="")
            response = run_graph_agent(app, user_input)
            print(f"{response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
