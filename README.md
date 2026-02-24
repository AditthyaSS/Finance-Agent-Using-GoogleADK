
<p align="center">
  <img src="assets/agent-development-kit.png" width="110" alt="Google ADK Logo"/>
</p>

<h1 align="center">Finance Assistance Agent</h1>

<p align="center">
  <em>An AI-powered finance assistant built on Google's Agent Development Kit</em>
</p>

<p align="center">
  <a href="https://github.com/google/adk-python"><img src="https://img.shields.io/badge/Powered%20by-Google%20ADK-4285F4?style=flat-square&logo=google&logoColor=white"/></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-FFD43B?style=flat-square&logo=python&logoColor=blue"/></a>
  <a href="https://dev.to/aditthyass/how-to-develop-an-agent-using-google-adk"><img src="https://img.shields.io/badge/Blog-Dev.to-0A0A0A?style=flat-square&logo=devdotto&logoColor=white"/></a>
  <a href="https://github.com/AditthyaSS/Finance-Agent-Using-GoogleADK"><img src="https://img.shields.io/github/stars/AditthyaSS/Finance-Agent-Using-GoogleADK?style=flat-square&color=yellow"/></a>
</p>

---

## What is this?

I built a **Finance Assistance Agent** using **Google ADK** — a framework by Google to build, run, and evaluate AI agents. Ask it anything about finance and it responds with structured, accurate answers using Gemini's knowledge — now enhanced with **Google Search** for real-time web results.

> **Phase 2 in progress** — The agent can now search the web using Google Search to fetch up-to-date financial information, news, and market context beyond its pre-trained knowledge.

---

## Agent in Action

<p align="center">
  <img src="assets/output.png" alt="Finance Agent Output" width="900"/>
</p>

*The agent running in the ADK Web UI — answering a question about Fixed Deposits*

---

## What's Working

- ✅ Ask finance questions — *stocks, FDs, mutual funds, budgeting, savings*
- ✅ Conversational memory within a session
- ✅ Clean responses via ADK's Web UI
- ✅ Runs locally with `adk web`
- ✅ **Google Search integration** — real-time web search for up-to-date financial info

## What's Coming

- 🔜 Live stock & crypto prices via dedicated APIs
- 🔜 Real-time market trend analysis
- 🔜 Financial news feed integration
- 🔜 Portfolio Q&A

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
│   ├── agent-development-kit.png   ← ADK logo
│   └── output.png                  ← Agent screenshot
│
├── finance_ass_agent/
│   ├── __init__.py
│   └── agent.py                    ← Agent definition
│
├── requirements.txt
├── .env                            ← Your API key (not committed)
└── README.md
```

---

## Read the Blog

Full step-by-step breakdown of how I built this agent from scratch — including agent setup, tool configuration, and running it locally.

**[→ How to Develop an Agent Using Google ADK](https://dev.to/aditthyass/how-to-develop-an-agent-using-google-adk)** on Dev.to

---

<p align="center">
  Made by <a href="https://github.com/AditthyaSS">Aditthya SS</a> &nbsp;·&nbsp;
  <a href="https://dev.to/aditthyass">Dev.to</a>
</p>
