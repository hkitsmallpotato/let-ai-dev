# AI roleplay a business consultant hired to rescue a company

(Note: The background infos are real but perhaps exeggerated somewhat, manually curated from a Hackernews thread)

**AI used: Guanaco-33B, online demo**

**Company in the case study: Digital Ocean**

Further note: The online demo has a prompt length limit so I split it into two. Sadly it is unable to hold off discussing until the full context is given and so it actually gave 2 responses, one with only the first half of the report seen, the 2nd after seeing everything.

## User prompt

You are an expert business consultant specializing on technology and cloud computing, who has been hired by Digital Ocean (DO) in what is perceived as an urgent company rescue attempt. The CEO believes their company is in deep trouble and is approaching a crisis, and has given you the following summary of current situation: 

- Externally, we face pressure from the consolidated big 3 public clouds (AWS, GCP, Azure), and although DO's droplet (i.e. VM) is cheaper than the big 3, at $5/GB of ram, we've lost our confidence in our ability to compete on our core offerings. 
- This is reflected in the financial report, which shows growing revenue but falling profits. Although rising the unit price is proposed internally, we fear this will lead to us losing our only edge against the big 3. 
- Internally, our engineering is a complete mess. We’ve acquired tech debt to a debilitating levels, our systems have massive circular dependencies, Not-invented-here syndrome resulted in excessive, poorly built in-house/internal platforms, and the quality of our engineers are subpar with many lacking basic understanding of distributed system and how to operate them at scale in a reliable, sustainable manner. 
- The company culture is toxic, with teams playing turf game paralysing progress, while middle and upper managements have become so risk averse that any effort from the frontline engineer to refactor, re-architect, or otherwise improve these broken systems are shot down. 
- The net results is that the morale is low with pay being low while fire-fighting production system is frequent, inducing the better engineers to leave for greener pastures. As well, we’ve been unable to deliver any new products on our own for many years. 
- Recently, DO has went on a buying spree acquiring various companies, such as css-tricks.com (content creator specialising on teaching the hard part of css) as well as paperspace (cloud vendor specialised on AI use case, with their free GPU enabled cloud Jupiter notebook being popular). Meanwhile, DO sacked their very high quality writing team who had produced technical "How-tos" guide that are widely regarded as the best in the industry.
- External commenter in public has also critiqued our recent moves, saying that "DO has lost their core focus and appeal. Instead of upgrading their hardware, software, and other crucial piece of their infra, there’s been gimmicks, acquisitions, and marketings."

(End of report)

Based on these info, advise the CEO of DO on what he should do in the short team, and help him devise a new business and technical strategy for the company.

## AI response first attempt

As your consultant, I would first take a step back and look at the bigger picture. While there are clearly some challenges facing DO, it’s important not to lose sight of the strengths they still possess. Their low cost VM offering remains a key differentiator and one that could potentially be leveraged further. They also seem to have a strong brand recognition among developers and SMBs, which can be used to build upon.

Regarding the external pressures from the big 3, it’s worth considering whether DO should continue trying to compete directly with them. Instead, they could position themselves as a niche player focused on specific use cases where their lower costs can provide real value. For example, they might target startups or certain types of workloads that require more compute power but don’t need all the bells and whistles offered by the big 3.

On the internal side, the technical issues and cultural problems are serious concerns that must be addressed. However, rather than attempting a radical overhaul, I would recommend a gradual approach. One way to begin would be to establish clear goals for each team and ensure that everyone understands how their work contributes to those goals. This could help reduce the turf wars and encourage more collaboration.

Another area of focus should be improving the overall architecture and codebase. There may already be some good ideas within the organization about how to make things better, but they haven’t gotten enough support due to the risk aversion. To address this, management could set up a process for reviewing and prioritizing potential improvements based on their expected impact.

In general, the key here is to move forward incrementally while keeping the larger objectives in mind. Making small changes that deliver tangible results can help build momentum and create a sense of shared purpose across the organization.

After reading through the second part of the summary you provided, my advice to the CEO of DO would be to refocus the company’s efforts on its core competencies and to develop a long-term strategic plan that addresses both the technical and organizational challenges faced by the company. Here are a few suggestions for what the CEO could consider doing:

1. **Revisit the company’s mission statement and values:** It seems like DO has strayed away from its original vision and lost its identity. By taking the time to revisit the company’s mission statement and values, the leadership team can get a clearer idea of what the company stands for and what sets it apart from the competition.
2. **Develop a comprehensive technology roadmap:** Once the company has clarified its mission and values, it can start working towards building a detailed technology roadmap that outlines the company’s strategic direction and priorities. This roadmap should include plans for modernizing the existing infrastructure, enhancing the user experience, and developing new features and services that align with the company’s goals.
3. **Improve communication and transparency:** The fact that the company’s employees feel disconnected from the leadership team and frustrated with the state of affairs suggests that there needs to be greater transparency and openness within the organization. The CEO could implement regular town hall meetings, foster cross-functional collaboration, and encourage open feedback channels to increase engagement and morale.
4. **Invest in talent development:** Given the widespread skills gap within the organization, it’s critical for the company to invest in training and professional development programs that can help upskill its current workforce and attract top talent. This could involve partnering with local universities or setting up an in-house learning and development program.
5. **Establish accountability and metrics:** Finally, the CEO should put in place a framework for measuring success and holding people accountable for achieving their goals. This could mean implementing a performance evaluation process that incorporates objective metrics and providing regular feedback to employees.

Overall, the key takeaway is that DO needs to stop playing catch-up and instead chart its own course by focusing on what it does best and executing effectively. With a renewed sense of purpose and a commitment to continuous improvement, the company can turn around its fortunes and once again become a leader in the cloud computing space.

## AI response second attempt

As your consultant, my first step would be to take a deeper look into the problems mentioned in the report. It seems like there are several issues affecting the company’s performance, both externally and internally. Here are some initial thoughts based on the information provided:

1. **Competition with the Big 3 Cloud Providers:** The fact that DO’s droplets are cheaper than those offered by AWS, GCP, and Azure could be seen as an advantage, but it sounds like the company lacks confidence in its ability to compete on price alone. Raising prices may not be the best solution if the goal is to maintain market share and attract new customers. One option might be for DO to differentiate itself through added value services such as better customer support, more robust security features, or easier integration with third-party tools.
2. **Financial Performance:** Falling profits despite increasing revenues can indicate that costs are outpacing income growth. There may be operational efficiencies that could be improved to boost margins, such as streamlining processes or reducing overhead expenses. Additionally, it’s important to understand why profitability is declining, whether it’s due to higher expenses, lower sales volumes, or other factors.
3. **Technical Debt:** Tech debt refers to the accumulation of software development decisions and architectural choices that impede future progress. In the long run, it can slow down development, increase maintenance costs, and make the codebase harder to work with. Addressing technical debt requires a strategic approach that balances short-term needs with long-term goals. This could include initiatives such as refactoring, automation, and process improvements.
4. **Toxic Company Culture:** A dysfunctional organizational culture can create barriers to innovation and stifle employee morale. Encouraging open communication, promoting collaboration across departments, and establishing clear goals and objectives can help to foster a positive working environment.

In order to address these challenges effectively, it’s crucial to gather additional data and gain a deeper understanding of the underlying root causes. I would recommend conducting a thorough analysis of the company’s operations, finances, and culture to identify areas for improvement. From there, we can begin to develop a strategy for moving forward.

After reviewing the additional information you’ve provided about the current state of affairs at DO, here are my suggestions for the CEO to consider:

### Short-Term Actions:

1. **Assess the impact of the recent acquisitions:** Before determining next steps, the CEO should evaluate the effectiveness of the recent acquisitions and determine how they fit into the overall strategy for the company. He should also assess the potential benefits and risks associated with integrating these new assets into the existing infrastructure.
2. **Revisit the pricing strategy:** Given the concerns expressed by external commentators, the CEO should revisit the pricing structure for DO’s products and services. He should consider whether adjusting prices would enable the company to better compete with the Big 3 cloud providers while still generating sufficient revenue to cover operating costs.
3. **Improve communications with employees:** To address the issue of low morale among staff members, the CEO should prioritize improving internal communications. This includes ensuring that all employees are aware of the company’s vision and values, and keeping them updated on major changes and developments. Regular feedback mechanisms should also be implemented to allow employees to voice their opinions and concerns.
4. **Focus on talent retention:** Retaining top talent is critical for the success of the organization, especially given the competitive landscape. The CEO should implement strategies to encourage talented individuals to stay with the company, including offering competitive salaries, providing professional development opportunities, and creating a positive workplace culture.
5. **Evaluate the technical roadmap:** The CEO should ensure that the company has a clear technical roadmap in place that aligns with its broader business objectives. This should involve evaluating the current technology stack and identifying areas where improvements can be made. Any proposed solutions should be carefully vetted to ensure that they will meet the needs of the business and provide a good return on investment.

### Long-Term Strategy:

1. **Define a clear mission statement:** The CEO should work with senior leadership to define a clear and concise mission statement that articulates the purpose of the company. This should serve as a guiding light for decision making and should be used to inform all aspects of the business, from product development to hiring practices.
2. **Establish key performance indicators (KPIs):** The CEO should set specific KPIs that will be used to measure the success of the company over time. These metrics should be aligned with the mission statement and should reflect the company’s most important goals. Regular tracking and reporting of KPIs will help to keep everyone focused on achieving desired outcomes.
3. **Emphasize innovation:** Innovation is essential for survival in today’s fast-paced digital world. The CEO should promote a culture of innovation within the organization and allocate resources to support research and development efforts. This could include encouraging employees to come up with new ideas and allowing them to experiment with different approaches without fear of failure.
4. **Prioritize user experience:** Making sure that users have a positive experience when interacting with the company’s products and services is critical for building loyalty and driving growth. The CEO should ensure that UX is a priority throughout the design and development process, with dedicated teams tasked with optimizing the user journey.
5. **Diversify revenue streams:** Relying solely on one source of revenue can put the company at risk if that particular market segment experiences a downturn. Diversification is therefore essential for ensuring the longevity of the business. The CEO should explore ways to generate alternative sources of income, either by developing new products or expanding into related markets.

(internet connection lost)
