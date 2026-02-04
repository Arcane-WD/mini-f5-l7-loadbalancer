# Mini F5 – Layer-7 Load Balancer

This project implements a minimal **Application Delivery Controller (ADC)** using **NGINX** as a Layer-7 reverse proxy and multiple **FastAPI** backend services.

It models the core behavior of enterprise ADCs such as **F5 BIG-IP LTM**, including load-balancing, session persistence, and health-based failover.

---

## Architecture

```
Client
   |
   v
NGINX (Layer-7 Reverse Proxy / ADC)
   |
   +── backend1 (FastAPI)
   +── backend2 (FastAPI)
   +── backend3 (FastAPI)
```

NGINX acts as the **virtual server (VIP)** and **traffic manager**.
FastAPI containers act as **pool members**.

All traffic enters through NGINX and is forwarded to a selected backend.

---

## Implemented ADC Features

* Layer-7 reverse proxy (NGINX)
* Round-robin load balancing
* Backend pool with multiple members
* Cookie-based session persistence (NAT-safe)
* Health-based backend failover
* Per-backend request counters
* HTTP health endpoint (`/health`)
* Fully containerized
* Single-command startup using Docker Compose

---

## How Session Persistence Works

Each client receives a cookie (`SERVERID`) on their first request.
NGINX hashes this cookie and uses it to consistently route that client to the same backend on subsequent requests.

This is equivalent to **F5 cookie persistence profiles** used to maintain login sessions, carts, and application state.

---

## Health Monitoring and Failover

Each backend exposes:

```
GET /health
```

NGINX continuously monitors backend availability.
If a backend stops responding, it is temporarily removed from the pool and traffic is automatically re-routed to healthy servers.

This simulates **F5 LTM pool member health checks and failover behavior**.

---

## Technology Stack

* NGINX (Layer-7 reverse proxy and load balancer)
* FastAPI (backend services)
* Docker
* Docker Compose

---

## Backend Service Behavior

Each backend instance returns:

* Its container hostname
* A request counter
* A simple response message

This allows real-time observation of how traffic is distributed and persisted.

---

## How to Run

Build the backend image:

```bash
cd backends
docker build -t fastapi-backend .
```

Start the full ADC system:

```bash
cd ..
docker compose up
```

Access the virtual server:

```
http://localhost
```

All requests flow through NGINX and are forwarded to one of the backend services.

---

## Verifying Load Balancing

Use curl to force new TCP connections:

```bash
curl http://localhost
curl http://localhost
curl http://localhost
```

The `hostname` field will rotate across backend containers.

---

## Verifying Persistence

Open in a browser and refresh multiple times — the backend will remain the same.
Open in an incognito window — a different backend will be selected.

This demonstrates cookie-based session persistence.

---

## Verifying Failover

Stop a backend:

```bash
docker stop backend1
```

Within a short interval, traffic will be automatically routed to another backend.

This demonstrates health-based failover.

---

## Project Structure

```
mini-f5-l7-loadbalancer/
├── backends/           # FastAPI backend service
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── nginx/              # NGINX ADC configuration
│   └── nginx.conf
├── docker-compose.yml  # Multi-container topology
└── README.md
```

---

## Why This Project Exists

This project provides hands-on proof of how enterprise-grade ADCs such as **F5 BIG-IP LTM** operate:

* Virtual servers
* Backend pools
* Load-balancing algorithms
* Session persistence
* Health monitoring and failover
* Layer-7 traffic proxying

It demonstrates practical understanding of real-world traffic management in distributed systems.

---
