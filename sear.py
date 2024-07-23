from googlesearch import search

class SearchEngine:
    def __init__(self):
        pass

    def search(self, query):
        # Perform a Google search with the given query
        search_results = list(search(query, num=5, stop=5))
        return search_results

# Example usage:
# Create an instance of the SearchEngine class
search_engine = SearchEngine()

# Perform a search with a query
results = search_engine.search("Python programming")

# Print the search results
for result in results:
    print(result)
