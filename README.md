
<p align="center">
  <img src="assets/agent-development-kit.png" width="110" alt="Google ADK Logo"/>
</p>

<h1 align="center">Finance Assistance Agent</h1>

<p align="center">
  <em>A multi-agent AI finance assistant built on Google's Agent Development Kit</em>
</p>

<p align="center">
  <a href="https://github.com/google/adk-python"><img src="https://img.shields.io/badge/Powered%20by-Google%20ADK-4285F4?style=flat-square&logo=google&logoColor=white"/></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-FFD43B?style=flat-square&logo=python&logoColor=blue"/></a>
  <a href="https://dev.to/aditthyass/how-to-develop-an-agent-using-google-adk"><img src="https://img.shields.io/badge/Blog-Dev.to-0A0A0A?style=flat-square&logo=devdotto&logoColor=white"/></a>
  <a href="https://github.com/AditthyaSS/Finance-Agent-Using-GoogleADK"><img src="https://img.shields.io/github/stars/AditthyaSS/Finance-Agent-Using-GoogleADK?style=flat-square&color=yellow"/></a>
</p>

---

## What is this?

I built a **Finance Assistance Agent** using **Google ADK** — a framework by Google to build, run, and evaluate AI agents. This project now features a **multi-agent architecture** where two specialized agents collaborate to provide a complete financial picture:

- **Finance Assistance Agent** — analyzes your salary, expenses, and savings capacity from an employee database (simulated with dummy data for now).
- **Investment Plan Agent** — uses **Google Search** to fetch real-time market trends, stock prices, and financial news to generate actionable investment insights.

> **ADK Constraint:** Google ADK does not allow mixing custom tools and built-in tools (like `google_search`) within the same agent. To work around this, two separate agents are built and then connected using `AgentTool` — importing the investment agent as a callable tool inside the finance agent.

> **Read the blog for a full breakdown of this constraint and how it's solved →** [How to Develop an Agent Using Google ADK](https://dev.to/aditthyass/how-to-develop-an-agent-using-google-adk)

---

## Agent in Action

<p align="center">
  <img src="assets/output.png" alt="Finance Agent Output" width="900"/>
</p>

*The agent running in the ADK Web UI — answering a question about Fixed Deposits*

---

## Architecture

```
                    ┌──────────────────────────────────┐
                    │      finance_assistance_agent      │
                    │          (Root Agent)              │
                    │                                    │
                    │  Tool 1: get_user_personal_        │
                    │          finance_details()         │
                    │  Tool 2: AgentTool(               │
                    │          investment_plan_agent)    │
                    └──────────────┬───────────────────┘
                                   │ delegates to
                    ┌──────────────▼───────────────────┐
                    │       investment_plan_agent        │
                    │                                    │
                    │  Tool: google_search               │
                    │  → Real-time market data           │
                    │  → Stock prices & news             │
                    │  → Investment insights             │
                    └───────────────────────────────────┘
```

The two agents are connected via **`AgentTool`** from `google.adk.tools.agent_tool` — this lets the root finance agent call the investment agent as a sub-agent whenever real-world data is needed.

---

## What's Working

- ✅ Ask general finance questions — *stocks, FDs, mutual funds, budgeting, savings*
- ✅ **Employee/Salary data analysis** — reads salary, rent, food, entertainment & shopping spends
- ✅ **Savings & profit insights** — understands your cash flow and identifies saving opportunities
- ✅ **Google Search integration** — fetches live stock prices, market trends, and financial news
- ✅ **Multi-agent collaboration** — finance agent delegates web lookups to the investment agent via `AgentTool`
- ✅ Conversational memory within a session
- ✅ Clean responses via ADK's Web UI
- ✅ Runs locally with `adk web`

## Limitations / Notes

- � **No real database connected** — employee salary and expense data is returned from a Python function with dummy values (simulating what a real company database would provide)
- � **ADK constraint** — custom tools and built-in tools cannot be combined in a single agent; multi-agent wiring via `AgentTool` is the current workaround

---

## Run It Yourself

```bash
# 1. Clone the repo
git clone https://github.com/AditthyaSS/Finance-Agent-Using-GoogleADK.git
cd Finance-Agent-Using-GoogleADK

# 2. Set up virtual environment
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key
echo GOOGLE_API_KEY=your_key_here > .env

# 5. Launch the agent
adk web
```

Then open your browser at `http://localhost:8000` and start chatting.

---

## Project Structure

```
Finance-Agent-Using-GoogleADK/
│
├── assets/
│   ├── agent-development-kit.png     ← ADK logo
│   └── output.png                    ← Agent screenshot
│
├── finance_ass_agent/
│   ├── __init__.py
│   └── agent.py                      ← Root agent + employee finance tool
│                                        Uses AgentTool to call investment agent
│
├── investment_plan_agent/
│   ├── __init__.py
│   └── agent.py                      ← Sub-agent with Google Search tool
│                                        Fetches real-time market data & insights
│
├── requirements.txt
├── .env                              ← Your API key (not committed)
└── README.md
```

---

## How the Two Agents Work Together

| Agent | Role | Tools |
|---|---|---|
| `finance_assistance_agent` | Root agent — handles user queries, reads employee finance data | `get_user_personal_finance_details()`, `AgentTool(investment_plan_agent)` |
| `investment_plan_agent` | Sub-agent — fetches live financial data from the web | `google_search` |

When you ask something like *"Based on my salary, what's the best SIP to invest in right now?"*, the root agent:
1. Calls `get_user_personal_finance_details()` to get your salary (₹50,000), expenses, and savings (₹10,000/month)
2. Delegates to `investment_plan_agent` which searches Google for current SIP options and market trends
3. Combines both to give you a personalized, real-world investment recommendation

---

## Read the Blog

Full step-by-step breakdown of how I built this agent from scratch — including the ADK constraint workaround, multi-agent wiring with `AgentTool`, and the design decisions behind this architecture.

**[→ How to Develop an Agent Using Google ADK](https://dev.to/aditthyass/how-to-develop-an-agent-using-google-adk)** on Dev.to

---

<p align="center">
  Made by <a href="https://github.com/AditthyaSS">Aditthya SS</a> &nbsp;·&nbsp;
  <a href="https://dev.to/aditthyass">Dev.to</a>
</p>
