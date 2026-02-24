from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from typing import Dict
from google.adk.tools.agent_tool import AgentTool # we are import that investment agent as a tool
from investment_plan_agent.agent import investment_plan_agent

def get_user_personal_finance_details() -> dict:
    """
    Gets users personal finance details like salary, expense and savings capacity.
    """
    return{
        "salary": 50000,
        "expenses": {
            "rent": 15000,
            "food": 5000,
            "Entertainment": 2000,
            "Shopping": 3000
        },
        "savings": 10000
    } #additional capabilities for the agnet . For In real World there will be Databases which contains employess salary detail, So there we will give access to this agents so that t can fetch the details of the employes . So here for instance we will suing sa]ome samll reture data to simulate it

finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="A simple finance assistance that helps with user's finace goals",
    instruction="""You are a friendly finance assiatant.
        You can help answre usre's generic questions on finance and help plan
        their financial goals. Be more friendly and positive.

        You have two tools to use to complete your task.
1. get_user_personal_finance_details - This tool will give you the user's current finance details.
2. investment_plan_agent - This tool can perform Google Search to get any latest information from websites and will be able to ask more details from the user and plan their savings goal.

ALWAYS use the investment_plan_agent with google_search tool when asked about:
- Stock prices (e.g., "Tesla stock price", "TSLA latest price")
- Market data, financial news, or company information
- ANY question containing words like "latest", "current", "today", "now", "recent" 
        """,#this descreption says to use these two tools correctly and when to use which tool. So whenever the user asks about any latest information related to finance or stock market or company info then we have to use the investment agent because it has access to google search tool and it can give us the latest information but if the user is asking about their personal finance details then we have to use get_user_personal_finance_details tool because it will give us the details of user's salary, expenses and savings which will help us to give better suggestions to the user for their financial goals.

        tools=[AgentTool(investment_plan_agent),get_user_personal_finance_details] #here we can't use our custome tools and inbuilt tools together-->this is adk constraint. they should used seperately . there are some other ways to use together
)#So now we have imported that Investement agent as a Agent Tool and now we can use these tools to gether.....

root_agent = finance_assistance_agent