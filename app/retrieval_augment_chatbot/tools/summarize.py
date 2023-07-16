import requests
import html2text

import VirtualLLM

text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
text_maker.ignore_images = True

def grab_webpage(url, text_maker):
    req = requests.get(url)
    return text_maker.handle(req.text)

chunk_size = 800
chunk_overlap = 30

def chop_document(doc):
    tDoc = VirtualLLM.tokenize(doc)

    chunks = []
    b = 0
    reachedEnd = False
    while not reachedEnd:
        reachedEnd = not (b + chunk_size < len(tDoc))
        cur_chunk = VirtualLLM.detokenize(tDoc[b:b + chunk_size])
        chunks.append(cur_chunk)
        b = b + chunk_size - chunk_overlap
    return chunks

main_question = "Provide a summary of the article towards answering the question: Give me a summary of news on debt ceiling in the US."

def summarize_webpage(doc, main_question):
    chunks = chop_document(doc)
    cur_ans = ""
    for chunk in chunks:
        refine_prompt_formated = refine_prompt.format(question=main_question,\
                    snippet=chunk,\
                    partialans=cur_ans)
        cur_ans = VirtualLLM.generate(refine_prompt_formated)
    return cur_ans
