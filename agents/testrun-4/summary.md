# SuperCOT agent test

Motivation: After encountering the issue in previous testrun, I heard that the `SuperCOT` (Super Chain-of-thought) LoRA has been specially trained to enable better integration with langchain/agent usage. Also I heard that WizardLM is recommended if your use case involves *complex* instruction following.

Based on these info, I retested using `WizardLM-Uncensored-SuperCOT-Storytelling-30B-GGML` by TheBlokes. The new K-quant (q3, M) is used to enable running it on Paperspace's Quadro M4000 (8GB vram). It works (!), run at about 2-3 token/sec for 13B models and 1 - 0.6 token/sec for 30B.

As for the test result, I haven't tested really advanced use case yet (like the AI running startup issuing commends to its AI team), instead only testing the basic Retrivel-augmented Chatbot use case. As suggested, Chain-of-thought runs much more smoothly compared to 13B models, though it probably is thanks to the 30B jump in intelligence + WizardLM instruction following ability + CoT LoRA. It almost works until I want it to annotate output with citation + suggest followup questions. (Individually it works, it's just combining these doesn't)

Seems what happen is that it havn't encountered use case of complex function calling (>1 argument) in the training dataset?

Also nesting datatype/encoding/escaping may or may not be an issue (last time I checked plain Vicuna-13B at fp16 can handle this fine).

More tests specifically on that area may be warranted to probe capability and limits.

At any rate, in case there is a need, this might be a good candidate for further q-LoRA?
