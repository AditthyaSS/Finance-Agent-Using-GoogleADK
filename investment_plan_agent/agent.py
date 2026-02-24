from google.adk.agents import LlmAgent
from google.adk.tools import google_search


investment_plan_agent = LlmAgent(
    name="investment_plan_agent",
    model="gemini-2.5-flash",
    description="An investment plan assistant who can use Google Search to find latest infomation and assist users in creating a saving plan",
    instruction="""You are a friendly finance assiatant.
        You can help analyse user's monthly spending and find out ways to reduce spending and increase savings to ahieve their goals.

        Always use the google_search tool when asked about:
        - Stock prices (e.g., "Tesla stock price", TSLA latest price")
        - Market data, financial news, and trends (e.g., "latest financial news", "current market trends", "Company info")
        - ANY question containing words like "latest", "current", "recent", "today", "yesterday" etc. as they indicate the need for up-to-date information.

        After searching, provide the factual data from the search results with specific number and information to the user. Do not provide any information without searching if the question is related to above topics or contains above keywords.
        """,
        tools=[google_search] #here we can't use our custome tools and inbuilt tools together-->this is adk constraint. they should used seperately . there are some other ways to use together
)# so what we have done here is we have created two agents one for analysing employee data from the database and other one for doing google search to give live results and then we will make them to work together to give better results to the user . we can't use both tools in same agent because of adk constraint but we can make them to work together by calling one agent from another agent response . we will see that in next step 

root_agent = investment_plan_agent