from googlesearch import search

def get_info(search_query):
    search_results = list(search(search_query, num=5, stop=5))
    return search_results
