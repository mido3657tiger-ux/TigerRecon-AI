# 🐯 TigerRecon-AI

<div align="center">

![Status](https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/PYTHON-3.x-blue?style=for-the-badge)
![Flask](https://img.shields.io/badge/FLASK-API-lightgrey?style=for-the-badge)
![React](https://img.shields.io/badge/REACT-FRONTEND-61dafb?style=for-the-badge)
![License](https://img.shields.io/badge/LICENSE-MIT-yellow?style=for-the-badge)

**AI-Powered Reconnaissance & Asset Discovery Framework**

*Built for authorized security researchers and bug bounty hunters*

</div>

---

## 📖 Overview

**TigerRecon-AI** is a web-based reconnaissance tool that combines a Python/Flask backend with a React frontend dashboard. It automates asset discovery and port scanning for authorized security testing.

> ⚠️ **For authorized testing only.** Only use on systems you own or have explicit written permission to test.

---

## ✨ Features

- 🔍 Automated asset & subdomain discovery
- 🛰️ Multi-threaded port scanning
- 📊 Live results dashboard (React frontend)
- 🔗 REST API for integration with other tools
- 📄 Export scan results as JSON/HTML

---

## 🗂️ Project Structure

```
TigerRecon-AI/
├── backend/
│   ├── server.py           # Flask API server
│   ├── requirements.txt    # Python dependencies
│   └── scanners/
│       └── port_scanner.py # Port scanning module
├── frontend/
│   ├── index.html          # Main HTML page
│   └── src/
│       └── App.js          # React dashboard
└── package.json            # Frontend dependencies
```

---

## 🚀 Quick Start

### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt
python server.py --host=0.0.0.0 --port=5000
```

### 2. Frontend Setup

```bash
npm install
npm run start
```

Then open: `http://localhost:3000`

---

## 🔒 Legal & Ethics

This tool is for **educational and authorized security testing only**.

- ✅ Use on your own systems
- ✅ Use with written permission from the target owner
- ✅ Use in legal bug bounty programs (HackerOne, Bugcrowd)
- ❌ Never use on systems without permission

The author is not responsible for any misuse.

---

## 👤 Author

**Tiger-X** | Security Researcher

[![HackerOne](https://img.shields.io/badge/HackerOne-Profile-red?style=flat-square)](https://hackerone.com)

---

<div align="center">
<sub>Built for authorized hunters. Stay legal, stay sharp. 🎯</sub>
</div>
