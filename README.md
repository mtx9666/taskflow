# TaskFlow — Full-Stack Dev Portfolio

Monorepo with two production-style projects: a **React + Node task manager** and a **Python stock analytics engine** with Jupyter demos.

**Author:** Ali ([@mtx9666](https://github.com/mtx9666))

## Projects

### 1. TaskFlow — Task management app

Modern full-stack task manager with REST API and React UI.

**Features:**
- Node.js / Express REST API
- React frontend with component architecture
- Task CRUD (create, read, update, delete)
- Responsive UI with modern CSS

**Tech:** Node.js · Express · React · MongoDB-ready structure

**Location:** `./taskflow/`

```bash
cd taskflow
npm install
cd client && npm install && cd ..
npm run dev
```

### 2. Stock Analyzer — Quantitative market analytics

Python toolkit for technical analysis, risk metrics, and comparative stock research.

**Features:**
- Moving averages, RSI, MACD, Bollinger Bands
- Returns, volatility, Sharpe ratio
- Multi-ticker comparative analysis
- Interactive Jupyter notebook walkthrough

**Tech:** Python · Pandas · yfinance · Matplotlib · Jupyter

**Location:** `./stockanalyzer/`

```bash
cd stockanalyzer
pip install -r requirements.txt
jupyter notebook notebooks/stock_analysis_demo.ipynb
```

## Project structure

```
taskflow/
├── taskflow/           # Node + React app
│   ├── client/
│   └── server.js
├── stockanalyzer/      # Python analytics
│   ├── stock_analyzer.py
│   └── notebooks/
├── README.md
└── .gitignore
```

## Prerequisites

- Node.js 18+
- Python 3.10+
- MongoDB (optional, for TaskFlow persistence)
- Git

## What this demonstrates

| Skill | TaskFlow | Stock Analyzer |
|-------|----------|----------------|
| Full-stack architecture | ✓ | |
| REST API design | ✓ | |
| React component patterns | ✓ | |
| Time-series analysis | | ✓ |
| Financial metrics | | ✓ |
| Data visualization | | ✓ |

## License

MIT
