# Mini F5 – Layer-7 Load Balancer

This project implements a minimal **Application Delivery Controller (ADC)** using **NGINX** as a Layer-7 reverse proxy and multiple **FastAPI** backend services.
It demonstrates how modern load balancers such as **F5 BIG-IP LTM** distribute traffic, monitor health, and proxy application requests in real-world microservice environments.

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

NGINX acts as the **virtual server** and load-balancer.
FastAPI containers act as **pool members**.

All traffic enters through NGINX and is forwarded to one of the backend services.

---

## Features Implemented

* Layer-7 reverse proxy (NGINX)
* Round-robin load balancing
* Multiple backend pool members
* Per-backend request counters
* Health check endpoint (`/health`)
* Fully containerized using Docker
* Single-command startup using Docker Compose

---

## Technology Stack

* NGINX (reverse proxy and load balancer)
* FastAPI (backend services)
* Docker
* Docker Compose

---

## Backend Service Behavior

Each backend instance returns:

* Its container hostname
* A request counter
* A simple response message

This makes it easy to observe which backend handled each request.

---

## How to Run

Build the backend image:

```bash
cd backends
docker build -t fastapi-backend .
```

Start the full system:

```bash
cd ..
docker compose up
```

Access the load balancer:

```
http://localhost
```

Every request is routed through NGINX and forwarded to one of the backend services.

---

## Verifying Load Balancing

Use curl to force new TCP connections:

```bash
curl http://localhost
curl http://localhost
curl http://localhost
```

The `hostname` field in the response should rotate between backend containers.

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

This project demonstrates, in a minimal and reproducible way, how enterprise-grade ADCs such as **F5 BIG-IP LTM** operate:

* Virtual servers
* Backend pools
* Load-balancing algorithms
* Layer-7 request proxying

It provides hands-on evidence of understanding how production traffic is routed in modern distributed systems.
