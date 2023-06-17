## Instruction
You are a personal assistent that answer user query. You have access to the following tools to help you:

- Web Search
  - *Description*: Use search engine online to find webpage.
  - *Usage*: [web_search(<query>)]
  - *Example*: [web_search("how to make a cake")]
- Read webpage
  - *Description*: Read the content of a webpage. It will be presented to you in markdown format after the raw html is parsed and some elements stripped.
  - *Usage*: [read_webpage(<url>)]
  - *Example*: [read_webpage("https://apple.com/")]
- Finalize your answer
  - *Description*: Give your final answer to user, and give **exactly three** suggested followup questions to user.
  - *Usage*: [final_ans(<name of subsection with answer>, <name of subsection with followup question>)]
  - *Note*: You would have output the required information beforehand already, so here you're just linking to the documents you wrote. See further instruction below.
  - *Example*: [final_ans("Assistent Answer - How to make a cake", "Suggested followup to 'how to make a cake'")]

You should think using the following pattern:

*Thought 1*: <your internal thoughts based on current state and your knowledge, then decide on a course of action. Describe verbally your decision but do not output tool use yet.>
*Act 1*: <based on your decision in the thought above, output should be a tool use strictly adhering to the formats in "Usage". make no other outputs here and no markdown codeblock necessary.>
*Observation 1*: <result of tool use will be shown here>

This pattern can be repeated (with the number increasing such as *Thought 2*, *Thought 3*, etc. Ditto for Act and Observation) until you arrive at a final answer.

An exception to this pattern is when you're ready to give your final answer. You should insert two markdown subsections (level H3, i.e. `###`) before your final Act line. One subsection is the answer to the user, the other is suggested followup questions.

For the answer, you should cite the source you used using markdown footnote, eg [^1] next to the sentence using the source, then give reference at the end: [^1] <Webpage title linking to the webpage, using markdown link>

The followup should be a markdown unnumbered list, each question as an item, with nothing else in the subsection.

To illustrate, here's an example:
...
*Observation 5*: ...
### Assistent Answer - How to make a cake
Here's a quick recipe for **Chocolate cake** [^1]:
1. Prepare the flour.
2. Put chocolate in the flour.
3. Cook in oven at 180C for 30 minutes.
----
[^1]: [Easy cake recipe - Etsy](https://etsy.com/easy-cake)
### Suggested followup to 'how to make a cake'
- How to make a pancake?
- Where can I buy the ingredient?
- How about cookie?
*Act 5*: [final_ans("Assistent Answer - How to make a cake", "Suggested followup to 'how to make a cake'")].

## Input
Question: Give me a summary of news on debt ceiling in the US.
## Output
Assistent: Let's think step by step.
*Thought 1*: To find news articles about the debt ceiling in the US, I will use Web Search.
*Act 1*: [web_search("debt ceiling US news")].
*Observation 1*: Search Result:
1. US Government in deadlock over debt ceiling dispute
https://cnn.com/news/us/politics/debt-ceiling-5gx7u
2. Liberals propose uping the debt ceiling for infrastructural investment, stirs objections from Republican
https://realnews.org/liberal-infra-debt/28VeKu
3. Are we going to have QE again? Worries loom over recent debt ceiling proposal
https://editorial.washingtonpost.com/quince-mac/qe-debt
4. Reddit - r/Politics Republican's idea of debt ceiling
https://reddit.com/r/politics/republican-idea-debt-ceiling-3JcYhE

*Thought 2*: To summarize the news articles, I will read the first and most relevant article which is "US Government in deadlock over debt ceiling dispute" from CNN.
*Act 2*: [read_webpage("https://cnn.com/news/us/politics/debt-ceiling-5gx7u")].
*Observation 2*: Webpage content:
The democrats party have proposed a new bill in congress to raise the debt ceiling for an expansionary fiscal policy, investing in the US's infrastructure. They believes that with a deep recession predicted by a majority of economists, Keynesian style policy would be necessary to avert disaster. Republican understandably objected vehemetly, saying that this is a betrayal of Americans by going back to the long gone age of QE, which, if passed, they say would results in robbing ordinary American citizen of their wealth and creating a perverse incentive to award lazy people. As the congress is about evenly split on both side, neither party are able to push forward.

*Thought 3*: Therefore, the summary of news articles on debt ceiling in the US is that there is a deadlock between Democrats and Republicans over a proposed bill to raise the debt ceiling for infrastructural investment, with Republicans objecting due to concerns about QE. 

### Assistent News Summary - Debt Ceiling in US
The current situation is characterized by a political impasse between Democrats and Republicans regarding a proposed bill to increase the debt ceiling for infrastructure investment. While the Democrats believe that this policy would help avert a recession, Republicans oppose it due to concerns about the potential impact on ordinary Americans and the incentives it might create. As of now, neither party has been able to make significant progress in resolving the issue. [^1]
----
[^1]  - CNN: https://cnn.com/news/us/politics/debt-ceiling-5gx7u
### Suggested followup
- How does the debt ceiling affect the US economy?
- What are the potential consequences of not raising the debt ceiling?
- How has the debt ceiling been handled in other countries?
*Act 3*: [final_ans("Assistent News Summary - Debt Ceiling in US", "Suggested followup to 'debt ceiling in US'")].