### Instruction
User asked question: {{question}}

You have read a webpage part by part and made notes as shown in input section below. Synthesize a final answer to the user question based on your notes.

### Input
{% for item in snippets -%}
{{ item }}
{% endfor -%}

### Output
Answer: 
