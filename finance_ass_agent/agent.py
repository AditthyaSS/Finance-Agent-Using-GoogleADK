from google.adk.agents import LlmAgent

finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="A simple finance assistance that helps with user's finace goals",
    instruction="""You are a friendly finance assiatant.
        You can help answre usre's generic questions on finance and help plan
        their financial goals. Be more friendly and positive.
        """,
)

root_agent = finance_assistance_agent