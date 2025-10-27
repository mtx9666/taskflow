# Gitz - Multi-Project Repository

This repository contains multiple projects showcasing different technologies and use cases.

## Projects

### 1. Stock Analyzer 📈
A comprehensive stock market analysis tool built with Python and Jupyter notebooks.

**Features:**
- Technical analysis with moving averages, RSI, MACD, and Bollinger Bands
- Performance metrics calculation (returns, volatility, Sharpe ratio)
- Comparative analysis across multiple stocks
- Risk-return visualization
- Interactive Jupyter notebook demonstrations

**Location:** `./stockanalyzer/`

### 2. TaskFlow 📋
A modern task management application with full-stack architecture.

**Features:**
- Node.js/Express backend with MongoDB
- React frontend with modern UI
- User authentication and authorization
- Task CRUD operations
- Real-time updates

**Tech Stack:**
- Backend: Node.js, Express, MongoDB, JWT
- Frontend: React, modern CSS
- Database: MongoDB with Mongoose ODM

**Location:** `./taskflow/`

## Getting Started

### Prerequisites
- Node.js (v14 or higher)
- Python 3.7+
- MongoDB (for TaskFlow)
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd gitz
```

2. For Stock Analyzer:
```bash
cd stockanalyzer
pip install -r requirements.txt
jupyter notebook
```

3. For TaskFlow:
```bash
cd taskflow
npm install
cd client
npm install
cd ..
npm run dev
```

## Project Structure

```
gitz/
├── stockanalyzer/
│   └── notebooks/
│       └── stock_analysis_demo.ipynb
├── taskflow/
│   ├── client/
│   │   ├── public/
│   │   └── src/
│   │       └── components/
│   └── package.json
├── .gitignore
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


