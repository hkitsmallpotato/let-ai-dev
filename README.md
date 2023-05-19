# let-ai-dev

This repo hosts some raw and cleaned up data for an experiment to use open source LLM to do end-to-end Software Development.

## AI used

- Vicuna-13b v1.1 (general purpose, was SOTA in the open source space until recently)
- MPT-7b-Chat (features ability to have longer/soft context length limit due to using AliBi instead of positional embedding)
- StarChat (intruct fine-tuned from StarCoderBase, specialized on coding)

## Method

Simple role-playing prompt is used to prim the AI. A partially standardized Input/Output mechanism is provided, where documents from previous stage of Software Development is provided with a brief description of what it is, and it is asked to perform a list of tasks outputing some documents.

Prompts are sometimes surrounded with special instruction asking it to read but hold on doing any work until user say a specified phrase, to overcome UI limit that may accidentally truncate user input.

In some of the tasks, additional background information or user preference is also attached.

## Files

- root directory: `{ai-name}-{topic}-{phase}.md` Data of asking AI to do first 2 phase in SDLC (requirement analysis and system architecture)
- `/uncategorized` Misc. and advanced tests
- `code/others` Coding tasks that are not part of a full SDLC/full project
- `code/frontend` and `code/backend` - Try to extend to the test to actual implementation

## Preliminary Results

They are generally able to give a rough draft of the requested documents, although the attention to details may be disappointing. It is also found that although injecting user preference/background info do tilt the AI to a desired direction, it also sometimes interfere negatively with the AI's pre-existing knowledge resulting in output where the AI seems to have fundamental misunderstanding about basic concepts.

On low level design and coding ability, Vicuna-13b v1.0 already have some capability on that front, however it completely falls apart once some rather low "difficulty threshold" is reached, especially on algorithmic tasks. The author however observe that this part seems to have visibly improved somewhat on the v1.1 update. It also have troubles with knowledge cut-off and perhaps breath of knowledge of specific software libraries, but this is perhaps not Vicuna's flaw specifically and more an infrastructural limit of existing LLM. 13b Model also tends to be slower performance-wise, which can be an issue for the impatient.

StarChat are also able to do design work aside from coding, and is rather fast. However it currently suffer from a major weakness that the instruction-tuning quality/strength is not good enough (due to it relying on dolly and open assistent, which also have similar issues). As other people have observed, they have a tendency to ignore user instruction and do its own thing, especially from turn 2 of a conversation onward. It also often say it can't do something (even for a straightforward coding task with no moral controversy) because eg it doesn't understand what task is there or that it doesn't understand the context/detail enough. Generally speaking it seems to be highly sensitive to the exact wording used and sometimes one or two word in a long paragraph is the offender there. Advantage compared to Vicuna seems to be that it knows more libraries/obscure language etc. (Not sure about the knowledge cut-off date)

Another limitation that is not the AI's fault but again an infrastrutural limit is that the short context length limit means that while we can use them to quickly generate a scaffold for a software project from nothing, trying to *modify* existing software still seems to be out of the question mostly. For this MPT's use of AliBi is an encouraging sign, however the quadratic performance bottleneck is still there and the slowdown may become untolerable once the conversation goes on for a while.

## Other things

**Other tests performed**:

We also tried to test these AI on a variety of misc. tasks, some of them are:

- General webdev problem (eg authentication, multi-tenancy, file upload, HTML5 collaborative editing)
- Meta level "capability amplification" test (or really, just prompt engineering?)

**Static compilation of agent workflow**:

One way to use these powerful AI is to agentize them and put them into a loop to analyze goal, come up with an action plan, then execute it (AutoGPT/Autonomous Agent etc). It is observed that they often get derailed/spin in a loop without making forward progress.

One possible perspective to look at the set of prompt we designed is that it is a human crafted, "statically compiled" action plan to replace having the AI trying to give the next step dynamically/on-the-spot by analysing the situation.

**Future improvement**:

The set of prompts I designed right now is still pretty rough. I also found out the order of task seems "wrong" to the AI's eye and so it ignored some of the task, especially those around various diagram to analyse use case.

As I am in a rush, I just skipped some of those tasks, perhaps resulting in incomplete requirement doc to downstream which may affect their quality.
