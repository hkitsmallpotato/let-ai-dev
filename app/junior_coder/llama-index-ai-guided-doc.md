How to use semantic search?
👨‍💻
🤖

To use semantic search with LlamaIndex, you can create a `GPTVectorStoreIndex` from your documents and then use it to create a query engine. Here's an example code snippet:

```python
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

# Load your documents
documents = SimpleDirectoryReader('data').load_data()

# Create the index
index = GPTVectorStoreIndex.from_documents(documents)

# Create the query engine
query_engine = index.as_query_engine()

# Query the engine
response = query_engine.query("What did the author do during his time at YC?")
```

This will return a response that matches the query using semantic search.

----

How do I load data into llama-index using the github loader? I also want to load a document website into llama-index.
👨‍💻
🤖

To load data into LlamaIndex using the Github loader, you can download the loader using the download_loader function and then use it to load your data. Here's an example code snippet:

```python
from llama_index import GPTVectorStoreIndex, download_loader

GithubRepoReader = download_loader('GithubRepoReader')

# Replace <owner> and <repo> with the owner and name of the Github repository you want to load
repo_url = f'https://github.com/<owner>/<repo>'
loader = GithubRepoReader()
documents = loader.load_data(repo_url=repo_url)

# Create the index
index = GPTVectorStoreIndex.from_documents(documents)
```

To load a document website into LlamaIndex, you can use the Web Page Reader data connector. Here's an example code snippet:

```python
from llama_index import GPTVectorStoreIndex, download_loader

WebPageReader = download_loader('WebPageReader')

# Replace <url> with the URL of the website you want to load
loader = WebPageReader()
documents = loader.load_data(url=<url>)

# Create the index
index = GPTVectorStoreIndex.from_documents(documents)
```

Note that you may need to install additional dependencies for the GithubRepoReader and WebPageReader data connectors to work properly.

----

Thanks. For the Web Page Reader, is there functions/addon within the llama-index ecosystem to crawl a website and load every page within the same domain into llama-index, or do I have to do it myself?
👨‍💻
🤖

Yes, there is a data connector within the LlamaIndex ecosystem that can crawl a website and load every page within the same domain into LlamaIndex. It's called the Web Crawler Reader and it's part of the LlamaHub repository. You can download it using the download_loader function and then use it to load your data. Here's an example code snippet:

```python
from llama_index import GPTVectorStoreIndex, download_loader

WebCrawlerReader = download_loader('WebCrawlerReader')

# Replace <url> with the URL of the website you want to crawl
loader = WebCrawlerReader()
documents = loader.load_data(url=<url>)

# Create the index
index = GPTVectorStoreIndex.from_documents(documents)
```

This will crawl the website and load every page within the same domain into LlamaIndex. Note that you may need to install additional dependencies for the Web Crawler Reader to work properly.

----

I see, that's indeed useful. For the map-reduce strategy to summarize a document, can I specify a specific question for LLM to focus on during summarization, instead of generating a generic summary?
👨‍💻
🤖

Yes, you can specify a specific question for LLM to focus on during summarization using the document summary index. You can customize the summary query to ask a specific question, and the index will generate a summary that answers that question. Here's an example code snippet:

```python
summary_query = "What are the sports teams in Toronto?"
doc_summary_index = GPTDocumentSummaryIndex.from_documents(summary_query=summary_query)
```

This will generate a summary that answers the question "What are the sports teams in Toronto?" when you query the document summary index.

----

Understood. In my use case, after querying the vector store, is it true that it will return the full documents ranked by relevance to the query? If I want to perform the map-reduce summarization strategy on the matched documents from vector store query, what should I do? For context, this is because in my use case the full ingested document, individually, usually exceed LLM's context length limit.
👨‍💻
🤖

Yes, after querying the vector store, it will return the full documents ranked by relevance to the query. To perform the map-reduce summarization strategy on the matched documents from the vector store query, you can use the GPTDocumentSummaryIndex. First, you can create a GPTVectorStoreIndex from your documents and then use it to create a query engine. Here's an example code snippet:

```python
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, GPTDocumentSummaryIndex

# Load your documents
documents = SimpleDirectoryReader('data').load_data()

# Create the index
index = GPTVectorStoreIndex.from_documents(documents)

# Create the query engine
query_engine = index.as_query_engine()

# Query the engine
response = query_engine.query("What did the author do during his time at YC?")

# Get the matched documents
matched_documents = response.get_matched_documents()

# Create the document summary index
summary_query = "What are the main points of the document?"
doc_summary_index = GPTDocumentSummaryIndex.from_documents(matched_documents, summary_query=summary_query)

# Summarize the documents
summaries = doc_summary_index.summarize_documents()

# Do map-reduce on the summaries
reduced_summary = map_reduce(summaries)
```

This will return a reduced summary of the matched documents from the vector store query. Note that you may need to install additional dependencies for the GPTDocumentSummaryIndex to work properly, and you will need to define your own map-reduce function to summarize the documents.

----
Ok, one last question. Is it correct to say that while the map reduce document summarization strategy can summarize a document to overcome the context length limit problem, it comes at the cost of latency because many calls to LLM would be needed? (Assume LLM call is relatively expensive)

Yes, it is correct to say that while the map-reduce document summarization strategy can summarize a document to overcome the context length limit problem, it comes at the cost of latency because many calls to LLM would be needed. Each call to LLM can be relatively expensive, so performing multiple calls for each document can increase the overall latency of the summarization process. However, this approach can still be useful for summarizing long documents that exceed LLM's context length limit.


----

https://gpt-index.readthedocs.io/en/latest/how_to/integrations/vector_stores.html
https://gpt-index.readthedocs.io/en/latest/use_cases/queries.html
https://gpt-index.readthedocs.io/en/latest/examples/index_structs/doc_summary/DocSummary.html
https://gpt-index.readthedocs.io/en/latest/how_to/index_structs/vector_store_guide.html


https://gpt-index.readthedocs.io/en/latest/examples/index_structs/doc_summary/DocSummary.html
https://gpt-index.readthedocs.io/en/latest/use_cases/queries.html
https://gpt-index.readthedocs.io/en/latest/examples/query_engine/JointQASummary.html
https://gpt-index.readthedocs.io/en/latest/examples/query_engine/sub_question_query_engine.html


https://gpt-index.readthedocs.io/en/latest/examples/data_connectors/WebPageDemo.html
https://gpt-index.readthedocs.io/en/latest/how_to/data_connectors.html
https://gpt-index.readthedocs.io/en/latest/guides/tutorials/fullstack_app_guide.html
https://gpt-index.readthedocs.io/en/latest/examples/data_connectors/NotionDemo.html

https://gpt-index.readthedocs.io/en/latest/how_to/data_connectors.html
https://gpt-index.readthedocs.io/en/latest/guides/primer/usage_pattern.html
https://gpt-index.readthedocs.io/en/latest/getting_started/starter_example.html
https://gpt-index.readthedocs.io/en/latest/guides/tutorials/building_a_chatbot.html


https://gpt-index.readthedocs.io/en/latest/use_cases/queries.html
https://gpt-index.readthedocs.io/en/latest/guides/tutorials.html
https://gpt-index.readthedocs.io/en/latest/guides/tutorials/terms_definitions_tutorial.html
https://gpt-index.readthedocs.io/en/latest/examples/query_engine/CustomRetrievers.html


--

https://gpt-index.readthedocs.io/en/latest/how_to/analysis/cost_analysis.html
https://gpt-index.readthedocs.io/en/latest/examples/index_structs/doc_summary/DocSummary.html
https://gpt-index.readthedocs.io/en/latest/examples/query_engine/JointQASummary.html
https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html

--

Ar, ok, actually still have more question after thinking. Given the situation above, is it possible to turn around and do things like this instead: During initial ingest of documents crawled from website, instead of submitting the original, we perform summarization of each chunk of each document first, and submit a concatenation of the summaries as replacement of the original documents. Then later, vector store search can directly retrieve a condensed document for Q/A. Can this be done in llama-index?
👨‍💻
🤖

Yes, it is possible to perform summarization of each chunk of each document during initial ingest of documents crawled from a website, and submit a concatenation of the summaries as a replacement of the original documents. This can be done in LlamaIndex using the GPTDocumentSummaryIndex. After creating the summary index, you can use it to summarize each document chunk and concatenate the summaries. Then, you can create a GPTVectorStoreIndex from the concatenated summaries and use it for vector store search. This approach can help to reduce the size of the documents and improve the efficiency of the vector store search.

Was this response helpful?

Verified Sources:
1. gpt-index.readthedocs.io/en/latest/use_cases/queries.html
2. gpt-index.readthedocs.io/en/latest/examples/index_structs/doc_summary/DocSummary.html
3. gpt-index.readthedocs.io/en/latest/guides/tutorials/building_a_chatbot.html
4. gpt-index.readthedocs.io/en/latest/examples/query_engine/JointQASummary.html

--

Show me sample code snippet to use this approach, thanks.
👨‍💻
🤖

Here's a sample code snippet to use the map-reduce document summarization strategy in LlamaIndex:

```python
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, GPTDocumentSummaryIndex

# Load your documents
documents = SimpleDirectoryReader('data').load_data()

# Create the index
index = GPTVectorStoreIndex.from_documents(documents)

# Create the query engine
query_engine = index.as_query_engine()

# Query the engine
response = query_engine.query("What did the author do during his time at YC?")

# Get the matched documents
matched_documents = response.get_matched_documents()

# Create the document summary index with a specific question
summary_query = "What are the main points of the document?"
doc_summary_index = GPTDocumentSummaryIndex.from_documents(matched_documents, summary_query=summary_query)

# Summarize the documents
summaries = doc_summary_index.summarize_documents()

# Do map-reduce on the summaries
reduced_summary = map_reduce(summaries)
```

This code snippet loads the documents, creates a vector store index, queries the engine, gets the matched documents, creates a document summary index with a specific question, summarizes the documents, and does map-reduce on the summaries. Note that you will need to define your own map-reduce function to summarize the documents, and you may need to install additional dependencies for the GPTDocumentSummaryIndex to work properly.

Was this response helpful?

Verified Sources:
1. gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html
2. gpt-index.readthedocs.io/en/latest/examples/index_structs/doc_summary/DocSummary.html
3. gpt-index.readthedocs.io/en/latest/guides/tutorials/unified_query.html
4. gpt-index.readthedocs.io/en/latest/how_to/query/query_transformations.html

--

Compare the two approaches above: ingest, query, then summarize; versus summarize/condense, ingest, then query. What are their pros and cons?
👨‍💻
🤖

Both approaches have their pros and cons.

The first approach of ingest, query, then summarize allows for more flexibility in the summarization process, as you can customize the summary query for each query and summarize only the matched documents. However, this approach can be slower and more resource-intensive, as it requires multiple calls to LLM for each document.

The second approach of summarize/condense, ingest, then query can be faster and more efficient, as it reduces the size of the documents and allows for faster vector store search. However, this approach may not be as flexible, as the summarization process is done upfront and may not be customized for each query. Additionally, the quality of the summaries may not be as high as when using the first approach.

Ultimately, the choice between the two approaches depends on the specific use case and the trade-offs between flexibility and efficiency.

Was this response helpful?

Verified Sources:
1. gpt-index.readthedocs.io/en/latest/use_cases/queries.html
2. gpt-index.readthedocs.io/en/latest/guides/tutorials/unified_query.html
3. gpt-index.readthedocs.io/en/latest/how_to/query/query_transformations.html
4. gpt-index.readthedocs.io/en/latest/examples/index_structs/doc_summary/DocSummary.html

--

Thanks a lot for your help! That's all for today :)
👨‍💻
🤖

Glad to be of help! If you have any more questions in the future, don't hesitate to ask. Have a great day!

Was this response helpful?

Verified Sources:
1. gpt-index.readthedocs.io/en/latest/use_cases/queries.html
2. gpt-index.readthedocs.io/en/latest/guides/tutorials/sql_guide.html
3. gpt-index.readthedocs.io/en/latest/how_to/query/query_transformations.html
4. gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html

--


