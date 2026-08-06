# Movewell Family 🏃‍♀️🧘‍♂️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Node Version](https://img.shields.io/badge/node-20%2B-green.svg)](https://nodejs.org/)
[![MCP Compliance](https://img.shields.io/badge/MCP-v1.0-purple.svg)](https://modelcontextprotocol.io)
[![Home Assistant Add-on](https://img.shields.io/badge/Home%20Assistant-Add--on-blue.svg)](https://www.home-assistant.io/)
[![OpenAI Codex OSS](https://img.shields.io/badge/OpenAI-Codex%20OSS%20Maintainer-orange.svg)](https://openai.com/form/codex-for-oss/)

> **Movewell Family** is an open-source, privacy-first AI platform designed for multi-generational family movement health, posture tracking, and adaptive physical rehabilitation. It empowers households to track movement baselines, prevent joint strain, and follow clinically guarded daily mobility routines.

---

## 🌟 Key Features

- 👨‍👩‍👧‍👦 **Multi-Generational Family Governance**: Tailored movement profiles for children, adults, and seniors with personalized mobility baselines.
- 🛡️ **Deterministic Clinical Safety Hardguards**: A non-bypassable safety engine that blocks high-impact or conflicting exercises when acute pain, fatigue, or joint restrictions are detected.
- 📷 **Real-Time Posture Vision Engine**: TypeScript-based Model Context Protocol (MCP) vision service calculating forward head tilt, lumbar spine flexion, and balance symmetry.
- 🏠 **Home Assistant Native**: Deployable as an official Home Assistant Add-on with real-time sensors, dashboard cards, and automation triggers.
- 🔌 **Model Context Protocol (MCP) Support**: Exposes standardized tools for LLM agent integration (OpenAI Codex, Claude, Custom GPTs).

---

## 🏗️ Architecture & Data Flow

```mermaid
flowchart LR
    subgraph Privacy Boundary (Local Hardware)
        A[Pose Keypoints / Camera] --> B[Movewell Vision MCP Service]
        B -->|Joint Vectors| C[Movewell Engine FastAPI]
        D[Family Health Profiles] --> C
    end
    
    subgraph Safety & Recommendation
        C --> E{Clinical Safety Hardguard}
        E -->|Passed| F[Adaptive Movement Protocol]
        E -->|Blocked / High Pain| G[Restorative Passive Protocol]
    end

    F --> H[Home Assistant Sensors & Dashboard]
    G --> H
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 20+

### 1. Movewell Engine (Python Backend)

```bash
# Clone the repository
git clone https://github.com/movewell-family/movewell-family.git
cd movewell-family/movewell_engine

# Install dependencies
pip install -r requirements.txt

# Run unit tests
pytest

# Launch backend server
uvicorn app.main:app --reload --port 8000
```

### 2. Movewell Vision Service (TypeScript MCP)

```bash
cd movewell-family/movewell_vision

# Install dependencies and build
npm install
npm run build

# Start vision MCP service
npm start
```

---

## 📖 API & MCP Tool Contract

### Engine Health Check
`GET http://localhost:8000/health`

### Generate Daily Recommendation
`POST http://localhost:8000/api/v1/recommendation`

```json
{
  "profile": {
    "member_id": "fam_01",
    "display_name": "Alex",
    "age_group": "adult",
    "mobility_level": "moderate",
    "restricted_joint_movements": ["knee_patella"]
  },
  "readiness": {
    "sleep_score": 82.0,
    "fatigue_level": 3,
    "pain_level": 0
  }
}
```

### Model Context Protocol (MCP) Tools
The vision service exposes standard tools at `http://localhost:2091/mcp/tools`:
- `analyze_posture_frame`: Evaluates forward head tilt & shoulder asymmetry.
- `get_lumbar_flexion_angle`: Measures spine flexion during squats.
- `get_movement_balance_score`: Evaluates left vs right lower body balance.

---

## 🛡️ Safety & Privacy First

- **Zero Cloud Streaming**: Raw camera frames remain local. Only 2D numerical joint coordinates are processed in memory.
- **Clinical Safety Rules**: Soft LLM recommendations are hard-filtered by deterministic rules (`app/services/safety_hardguard.py`). Acute pain (>6/10) immediately triggers restorative passive rest protocols.

---

## 🤝 Contributing

We welcome contributions from open-source developers, physical therapists, and researchers! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide and review our [SECURITY.md](SECURITY.md) policy.

---

## 📜 License

Distributed under the [MIT License](LICENSE). Copyright (c) 2026 Movewell Family Open Source Community.
