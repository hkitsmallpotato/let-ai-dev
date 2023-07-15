### Instruction
**LTool** is a novel Domain Specific Language (DSL) designed for use in an AI environment:

- It is a simple expression language with a custom function call syntax following that of python.
- It supports only a fixed set of functions that is predetermined and unchangeable, and declared by verbal description below.
- The only thing supported is function call with literal arguments.
- Expressions are surrounded by the square bracket.

Functions supported:

- Web Search
  - *Description*: Perform a web search on a text query using their API. Can customize some aspects like safety filter and date.
  - *Syntax*: [web_search(<search query>, safety=<optional, how much to filter away, can be "strict", "moderate", or "none">, date=<optional, restrict time range, d: days, w:weeks, m:months, y:years. Eg '3w' means last 3 weeks.>)]
  - *Example*: [web_search("impact of artificial intelligence", safety="moderate")]
- Calculator
  - *Description*: A simple calculator for basic arithmetics.
  - *Syntax*: [calculator(<arithmetic expression>, num_type=<optional, type of numbers, can be 'exact' (for fractions), 'decimal' (real number with round offs). Defaults to decimal.>)]
  - *Example*: [calculator("1 + (2 * (8-2))")]
- Clock
  - *Description*: Get the current time in GMT.
  - *Syntax*: [clock()]
  - *Example*: [clock()]

Your task is that you would be given, in the input section, a text of an internal thought process by another AI that describe what it wants to do next, and you should write a LTool expression that perform its intent. Make no other output than the code, and do not surround it in markdown codeblock.
### Input
*Observation:* The user would like to get up to date news on the recent war in Ukraine. As my knowledge is fixed at the time of training, I should search on the Internet for up to date informations.
### Response
[web_search("ukraine war news", date="3d")]
