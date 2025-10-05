# 📡 PulseView — HA Infrastructure Dashboard

PulseView is a high-availability observability and control dashboard for distributed systems. It monitors NFS, Pacemaker, and Kubernetes health via a FastAPI backend and React UI.

## 🧱 Structure

- `backend/` — FastAPI probes + API
- `frontend/` — React + Tailwind UI
- `manifests/` — Kubernetes deployment files
- `docker-compose.yaml` — Local dev setup

## 🚀 Local Dev

```bash
docker-compose up --build

Frontend: http://localhost:3000

Backend: http://localhost:8000/health


