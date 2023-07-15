# Using Dual LLM Pattern to overcome Agentization difficulties

## Background

Previously, it is widely known that Open source LLM have significant difficulties in being agentized as they are unable to reliably make output in structured format according to user specifications. This become a barrier to automation as the usual workflow is that these LLM make very strictly structured output, which can then be parsed programmatically to trigger downstream actions.

In the worst case, these LLM simply refuse to comply even with extensive prompt engineering, often derailing in creative and hard to control manner.

As a result, the recommendation is to use external means of control, such as the Microsoft guidance library.

## Discovery

More recently, there are people who seem to have succeeded in using Open source LLM for agent use case, and they did so using the programming specialized `WizardCoder` model, which they find to be better able to follow these kind of instructions.

## Idea

This then triggered my thought with an interesting idea...

Maybe the reason for the failure so far, is that "Structured output" is really just another word for **"programming task in a Domain Specific Language (DSL)"**. Although these general purpose LLM can still do programming to some extent, they are not as good as specialized models. And then I recall having done some special capability test on our old Vicuna, who is able to do In-Context Learning and acquire the ability to program in a novel DSL specified in the prompt immediately. So, if that's the case, why not just let each LLM work on their own area of strength/expertise?

So here's the plan to attack this problem again:
- General purpose LLM is still responsible for the main ReACT/Chain of thought (CoT) loop, but now the requirement for action is relaxed - they are only asked to verbally describe what they would do.
- Then we feed the verbal action output to `WizardCoder`, and give it just the task to transform it into the structured format.
  - With the insight above, we deliberately frame the task as a DSL programming problem, and "invent" our own DSL on the spot. Presumably this help put it into the right programming mindset.

## Result

- Calling tool use with multiple argument: One take pass
- Using code interpreter: Need some iterating on the prompt, and nudge in the first word/sentence of response is necessary, but it works.
- Annotating an answer with custom citation format: This used to be the hardest task that seemed impossible (I exhausted all methods without fine-tuning and nothing worked before). Now it is still hard, but I finally got it working somewhat, after adding example solution walkthrough, explain what concrete steps it need to take, and then to apply Chain of Thought to `WizardCoder` itself (!)

All in all, the above should make retriveal augmented chatbot that basically copy Bing, possible in principle with current Open Source LLM (though more experimentations may be needed to refine the prompt and ensure robustness).
