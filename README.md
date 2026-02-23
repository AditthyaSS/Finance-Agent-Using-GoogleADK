<div align="center">

<img src="https://raw.githubusercontent.com/google/adk-python/main/docs/assets/agent-development-kit.png" alt="Google ADK Logo" width="200"/>

# 💰 Finance Assistance Agent

**Built with [Google Agent Development Kit (ADK)](https://github.com/google/adk-python)**

[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://github.com/google/adk-python)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Dev.to Blog](https://img.shields.io/badge/Read%20My%20Blog-DEV.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/aditthyass/how-to-develop-an-agent-using-google-adk)

</div>

---

## 📖 About

I built a **Finance Assistance Agent** using the **Google Agent Development Kit (ADK)** — Google's open-source framework for building, evaluating, and deploying AI agents with precision and flexibility.

This agent is designed to answer your finance-related questions intelligently, powered by Gemini's pre-trained knowledge.

---

## ✅ What It Can Do (Phase 1)

In this phase of development, the agent can:

- 💬 Answer **finance-related questions** based on its pre-trained knowledge
- 📊 Explain concepts like **stocks, mutual funds, budgeting, savings, and investing**
- 🧠 Provide general financial guidance and definitions
- 🔁 Maintain a **conversational flow** through ADK's session management

> **Note:** The agent currently answers based on **previously trained data only**. It does **not** have access to real-time information such as live market prices, current trends, or today's news.

---

## 🚧 Current Limitations

| Feature | Status |
|---|---|
| Pre-trained financial Q&A | ✅ Available |
| Real-time market prices | ❌ Not yet available |
| Current market trends | ❌ Not yet available |
| Live stock/crypto data | ❌ Not yet available |
| Latest financial news | ❌ Not yet available |

---

## 🗺️ Roadmap — Phase 2 (Coming Soon)

In the next phase of development, we plan to add:

- 📈 **Real-time market data** integration (stocks, crypto, forex)
- 📰 **Live financial news** feed and trend analysis
- 🔍 **Web search tool** for up-to-date information
- 📉 **Portfolio tracking** and insights
- 🌐 **Multi-tool agent** with API integrations

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Google ADK installed
- A valid **Gemini API Key**

### Installation

```bash
# Clone the repository
git clone https://github.com/AditthyaSS/Finance-Agent-Using-GoogleADK.git
cd Finance-Agent-Using-GoogleADK

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Running the Agent

```bash
adk run finance_ass_agent
```

Or launch the interactive ADK web UI:

```bash
adk web
```

---

## 📁 Project Structure

```
Finance-Agent-Using-GoogleADK/
├── finance_ass_agent/
│   ├── __init__.py       # Package entry point
│   └── agent.py          # Agent definition
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not committed)
├── .gitignore
└── README.md
```

---

## 📝 Blog

Want to learn how I built this? Read my full step-by-step guide on Dev.to:

👉 **[How to Develop an Agent Using Google ADK](https://dev.to/aditthyass/how-to-develop-an-agent-using-google-adk)**

---

## 🛠️ Built With

- [Google ADK (Agent Development Kit)](https://github.com/google/adk-python) — Agent framework by Google
- [Gemini API](https://ai.google.dev/) — Google's multimodal AI model
- Python 3.10+

---

## 👨‍💻 Author

**Aditthya SS**
- Dev.to: [@aditthyass](https://dev.to/aditthyass)
- GitHub: [@AditthyaSS](https://github.com/AditthyaSS)

---

<div align="center">
  <sub>⭐ If you found this helpful, consider giving a star to the repo!</sub>
</div>
