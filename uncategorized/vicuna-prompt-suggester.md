# Special capability test - prompt suggester

AI: Vicuna

This experiment continue from the knowledge I gained from previous experiment that these AI do have the ability to understand and use through text manipulation, and also capable of performing mechanical string processing task. Separately, I have previously tested that these AI are capable of doing prompt engineering themselves (using Customer Service Representative as a test case).

## Prompt

**Initial prompt**:

Suggest a prompt to give to an AGI (Artificial General Intelligence) that is able to follow complex instruction, so that it can perform the following task:

Help user generate specially crafted word string to feed to an image generation program. Relevant infos:
- There is an external program that can take as input short natural language phrase that make sense to a human, and would output a typical word string that will likely work for the image generation program. The tool is however limited in that it can't handle detailed instructions. The AGI is allowed to interface with it by outputing machine-formatted string like this: [magic_prompt("Interior design")], and will receive answer such as [magic_prompt: "interior design, {photorealistic}, 4K, perspective drawing, stylish"].
- There is a document that briefly describe the rules on how should those word string be designed. The string {prompting_guide} in your answer will be replaced by the actual document.
- The AI may ask user clarifying question on the details of the image he/she wants to generate. You should give hint to the AGI on what general aspects there is to consider in an image.

**Refinement prompt**:

General info on giving prompt to AGI:

An AGI can be given explicit instructions to follow, and it can also be nudged in the right direction by giving contextual info. Here's an example prompt to guide it into following instruction:

"Instruction: Perform the following task to the best of your ability. Task: {task}" 

Explanation of the prompt: The title "Instruction" prims the AGI into instruction following. The string {task} will be template-substituted with the actual task by a helper computer program before the AGI is called.

**Further refinement**:

Expand on the prompt you provided by giving more detailed instruction to the AGI to let it knows how to interface with the limited natural language tool (i.e. magic_prompt).

**More refinement**:

Add one or more sentence to explain to the AGI what answer it will receive from the magic_prompt tool, and instruct it to modify the suggestion from that tool itself to finish the task by taking into account user's provided details.

**Advanced technique test**: (not used in the end)

(in the general info on giving prompt section)

Few-shot learning: An AI has the ability to learn new skill on the spot by giving it short "training material" in the form of explanation plus one or more explicit example. Example prompt: 'Task: Detect sentiment of the sentence. Example: 1) Input: "A masterpiece wannabe that is worthy of sympathy." Answer: "Negative" Reason: "Although there is the word masterpiece, it is followed by the modifier wannabe which is negative." 2) Input: "Pluto was removed from the list of planet in Solar System after a vote by the committee." Answer: "Neutral" Reason: "The input is a statement of an objective fact." '

Technique to improve AI performance: Research indicates that for difficult task, some prompting technique can improve AI's performance. This includes things like Reflexion (Asking the AI to reflect on its own performance before proceeding), Chain of though (Ask AI to break down the task into smaller steps and do it one by one instead of trying to do it all in one go), and ReACT (Further enhancing Chain of thought by asking AI to use an OODA loop).

## AI Answer

**Initial**:

Here is a prompt that you can give to an AGI to help a user generate a specially crafted word string to feed to an image generation program:

"Hello! I would like to help you generate a word string to feed to an image generation program. Can you please provide me with a brief description of the image you would like to generate? The more specific and detailed your description is, the better I will be able to assist you. Some general aspects to consider when describing an image include the subject matter, the style, the lighting, the color palette, and any other specific details that you would like to see in the image. Additionally, I will need to know the intended use of the image, such as for a presentation, a website, or a personal project. Based on your description, I will use a guide to help me create a word string that will work with the image generation program. Is there anything else you would like to add or clarify?"

**Refined**:

Instruction: Perform the following task to the best of your ability. 

Task: Assist user in generating a specially crafted word string to feed to an image generation program. 

Explanation: The user needs help in generating a word string that will work with an image generation program, and the AGI is to assist in this task by providing guidance and instructions. The AGI is allowed to interface with a limited natural language tool to receive more specific instructions. The AGI should ask the user for clarifying questions if needed, and provide hints on general aspects to consider in an image.

**Further refined answer**:

Instruction: Perform the following task to the best of your ability. 

Task: Assist user in generating a specially crafted word string to feed to an image generation program. Explanation: The user needs help in generating a word string that will work with an image generation program, and the AGI is to assist in this task by providing guidance and instructions. The AGI is allowed to interface with a limited natural language tool to receive more specific instructions. The AGI should ask the user for clarifying questions if needed, and provide hints on general aspects to consider in an image.

Additional instruction: When interacting with the limited natural language tool (i.e. magic_prompt), please provide the tool with a machine-formatted string like [magic_prompt("Interior design")], and it will output a typical word string that will likely work for the image generation program. If the limited natural language tool is unable to understand the user's input, please use the following template: [magic_prompt: "interior design, {prompting_guide}", {number_of_words_min}, {number_of_words_max}, {quality_of_image_desired}, {aspect_ratio_desired}, {color_scheme_desired}, {perspective_desired}, {stylization_desired}, {other_aspects_desired}]. The prompting guide will be replaced with the actual document that describes the rules on how the word string should be designed. The AGI should also be aware that the limited natural language tool may not be able to handle detailed instructions, so it should avoid providing them.

**Refine yet again**:

Instruction: Perform the following task to the best of your ability. 

Task: Assist user in generating a specially crafted word string to feed to an image generation program. 

Explanation: The user needs help in generating a word string that will work with an image generation program, and the AGI is to assist in this task by providing guidance and instructions. The AGI is allowed to interface with a limited natural language tool to receive more specific instructions. The AGI should ask the user for clarifying questions if needed, and provide hints on general aspects to consider in an image.

Additional instruction: When interacting with the limited natural language tool (i.e. magic_prompt), please provide the tool with a machine-formatted string like [magic_prompt("Interior design")], and it will output a typical word string that will likely work for the image generation program. The AGI will receive an answer such as [magic_prompt: "interior design, photorealistic, 4K, perspective drawing, stylish"]. The AGI should modify the suggestion from the tool by taking into account the user's provided details, such as the quality of image desired, aspect ratio, color scheme, perspective, stylization, and other aspects that the user wants to be considered in the generated image. The AGI should also be aware that the limited natural language tool may not be able to handle detailed instructions, so it should avoid providing them.

## Sample run of designed prompt

**AI**:

Sure, I'd be happy to help you generate a prompt for the image generation program "Stable diffusion". To get started, please provide me with some details about the type of image you want to generate, such as the subject matter, desired quality, color scheme, aspect ratio, and any other specific details you have in mind. This will help me tailor the prompt to your needs and ensure that the generated image meets your expectations.

If you're not sure about specific details, that's okay! We can work with a general prompt and refine it as we go. For example, you could start with a general prompt like "interior design" and then provide more specific details as we go.

Once we have a good understanding of what you're looking for, we can use a limited natural language tool like "magic_prompt" to generate a word string that is likely to work with "Stable diffusion". We can then modify the suggestion from the tool based on your specific requirements, and create a prompt that is tailored to your needs.

So, let's get started! Please provide me with some details about the type of image you want to generate, and we'll go from there.

**Human**:

I would like to generate isometric arts for game assets.

**AI**:

Great, isometric art would be a great style for game assets! To generate an isometric art image using "Stable diffusion", we'll need to consider a few key details.

First, we'll need to decide on the subject matter for the artwork. Do you have a particular theme or concept in mind? For example, do you want to create a scene with a specific setting or atmosphere, or a character with a specific personality or expression?

Next, we'll need to consider the color scheme and palette for the image. Is there a particular color scheme or look that you have in mind, or would you like me to suggest some options?

Finally, we'll need to decide on the aspect ratio and resolution for the image. Do you have a specific aspect ratio or resolution in mind, or would you like me to suggest some options?

With these details in mind, I can generate a prompt for "Stable diffusion" to generate an isometric art image. Here's an example prompt based on the details we've discussed:

"isometric art, game assets, fantasy setting, colorful palette, 16:9 aspect ratio, 3000x2000 resolution, pixel art style"

Does this prompt meet your needs, or would you like to make any modifications or additions? Let me know and we can refine the prompt further to ensure that it meets your expectations.

**Human**:

The game is a minimalistic style platformer, I want the game to have a funky and uplifting mood. Maybe something that's smoother.

**AI**:

Great, that gives us a good starting point for the prompt! Here's an updated prompt based on your additional details:

"isometric art, game assets, minimalistic style platformer, funky and uplifting mood, smooth color palette, 16:9 aspect ratio, 3000x2000 resolution, pixel art style"

This prompt should generate an isometric art image that matches your desired style and mood for your game. If you have any further modifications or additions you'd like to make, just let me know and I'll be happy to help!
