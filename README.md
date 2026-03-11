# 🔧 [PROJECT_NAME] — Backend

> [ONE LINE — what this backend does. Be specific. No generic lines.]

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?style=flat-square&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=flat-square&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=flat-square&logo=docker)
![Status](https://img.shields.io/badge/Stage-v0_Skeleton-orange?style=flat-square)

---

## 📋 Table of Contents

- [What This Does](#-what-this-does)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Environment Variables](#-environment-variables)
- [API Overview](#-api-overview)
- [Version Roadmap](#-version-roadmap)
- [Author](#-author)

---

## 🧠 What This Does

> Fill this when you start building. Answer 3 things:
> 1. What problem does this solve?
> 2. How does it solve it?
> 3. Who is it for?

**Current Status:** `v0` — Skeleton only. Folder structure set up. Docker running. Health check live. No features yet.

---

## 🏗️ Architecture

> Add your architecture diagram here when HLD_v0.md is written.
> Paste an image or ASCII diagram showing Frontend → Backend → DB → any external service.

Full system design → [HLD_v0.md](./HLD_v0.md)

---

## 🗂️ Project Structure

| File / Folder | What It Covers |
|---|---|
| [README.md](./README.md) | You are here. Start here always. |
| [HLD_v0.md](./HLD_v0.md) | System architecture — components, data flow, tech choices |
| [LLD_v0.md](./LLD_v0.md) | Detailed design — functions, classes, sequence diagrams |
| [API_CONTRACTS.md](./API_CONTRACTS.md) | Every endpoint — URL, method, request, response, errors |
| [SCHEMA.md](./SCHEMA.md) | All DB tables, columns, indexes — human readable |
| [schema_v0.sql](./schema_v0.sql) | Raw SQL — create all v0 tables |
| [ERD.png](./ERD.png) | Visual diagram — all DB tables and relationships |
| [docker-compose.yml](./docker-compose.yml) | One command spins up DB + Redis + all dependencies |
| [.env.example](./.env.example) | All env vars with dummy values — copy to .env, never commit real .env |
| [RUNBOOK.md](./RUNBOOK.md) | Deploy, rollback, restart services, 3am incident fixes |
| [SCALE_GUIDE.md](./SCALE_GUIDE.md) | Stack decisions from 0 to 1 billion users |
| [SCALING_QUESTIONS.md](./SCALING_QUESTIONS.md) | 20 questions to ask before building any feature |
| [VERSION_ROADMAP.md](./VERSION_ROADMAP.md) | v0 to v4 — what changes at each stage, mindset per stage |
| [ADR/](./ADR/) | Architecture Decision Records — one file per major tech choice |

---

## ⚡ Quick Start

**Prerequisites:** Python 3.11+, Docker, Git
```bash
# 1. Clone the repo
git clone https://github.com/ashutosh/[REPO-NAME].git
cd [REPO-NAME]

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Open .env and fill in real values

# 5. Start all dependencies
docker-compose up -d

# 6. Start the server
uvicorn main:app --reload

# 7. Open API docs
# http://localhost:8000/docs
```

---

## 🔑 Environment Variables

| Variable | What It Is | Example |
|---|---|---|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@localhost:5432/db` |
| `SECRET_KEY` | JWT secret key | `your-secret-key-here` |
| `ENVIRONMENT` | App environment | `development` |

> Add new variables here as you add them. Full list → [.env.example](./.env.example)

---

## 📡 API Overview

| Method | Endpoint | What It Does |
|---|---|---|
| `GET` | `/health` | Health check — all dependencies status |

> Add endpoints here as you build them. Full contracts → [API_CONTRACTS.md](./API_CONTRACTS.md)

---

## 📌 Version Roadmap

| Version | Scale | What Gets Built |
|---|---|---|
| `v0` ← **you are here** | Local only | Skeleton connected. Docker running. Health check live. |
| `v1` | 0 → 10K users | Core features. Auth. Deployed on cloud. CI/CD live. |
| `v2` | 10K → 500K | Redis cache. Read replicas. Rate limiting. RabbitMQ. |
| `v3` | 500K → 10M | Kafka. Kubernetes. Multi-region. Distributed tracing. |
| `v4` | 10M → 1B | DB sharding. Custom infra. Dedicated ML infrastructure. |

> Full breakdown of every stage with mindset → [VERSION_ROADMAP.md](./VERSION_ROADMAP.md)

---

## 👤 Author

**Ashutosh**
[GitHub](https://github.com/ashutosh) · [LinkedIn](https://linkedin.com/in/ashutosh)

---

> *"Debugging is twice as hard as writing the code in the first place."* — Brian Kernighan
>
> _(Replace this with your own words when you finish this project.)_
