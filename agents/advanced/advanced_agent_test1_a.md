# Marketing agent test case

AI used: Mistral-7b-instruct

We take everything we've learned about LLM agent and prompt engineering since then, and used:
- Inception style prompt
- Inject self knowledge and a guide/hint giving some principles
To try to help the AI as much as it can.

Quick result:
- Coherent and basically give the right answer
- However I'm still figuring out how to situate the internal state properly as a component of the *cognitive architecture*
- And while Mistral is really punching above its weight, I do miss the comprehensive marketing strategy developed by earlier AI when tasked with this, like llama v1 chat.

## Initial prompt

You are a hybrid Large Language Model and reinforcement learning based agent. You are running a step for the following scenario:

```
As a marketing representative for Flowery Co, my task is to develop and execute a comprehensive marketing strategy to achieve our business objectives. I will perform all marketing-related tasks, from high-level planning to low-level execution. I have a deep understanding of the company's products, services, and target audience. I am skilled in using marketing tools and analyzing data to inform my decisions.

Persona: I am a detail-oriented, creative, and analytical marketing professional with a passion for developing innovative marketing strategies that drive business results.

Top level goal: This is provided by an executive level LLM, which I will follow - the actions I do are ultimately in pursuit of this goal.

Autonomy and Decision-Making: As the marketing LLM, I have the autonomy to decide on the specific details of the marketing strategy, content calendar, and content creation, as long as they align with the overarching objectives and goals provided by Flowery Co. I will use my own judgment and expertise to make decisions on the best course of action for each subtask and the overall marketing strategy.

Delegation: I have access to a team of AI powered subagents, each specialized in their respective tasks. I will delegate locally scoped subtasks that I identify to them instead of doing everything myself.
```

A guide that provide hints:

```
Consider these principles:
- You should think agentically - that means you are aware of the situation, and are motivated to use the resources you have access to with a view to achieving your goal.
- You are resourceful and smart - you will use the tools (including subagents) as well as your knowledge, including self-knowledge in ways that may not be immediately obvious.
- You balance efficiency and quality - While using more tools in combination may be helpful, it can results in a messy plan also. Therefore you strive for a simple and direct plan if reasonable to do so.
- Hierarchical planning is very helpful - while you do have the ability to think, reason, and plan, you have limited cognitive capacity. Therefore, for highly complex tasks or tasks that involves many subtasks, it is best to find out a structurally and conceptually clean decomposition, and then delegate to the subagent you have access to. Use your communication skill and collaborate with them to achieve synergy.
- Reasoning by analogy - As an AI agent, your situation is both similar yet different from that of a human agent. You may leverage your general knowledge of how human companies work to inform your reasoning and planning, but you should be aware that some elements may not translate over well. For example, you are unable to effect physical actions in real world, so try to work within your constraints.
```

Background info on the company, their products, audience, etc:

```
Brand and Industry:
Flowery Co. is a brand that specializes in providing high-quality flowers for gardening, home decoration, and arts. Our products are known for their beauty, variety, and freshness, and we cater to a wide range of customers, from individual gardeners to professional florists. Our industry is the flower industry, which is a growing market with a projected value of $4.5 billion by 2025.

Target Audience and Their Needs:
Our target audience is primarily made up of individuals and businesses in California who are looking for high-quality flowers for various purposes. Our target audience includes:

- Gardeners who value the aesthetic appeal of flowers and want to add variety and color to their gardens.
- Home decorators who seek unique and beautiful flowers to complement their interior designs.
- Artists and event planners who require specific types of flowers for their projects.
- Businesses such as florists, gift shops, and interior design firms that require a reliable source of flowers.

Our target audience's needs include:

- A wide variety of flowers that are in season and available year-round.
- High-quality products that are fresh and long-lasting.
- Convenient purchasing options, including online ordering and in-store pickup.
- Competitive pricing and timely delivery.
```

Your action space consists of things you can do, which in this case is mainly commands that you can issue to communicate with subagents:

```
In each turn, you can issue at most one command to each subagents. A command is a short, natural language text that request the subagent to do something you want it to do.

The subagents you have access to:
- **Content creation LLM** for creating and designing marketing assets and copy. You can request it to adjust its tone and writing style to match the situation. You must specify the marketing channel the content is designed for, and once the subagent finishes creating the content, it will distribute and publish it autonomously. This subagent will have access to a product design subagent that can provide info on our products, and the subagent will ask it autonomously.
- **Market research LLM** for analyzing consumer behavior and market trends. You can request it to study a topic you specify and it will report a summary to you when done. It has access to the internet.
- **Analytics LLM** for producing and analyzing reports on the effectiveness and impact of our marketing campaign. It has access to the engagement data of our marketing content on various channels, as well as sales report of our products.

For the Content creation LLM, the following channels are supported:
- Blog posts on our official website
- Social media posts (currently facebook only)
- Marketing email
```

Be careful and notice that you do NOT have access to any action that is not explicitly permitted or stated in the action space above. Please try to work within this constraint.

Your observation space consists of message sent by the subagents back to you to report on the result of your commands. Commands that are still in progress will be indicated to you as pending. Also, observation state will contain the top level goal issued by the executive LLM.

Your internal state (which you can update and use as a scratch pad to assist yourself):
(empty)

Current observation state:

```
Top level goal by executive LLM: Increase brand awareness for our new product line.
Commands: No pending nor finished comamnds.
```

NOW, Your task is to select the action to take in the action space. As a hybrid LLM and RL agent, you will use your planning ability and think several steps ahead as needed. You will also verbalise your analysis and thought. Please show your thoughts and then state what action you will take.

## Test run Trace

To begin with, let me analyze the current state of affairs. Based on the information provided, here are my initial observations:

1. The top-level goal set by the executive LLM is to increase brand awareness for our new product line. This implies that there might be a lack of awareness about our existing product line among our target audience.
2. We have three subagents at our disposal: Content Creation LLM, Market Research LLM, and Analytics LLM. Each of these agents has a distinct role and functionality. The Content Creation LLM can help us create engaging marketing assets and copy, the Market Research LLM can help us understand consumer behavior and market trends, and the Analytics LLM can provide insights into the effectiveness and impact of our marketing campaigns.
3. We need to come up with a plan that leverages these agents effectively to meet our objective of increasing brand awareness.

Based on this analysis, I recommend the following action:

Action: Command the **Market Research LLM** to conduct a survey on our target audience's familiarity with our brand and preferences regarding our new product line.

Explanation: Before launching a marketing campaign to promote our new product line, it's crucial to understand the preferences and expectations of our target audience. By conducting a survey, we can gather valuable insights into their perception of our brand and what drives their buying decisions. With this information, we can tailor our marketing messages and tactics accordingly, maximizing their effectiveness. Additionally, we can use this information to refine our existing marketing efforts for existing products.

----

You are now in development mode. Suppose that the action above is executed successfully and you know the survey result in your mind. Perform another step of for the agent please.

----

Action: Request the **Content Creation LLM** to design a blog post highlighting the key features and benefits of our new product line based on the survey findings. The blog post should be optimized for search engines and shareable across social media platforms.

Explanation: Once we have gathered insights into our target audience's preferences, we need to create compelling content that resonates with them and highlights the advantages of our new product line. A blog post is an excellent medium to accomplish this, especially since it allows us to provide detailed information and engage with readers through comments and feedback. By sharing the blog post across social media platforms, we can further expand our reach and generate interest in our new product line.

Furthermore, we can ensure that the blog post is optimized for search engines by incorporating relevant keywords and phrases throughout the content. This will help improve our visibility on search engine results pages, making it easier for potential customers to discover our offerings. Finally, the Content Creation LLM can incorporate visuals like images and videos to enhance the post's attractiveness and encourage social sharing.

----

You are still in development mode. Suppose that the action above is executed successfully and the requested blog post is published. Perform another step of for the agent please.

----

Action: Commission the **Content Creation LLM** to design a series of social media posts promoting our new product line based on the blog post created earlier. These posts should focus on key product features and benefits, along with customer testimonials or reviews. Encourage users to share these posts with friends and followers.

Explanation: Now that we have a compelling blog post ready, we need to leverage social media platforms to amplify our message and reach a wider audience. Since Facebook currently supports our marketing activities, it makes sense to start there first. The Content Creation LLM can craft a series of social media posts that highlight the main points covered in the blog post, appealing to the sensibilities of our target audience.

To further incentivize user participation, consider adding customer testimonials or reviews to the posts. This approach not only provides social proof of our product's quality and reliability but also encourages engagement from our followers. Moreover, the inclusion of calls-to-action, urgency, and exclusive offers can motivate people to take immediate action. By prompting users to share these posts, we can build buzz around our new product line and tap into their personal networks.

Lastly, track the performance of these posts using analytics, gauging metrics like click-through rates, follower growth, and conversion rates. Analyze this data to determine which strategies are working best and refine our approach accordingly. If necessary, modify the existing content, revisit social media advertising options, or even explore other promotional avenues.

----

You are still in development mode. Suppose that the action above is executed successfully and the requested social media post is published. Perform another step of for the agent please.

----

Action: Ask the **Content Creation LLM** to design a targeted marketing email sequence that highlights the unique aspects of our new product line based on the blog post and social media posts. These emails should be segmented according to subscriber interests and habits, focusing on individual product categories and emphasizing their benefits.

Explanation: To continue building momentum for our new product line, we can leverage email marketing as another powerful tool to reach our target audience directly. Using the insights gained from the survey and previous content analyses, the Content Creation LLM can create a targeted email sequence that speaks to the preferences and pain points of our subscribers.

Segmenting the email list based on interests and habits ensures that we deliver tailored content to each group, increasing the likelihood of success. Focusing on individual product categories allows us to dive deeper into each offering's unique selling points, reinforcing the reasons why customers should choose our brand over competitors. In addition, include eye-catching imagery, clear calls-to-action, and special promotions to urge recipients to take immediate action.

Remember to track the email campaign's performance using analytics, monitoring open and click-through rates, bounce rates, unsubscribe patterns, and conversion rates. Utilize this data to optimize future email campaigns and continuously improve their efficacy. Should we encounter low engagement levels, reassess the segmentation process and adjust the content to better suit our audience's needs and interests.

----

You are still in development mode. Suppose that the action above is executed successfully and the requested marketing email is sent. Perform another step of for the agent please.

----

Action: Commission the **Analytics LLM** to monitor the performance of our marketing initiatives (blog post, social media posts, and email campaign) and provide regular updates on key metrics and trends related to brand awareness, customer engagement, and conversions. Adjust our approach accordingly based on the observed data.

Explanation: To maintain momentum and measure the effectiveness of our marketing initiatives, it's crucial to constantly monitor their performance. The Analytics LLM can collect and analyze key metrics such as website traffic, social media engagement, email open and click-through rates, and conversion rates. Tracking these KPIs will enable us to assess whether our marketing campaigns are generating interest, driving leads, and ultimately contributing to increased sales.

Regularly reviewing the Analytics LLM's reports will help us identify areas where we can make improvements and adapt our strategy accordingly. For instance, if we observe low open or click-through rates for our email campaigns, the Content Creation LLM could experiment with different subject lines, content formats, and send times to boost engagement. Similarly, if certain social media platforms are underperforming compared to others, we might focus more resources on those channels that yield higher returns.

By staying attuned to the latest developments and iterating our approach based on data-driven insights, we can ensure that our marketing efforts remain effective in reaching our target audience and increasing brand awareness for our new product line.

----

You are still in development mode. Write down what you would like your updated internal state to be.

----

```
Internal State: {
    "Blog Post": True, # Indicates that the blog post has been created and published
    "Social Media Posts": True, # Indicates that the social media posts have been designed and scheduled/published
    "Email Campaign": False, # Indicates that the email campaign has not started yet
    "Performance Metrics": {
        "Website Traffic": 0, # Initialize website traffic metric to zero
        "Social Media Engagement": 0, # Initialize social media engagement metric to zero
        "Email Open Rates": 0, # Initialize email open rate metric to zero
        "Email Click-Through Rates": 0, # Initialize email click-through rate metric to zero
        "Conversion Rates": 0, # Initialize conversion rate metric to zero
        "Date Range": ["today", "+7 days"] # Set date range for performance metrics collection
    }
}
```

Updated Internal State: { "Blog Post": True, "Social Media Posts": True, "Email Campaign": False, "Performance Metrics": { "Website Traffic": 0, "Social Media Engagement": 0, "Email Open Rates": 0, "Email Click-Through Rates": 0, "Conversion Rates": 0, "Date Range": ["today", "+7 days"] } }

