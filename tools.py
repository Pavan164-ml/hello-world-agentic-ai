# tools.py
from duckduckgo_search import DDGS

# This tool allows the agent to search the web using DuckDuckGo.
def web_search(query: str) -> str:
    """
    Executes a web search for the given query using the DuckDuckGo Search API and returns the results.
    """
    print(f"--- Executing Web Search for: '{query}' ---")
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
        # We format the results into a string for the LLM to read.
        return str(results) if results else "No relevant search results found."

# This is a special tool. The agent calls this function when it has found the final answer.
def finish(answer: str) -> str:
    """
    Call this function when you have the complete and final answer to the user's question.
    """
    print(f"--- Agent has finished with answer: '{answer}' ---")
    return answer

# A dictionary that maps tool names to their actual function implementations.
AVAILABLE_TOOLS = {
    "web_search": web_search,
    "finish": finish,
}