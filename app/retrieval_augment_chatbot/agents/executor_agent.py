class ExecutorAgent:
    def executeAction(self, action):
        actionType = action["type"]
        if actionType == "search":
            qRes = do_search(action["arg"])
            formattedRes = display_search_result(qRes)
            return searchResultTemplate.format(res=formattedRes)
        elif actionType == "visit":
            doc = grab_webpage(action["arg"]["url"], text_maker)
            return summarize_webpage(chop_document(doc), action["arg"]["question"])
