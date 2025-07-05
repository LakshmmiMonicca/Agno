from agno.tools import tool



@tool

def google_search(query: str) -> str:

    """

    Dummy Google search tool. Replace with real API or web scraping if needed.



    Args:

        query (str): The search query.



    Returns:

        str: Simulated search results.

    """

    # Replace with real API logic (e.g., SerpAPI or Google Custom Search API)

    return f"Top 3 results for '{query}':\n1. Result A\n2. Result B\n3. Result C"
