# 📌 VERSION ROADMAP — Project Evolution Guide

> This file defines how this project grows from a basic working skeleton to a billion-user scale system.
> Every version is a checkpoint. You do not jump versions. You feel the pain first, then upgrade.

---

## Version Map

| Version | Scale | Goal |
|---|---|---|
| v0 | 0 users — Local only | Connect everything. Skeleton works end to end. |
| v1 | 0 → 10K users | Core features live. Real users. Basic performance. |
| v2 | 10K → 500K users | Caching, queues, read replicas. Handle real load. |
| v3 | 500K → 10M users | Kafka, Kubernetes, multi-region. Serious scale. |
| v4 | 10M → 1B users | Sharding, custom infra, ML at scale. FAANG level. |

---

## v0 — Connect Everything (Stage Zero)

**Scale:** Local machine only. 0 real users.

**Goal:** Frontend talks to backend. Backend talks to DB. Data comes back. App runs with one command.

**What you build:**
- Project folder structure set up
- docker-compose runs DB locally
- Backend health check endpoint working
- Frontend loads and hits backend
- One real data flow works end to end (example: user submits → backend saves → frontend shows result)
- .env.example committed
- README has setup steps that actually work

**What you do NOT build in v0:**
- No auth (or just the most basic)
- No caching
- No queues
- No ML models in production
- No CI/CD
- No tests (maybe one smoke test)

**Design files for v0:**
- HLD_v0.md — boxes and arrows only. Frontend → Backend → DB
- LLD_v0.md — folder structure + core function names
- schema_v0.sql — only tables needed to run today
- API_CONTRACTS.md — only endpoints that exist today
- docker-compose.yml — DB only

**Approach — v0 mindset:**
> Do not think about scale. Do not think about performance.
> Think only: does the wire connect? Does data flow?
> A working ugly app beats a beautiful broken app every time.
> Get to working first. Then get to good.

---

## v1 — Core Features Live (First Real Version)

**Scale:** 0 → 10K users.

**Goal:** Real users can use the core feature. App is deployed. Basic monitoring exists.

**What gets added:**
- Full auth (JWT, refresh tokens, bcrypt)
- Core feature fully built and tested
- Deployed to cloud (AWS EC2 or similar)
- Nginx as reverse proxy
- Redis for sessions and basic caching
- Celery + Redis for background tasks
- AWS S3 for file storage
- Cloudflare CDN (free tier)
- Basic CI/CD pipeline (GitHub Actions)
- Structured logging added
- /health endpoint covers all dependencies

**Design files added:**
- HLD_v1.md — add Redis, Celery, S3, Nginx to architecture
- LLD_v1.md — detailed design for each core feature
- schema_v1.sql — updated schema with auth tables
- ADR/001_why_redis.md — first architecture decision recorded

**Approach — v1 mindset:**
> Now you think about correctness, security, and reliability.
> Every feature behind a feature flag.
> Docs before code — write API contract before building endpoint.
> CI/CD before your 3rd feature. Manual deploys create fear.

---

## v2 — Handle Real Load (Scale Up)

**Scale:** 10K → 500K users.

**Goal:** App does not fall over under load. Read performance is fast. Background jobs are reliable.

**What gets added:**
- PostgreSQL read replicas (reads go to replica, writes to primary)
- Redis Cluster (replace single Redis)
- RabbitMQ (replace Celery+Redis queue for complex routing)
- Elasticsearch (add search if needed)
- Rate limiting on all public endpoints
- Database indexes reviewed and optimized
- Query performance analyzed (EXPLAIN ANALYZE on slow queries)
- Load testing with k6 before every major release
- Horizontal scaling — multiple backend instances behind Nginx

**Design files added:**
- HLD_v2.md — add read replicas, Redis cluster, RabbitMQ, Elasticsearch
- LLD_v2.md — updated for new services
- schema_v2.sql — index additions, query optimizations
- ADR/002_why_read_replica.md
- ADR/003_why_rabbitmq.md

**Approach — v2 mindset:**
> You have felt the pain. DB is slow. Cache is a single point of failure.
> Now you fix what hurts. Not what you think will hurt.
> Measure first. Optimize what the data tells you.

---

## v3 — Serious Scale (Production Grade)

**Scale:** 500K → 10M users.

**Goal:** System handles massive concurrent load. No single point of failure. Multi-region.

**What gets added:**
- Kafka (replace RabbitMQ — millions of events, guaranteed delivery)
- Kubernetes (replace manual EC2 — auto scaling, self healing)
- Cassandra (for write-heavy features like activity feeds, logs)
- Multiple AWS regions (latency + availability)
- Distributed tracing (Jaeger or AWS X-Ray)
- Full observability stack (Prometheus + Grafana)
- Database connection pooling (PgBouncer)
- Microservices split where team size demands it

**Design files added:**
- HLD_v3.md — full distributed system architecture
- LLD_v3.md — service contracts, Kafka topic design
- schema_v3.sql — Cassandra schema + sharding strategy
- ADR/004_why_kafka.md
- ADR/005_why_kubernetes.md

**Approach — v3 mindset:**
> You split monolith only when you feel the pain — deploy conflicts, team scaling, different scaling needs.
> Not before.
> Observability is now your best friend. If you cannot measure it you cannot fix it.

---

## v4 — FAANG Level (1 Billion Users)

**Scale:** 10M → 1B users.

**Goal:** Custom infrastructure. ML at scale. Every millisecond matters.

**What gets added:**
- Database sharding (horizontal partition of PostgreSQL)
- Custom CDN or Akamai (replace Cloudflare)
- Dedicated ML infrastructure (separate training + serving clusters)
- Java or Go for bottleneck services (where Python is too slow)
- Global load balancing
- Chaos engineering (Netflix Simian Army style)
- Cost optimization at every layer

**Design files added:**
- HLD_v4.md — global distributed architecture
- LLD_v4.md — sharding strategy, ML serving design
- ADR/006_why_sharding.md
- ADR/007_why_java_for_X_service.md

**Approach — v4 mindset:**
> Every decision is now a cost-performance tradeoff.
> You have a dedicated team per service.
> Architecture is about people and teams as much as technology.

---

## File Versioning Convention
```
HLD_v0.md       ← architecture at v0
HLD_v1.md       ← architecture at v1 (v0 stays, never deleted)
schema_v0.sql   ← DB at v0
schema_v1.sql   ← DB at v1
LLD_v0.md
LLD_v1.md
```

These files are never overwritten — they are your project history.

These files are updated in place across all versions:
- README.md
- API_CONTRACTS.md
- RUNBOOK.md
- SCALE_GUIDE.md
- SCALING_QUESTIONS.md
- VERSION_ROADMAP.md (this file)
- docker-compose.yml
- .env.example

