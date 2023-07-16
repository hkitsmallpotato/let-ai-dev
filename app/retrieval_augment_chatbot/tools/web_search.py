from duckduckgo_search import DDGS

def do_search(query, limit=10):
    search_result = None
    with DDGS() as ddgs:
        ddgs_gen = ddgs.text(query, backend="lite")
        search_result = [r for r in islice(ddgs_gen, limit)]
    return search_result

def display_search_result(search_result):
    return "\n".join(["{n}. [{title}]({url})\n{body}"
        .format(n=i+1, \
                title=search_result[i]["title"], \
                url=search_result[i]["href"], \
                body=search_result[i]["body"]) \
        for i in range(0, 10)])
