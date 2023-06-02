# Appendix: Human simulated agent output

## System output
You performed web search in "artificial intelligence", "machine learning", "neural network", "deep learning" last round. After browsing through the top hits and having another assistent AI summarize it, here's a report:

The rate of progress in AI is explosive in the last 6 months, due to the stable diffusion (a model to generate image from text prompt) revolution first, and then later, ChatGPT (a model in the Large Language Model/LLM family), and a long list of rapid developments in an extremely short time span. Both of them are under an emerging trend known as "generative AI". Whereas previous neural network based AI are about detection, and performing narrow-domain tasks, these new AI give promise for the ability to generates new artifacts at a near human level, and is getting somewhat close to the idea of general intelligence. There have however been concerned expressed about the potential impact of misuse, such as misinformation, tyranny, job loss, and existential risk.

----

## System output
You asked assistent to read up about recent industry trend in generative AI and to understand its potential impact on society. Assistent report:

Generative AI has the potential to be broadly applicable to all sectors in society to automate job. Some of the trends include:
- Augmentation with tools: Large language model (LLM) have specific weaknesses in areas like keeping up to date with new knowledge, memories, mathematics, etc. These can be addressed by leveraging its in-context learning ability and ability to give structured output to integrate with external tools, such as web search, vector database for memories and information retrieval, and Wolfram alpha.
- Deep integration into workflow: By integrating them tightly with existing platforms, they can provide new user experience previously impossible, such as Github CopilotX for coding assistence, Microsoft Copilot that integrate LLM with Window OS, Google's new product to integrate LLM with docs, slides, sheets, etc so that user can use natural language commands to generate full working documents.
- Prompt engineering: LLM can be flexibly, and cheaply, instructed to perform a wide spectrum of tasks simply by giving it natural language commands instead of having to do expensive training. This open it up to non-technical people. However "prompting" LLM correctly is a new skill.
- Impact on Artists: with the stable diffusion ecosystem maturing with plenty of customizations (LoRa), controlnet, and segment anything (SAM) by meta, arts are no longer something only people with skill can do. For example, Adobe is integrating these AI into their product with features such as out-painting to auto-extend a picture, or ability to generate a new object in a photo.
- Multimodality and robotics - although it is early, experiments have shown promises on making LLM able to interact with medias other than text (eg image), and it can then be used to control a robots to perform task. Humanoid robots is a holy grail that gain renewed interests.

----

## System output
You performed web search on "generative AI research", "recent advancements in machine learning", or "current trends in natural language processing" last round. An assistant AI have summarized the results with this report:

*Generative AI research*:
- Multimodality is a focus area - the ability for LLM to interact with more than text (like image) would open up further applications such as integrations with robotics. Moreover, according to the embodied intelligence hypothesis, letting LLM interact with the world physically is an important path to obtain training data that guide it towards AGI (Artificial General Intelligence).
- Longer context length limit - a major limit of LLM today is that they can only work on a short length of text at a time with no memories outside (eg 2048 tokens, 1 token is about 0.75 words). This is due to the qudratic bottleneck of the attention layer in the neural network. Many subquadratic attention replacement have been proposed, but it remains to be seen which one is actually feasible at the extreme scale of GPT3 or above.
- STEM and coding ability - one of the very few areas where LLM is obviously weak when evaluated by humans.

*Trend in NLP*:
- replacing previous generation NLP models such as BERT or task-specific models with universal one that uses LLM + in-context learning to achieve SOTA (State of the art) results on standard tasks such as named entity recognition, sentiment analysis, etc.

----

## System output
You perfomed research on multimodality and embodied intelligence hypothesis last round. Another assistent AI made this report:

What is the embodied intelligence hypothesis: A hypothesis that human intelligence is attributed to the fact that they are *embodied* - a mind living inside a body, with the daily interaction with the world giving the mind feedback and training data based on multi-sensory inputs. This is in contrast to previous ideas that intelligence is isolated, or stand alone, and can theoretically be obtained simply by infusing sufficient capabilities such as reasoning, planning, etc.

Implication: Multi-modality is important as it is a critical element of the attempt to achieve AGI (Artificial General Intelligence).
What is multi-modality: The ability for LLM to interact with more media than text such as image.

Recent advances:
- A team have cheaply replicated the GPT4 multimodality feature in open models simply by stitching an open LLM model with a vision model (CLIP) with a single linear layer, and then perform training with both networks freezed.
- Google have experiments with integrating LLM with robotics - sensory inputs are given to the LLM, LLM is given natural language command of an objective, and it describe its plan and action which is picked up and executed by the (embodying) robot.

