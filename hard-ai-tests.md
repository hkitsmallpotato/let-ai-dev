# (Hard test) Ask AI to do undergrad CS project

- Some of the "harder" test I have is to give a very small snippet of a typical undergrad CS course project to AI and see what they can do:
  - Re-implementing toy version of RDBMS from ground-up
  - Re-implementing a deep learning library
- I usually phrase it in a "tutorial for human" way - ask it to write a tutorial to teach these topics.
- Specific part I tests:
  - RDBMS: first phase of query planner: convert SQL into relational algebra expression
  - Deep learning library: computational graph and automatic differentiation

So far the results is that 13B just can't do it. Vicuna-13B can slightly get close to the goal if you test extensively and give the right prompt, but otherwise no.

So when Guanaco come out and there's an online demo for 33B (or 30B?), I give it a quick shot. Here's the result:

## Guanaco-33B on SQL to relational algebra query planner

*Question*:

Write a deep dive tutorial on reimplementing a toy version of RDBMS. Write the section for the query translator whose job is to convert SQL to relational algebra expression. Begin with code that can only handle simple SQL on a single table of the form “SELECT … FROM mytable WHERE …”. No sorting/pagination is needed. Use python, and you may assume the SQL is already parsed into AST (Abstract syntax tree). The output should also be AST of relational algebra.

*Answer*:

Here’s a deep dive tutorial on re-implementing a toy version of a Relational Database Management System (RDBMS) using Python, focusing on the Query Translator component which converts Structured Query Language (SQL) queries to relational algebra expressions. We will start by handling a basic SELECT query over a single table without any sort or pagination requirements.

The first step in implementing our Query Translator is to parse the input SQL statement into an Abstract Syntax Tree (AST), which represents the logical structure of the query. This can be done using a parser generator like PLY or Pyparsing. Once we have the AST, we can traverse it to extract information about the tables involved in the query and the columns being selected.

Once we have extracted the necessary information from the SQL query, we can begin converting it to a relational algebra expression. In this case, we are dealing with a simple SELECT query, so the translation process will be fairly straightforward.

The basic idea behind the conversion is to represent each table as a relation, and then apply operators such as selection, projection, and join to these relations to obtain the final result. Let’s look at how we can translate each part of the SELECT query to a corresponding relational algebra expression.

- Selection: The selection clause specifies which columns to include in the result. We can implement this by projecting the relevant columns onto the resulting relation. For example, if the SQL query is SELECT col1, col2 FROM mytable, we can create a new relation consisting of two attributes - col1 and col2 - by projecting them onto the original relation.
- Projection: Projection simply involves selecting specific values from a relation based on some condition. In our case, we need to check whether the value of the specified column matches the given predicate. To do this, we can use a conditional operator called the selection function, which takes a boolean expression as its argument and returns either true or false depending on the outcome of the evaluation.
- Join: Joins combine data from multiple relations to produce a new set of tuples that satisfy certain conditions. There are several types of joins, but in this case, we’ll focus on the inner join, which selects matching tuples from both relations. Implementing an inner join requires us to ensure that there is no duplicate data in the joined result. One way to achieve this is through the use of a hash table, where we store all the unique tuples seen so far and eliminate duplicates during the joining process.

Here’s an example implementation of the above steps in Python:
```python
import ast
from collections import defaultdict

def parse_sql(query):
    """Parse the given SQL query into an AST."""
    # Implementation of the parser here
    
    return ast.parse(query)

def get_tables(ast):
    """Extract the list of tables mentioned in the query."""
    tables = []
    for node in ast.body:
        if isinstance(node, ast.Table):
            tables.append(node.name)
    return tables

def get_columns(ast):
    """Extract the list of columns mentioned in the query."""
    columns = []
    for node in ast.body:
        if isinstance(node, ast.Column):
            columns.append((node.name, node.type))
    return columns

def translate_select(ast):
    """Translate a SELECT query to a relational algebra expression."""
    tables = get_tables(ast)
    columns = get_columns(ast)
    
    # Extract the selection predicates
    selections = {}
    for node in ast.where:
        left, right = node.left, node.comparison_op, node.right
        selections[left] = {col: val for col, _ in columns if isinstance(col, str)}
        
    # Create a new relation for each table
    relations = [defaultdict(list) for tbl in tables]
    for row in ast.result_fields:
        cols = [(c, v) for c, _ in columns if isinstance(c, int)]
        tuple = dict(cols)
        for tbl, attrs in zip(tables, row.names):
            relations[tbl][tuple] = tuple([attrs])
            
    # Project the desired columns
    projections = [{}] * len(relations)
    for col, sel in selections.items():
        for tbl, attrs in zip(tables, row.names):
            projections[tbl].update({k: v for k, v in attrs if k in sel})
                
    # Apply the selection function to filter out unwanted rows
    filtered_rows = []
    for tbl, attrs in zip(tables, row.names):
        filtered_rows += [tuple(v) for tuple, v in relations[tbl].iteritems() if eval(selections[tbl], locals(), v)]
    
    # Perform the inner join
    joined_tuples = []
    for t1, t2 in itertools.product(*filtered_rows):
        if not set(t1) & set(t2):
            joined_tuples.append(tuple(sorted(set().union(*filtered_rows))))
    return joined_tuples

if __name__ == '__main__':
    sql = 'SELECT col1, col3 FROM mytable WHERE col2 > 5 AND col4 < 10'
    ast = parse_sql(sql)
    results = translate_select(ast)
    print('Query Result:', results)
```

In this example, we define a parse_sql function that parses the input SQL query into an AST object. Next, we define get_tables and get_columns functions that extract

