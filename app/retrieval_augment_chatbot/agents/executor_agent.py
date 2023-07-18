import tools.web_search as ws

searchResultTemplate = """Here are the search results:
{res}
(End of search result)
"""

class ExecutorAgent:
    def executeAction(self, action):
        actionType = action["type"]
        if actionType == "search":
            qRes = ws.do_search(action["arg"]["query"])
            formattedRes = ws.display_search_result(qRes)
            return searchResultTemplate.format(res=formattedRes)
        #elif actionType == "visit":
        #    doc = grab_webpage(action["arg"]["url"], text_maker)
        #    return summarize_webpage(chop_document(doc), action["arg"]["question"])
        else:
            raise Exception("Unknown action type: " + actionType)
