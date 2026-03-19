# 🚀 Distributed Rate Limiter (FastAPI + Redis)

A production-style distributed rate limiter built using **FastAPI**, **Redis**, and **Lua scripting**.
Designed to handle concurrent requests safely with atomic operations and scalable architecture.

---

## 🧠 Features

* ⚡ Sliding Window Rate Limiting (accurate + fair)
* 🔒 API Key based limits (multi-tenant ready)
* 🧩 FastAPI Middleware integration (automatic enforcement)
* 🧠 Redis + Lua for atomic operations (no race conditions)
* 🐳 Fully Dockerized setup
* 📊 Real-time request tracking using Redis sorted sets

---

## 🏗️ Architecture

Client → FastAPI → Rate Limiter Middleware → Redis (Lua Script)

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Database:** Redis
* **Scripting:** Lua (for atomic rate limiting)
* **Containerization:** Docker + Docker Compose

---

## 📦 Project Structure

```
rate_limiter/
├── app/
│   ├── main.py
│   ├── middleware.py
│   ├── limiter.py
│   ├── redis_client.py
│   ├── api_keys.py
│   ├── lua/
│   │   └── sliding_window.lua
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone https://github.com/Aravind226/Rate-Limiting-Middleware.git
cd rate_limiter
```

---

### 2. Run with Docker

```
docker-compose up --build
```

---

### 3. Access the API

```
http://localhost:8000
```

---

## 🔑 API Usage

### Request

```
curl http://localhost:8000 \
  -H "x-api-key: free_key_123"
```

---

## 📊 Rate Limits

Defined in `app/api_keys.py`:

| API Key      | Limit | Window |
| ------------ | ----- | ------ |
| free_key_123 | 5     | 60 sec |
| pro_key_456  | 50    | 60 sec |

---

## 🧠 How It Works

* Each request is intercepted by middleware
* A unique key is generated:

  ```
  rate_limit:{api_key}:{route}
  ```
* Redis stores timestamps in a **sorted set**
* Lua script:

  * removes expired entries
  * counts current requests
  * decides allow/block

---

## 🔥 Example Response Headers

```
X-RateLimit-Limit: 5
X-RateLimit-Remaining: 2
```

---

## ⚠️ Important Notes

* Redis hostname must be:

  * `redis` (inside Docker)
  * `localhost` (if running locally)
* Sliding window = last N seconds, not fixed intervals

---

## 🧪 Testing Rate Limits

```
for i in {1..10}; do
  curl http://localhost:8000 \
    -H "x-api-key: free_key_123"
done
```

Expected:

* First 5 requests → ✅ allowed
* Next requests → ❌ 429 Too Many Requests

---

## 🧠 Future Improvements

* Persistent API key storage (PostgreSQL)
* Dashboard for analytics
* Distributed Redis cluster support
* Burst + sustained rate limiting
* Per-user + per-IP limits

