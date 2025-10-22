"""Search tool for information retrieval (simulated)."""

from langchain_core.tools import tool


@tool
def search_web(query: str) -> str:
    """Search the web for information (simulated).
    
    This is a simulated search tool that returns mock results.
    In a real implementation, this would connect to a search API.
    
    Args:
        query: The search query
        
    Returns:
        Search results as a string
    """
    # Simulated search results
    mock_results = {
        "python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "langchain": "LangChain is a framework for developing applications powered by language models.",
        "langgraph": "LangGraph is a library for building stateful, multi-actor applications with LLMs.",
        "weather": "The weather today is sunny with a high of 75°F and a low of 60°F.",
    }
    
    # Simple keyword matching
    query_lower = query.lower()
    for keyword, result in mock_results.items():
        if keyword in query_lower:
            return f"Search results for '{query}': {result}"
    
    return f"Search results for '{query}': No specific information found. This is a simulated search tool."


@tool
def get_current_time() -> str:
    """Get the current time.
    
    Returns:
        Current time as a string
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_search_tools():
    """Get all search tools.
    
    Returns:
        List of search tools
    """
    return [search_web, get_current_time]
