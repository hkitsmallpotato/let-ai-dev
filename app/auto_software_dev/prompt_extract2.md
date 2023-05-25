### Task
Extract source code of all files mentioned in the guide below on scaffolding a new project, and pack them into a machine readable string, which should be a syntactically valid JSON in compact form. The format must be a list of file object, one entry for each source file extracted from the guide. A file object contain attribute "name", value is filename with path relative from project base, and "content", value is content of the file properly escaped. For this task you must also consider the shell script file provided after the guide to be one of the source file. Be faithful to the guide and do not inject your own enhancement except for the purpose of ensuring the guide work as intended, also try to be concise. Do not output anything other than the JSON requested.
### Example Output
This is syntactically valid:
[{{"name":"a.txt","content":"foo"}},{{"name":"b.txt","content":"bar"}}]
But this is incorrect as the top level of JSON is not a list:
{{"files":[{{"name":"c.txt","content":"baz"}}]}}
### Input
Guide:
{guide}
Additional shell script:
{script}
### Output
