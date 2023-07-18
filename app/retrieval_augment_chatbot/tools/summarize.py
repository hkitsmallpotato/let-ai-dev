import requests
import html2text

#from llm.virtual_llm import VirtualLLM

text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
text_maker.ignore_images = True

def grab_webpage(url, text_maker):
    req = requests.get(url)
    return text_maker.handle(req.text)

chunk_size = 800
chunk_overlap = 30

def chop_document(doc, llm):
    tDoc = llm.tokenize(doc)

    chunks = []
    b = 0
    reachedEnd = False
    while not reachedEnd:
        reachedEnd = not (b + chunk_size < len(tDoc))
        cur_chunk = llm.detokenize(tDoc[b:b + chunk_size])
        chunks.append(cur_chunk)
        b = b + chunk_size - chunk_overlap
    return chunks

#main_question = "Provide a summary of the article towards answering the question: Give me a summary of news on debt ceiling in the US."

refine_prompt = """### Instruction
Consider this question or request:

{question}

Input section below contains:
- Part of the text of a webpage (also called a snippet)
- (Optionally) a partial answer to the question or request above based on reading previous parts of the webpage.

Create or refine a partial answer towards answering the question or request based on any new info contained in the text of the webpage provided. Write your updated partial answer in the output section. If you did not find any useful info in the snippet, please simply copy the existing partial answer in input section to the output section.

### Input
Part of the text of webpage (snippet):
{snippet}
----
Partial answer so far (can be empty):
{partialans}
### Output
*Updated partial answer*: """

def summarize_webpage(doc, llm, main_question):
    chunks = chop_document(doc)
    cur_ans = ""
    for chunk in chunks:
        refine_prompt_formated = refine_prompt.format(question=main_question,\
                    snippet=chunk,\
                    partialans=cur_ans)
        cur_ans = llm.generate(refine_prompt_formated, "normal", 300)
    return cur_ans
