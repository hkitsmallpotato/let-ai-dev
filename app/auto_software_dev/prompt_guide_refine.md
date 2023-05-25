### Task
The input below shows a guide to scaffold some webapp. Collect the commands mentioned in the guide into a separate shell script the user can use for automation. Show the source code of your constructed shell script only and nothing else.

### Example
Suppose the guide says:
1. Generate a new project:
```
npm init hello-world
```
2. Install express:
```
npm install express
```
3. Create a file main.js
```js
const express = require("express")
const app = express()
const port = 3000

app.get('/', (req, res) => {{
    res.send('Hello world!')
}})

app.listen(port, () => {{ console.log('Listening on ${{port}}') }})
```
4. Start the server
```
node main.js
```

Then your output should be:
#!/bin/sh
npm init hello-world
npm install express
node main.js

Note that we do not create the source file in the script as we assume for the purpose of this task that user is responsible for that.

### Input
{guide}
### Output

