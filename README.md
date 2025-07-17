
# ⚙️ Random Chat — Backend

*Real-time Django WebSocket backend built with Django Channels + Redis. Powers the terminal-style frontend for anonymous chat rooms.*

---

## 🧠 Overview

This is the backend engine behind [**Random Chat**](https://github.com/jztchl/random-chat-front_end/) — a real-time, terminal-style anonymous chat app.

Features:

* 🔥 WebSocket chat per room using **Django Channels**
* 🏗️ Create + list public chat rooms (via REST API)
* 📊 Tracks active users per room
* ⚙️ **Redis-based** Channels layer for full async & scale-ready ops

---

## ⚒️ Tech Stack

| Layer          | Stack                        |
| -------------- | ---------------------------- |
| Backend        | Django + Django Channels     |
| Realtime       | ASGI + WebSocket Protocol    |
| Channels Layer | Redis (via Django Channels)  |
| Deployment     | RDS & Render / Railway Ready |

---

## 📦 Features

* ✅ WebSocket-based chat per room
* ✅ REST API to create + list rooms
* ✅ Scalable **Redis channel layer**
* ✅ Tracks active users in memory (or optional DB mode)
* ✅ RDS-compatible (PostgreSQL or similar)
* ✅ **Production-ready ASGI setup**

---

## 🧪 API Endpoints

| Method | Endpoint        | Description              |
| ------ | --------------- | ------------------------ |
| POST   | `/create_room/` | Create new chat room     |
| GET    | `/list_rooms/`  | List all available rooms |

---

## 📡 WebSocket Endpoint

> Endpoint: `/ws/chat/<room_name>/`

**Client sends:**

```json
{
  "message": {
    "message": "Hello World",
    "nick_name": "Neo"
  }
}
```

**Server broadcasts to all clients in that room:**

```json
{
  "message": {
    "message": "Hello World",
    "nick_name": "Neo"
  }
}
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/random-chat-backend.git
cd random-chat-backend
```

---

### 2. Set up virtualenv

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
REDIS_URL=redis://localhost:6379
DATABASE_URLS=example.com

```

---

### 5. Apply migrations

```bash
python manage.py migrate
```

---

### 6. Run local server (ASGI mode)

Use **Daphne** or **Uvicorn** to run ASGI properly:

```bash
daphne randomchat.asgi:application
# or
uvicorn randomchat.asgi:application
```

---

## 🌐 Production Setup (Render / Railway / EC2)

> Use **Redis** for Channels layer and **Daphne or Uvicorn** as ASGI server.

### ✅ `asgi.py` entrypoint

Make sure your project has:

```python
# randomchat/asgi.py

import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'randomchat.settings')
django.setup()
application = get_default_application()
```

---

### ✅ `settings.py` Channels Setup

```python
# Installed apps
INSTALLED_APPS = [
    ...
    'channels',
    'chat',
]

# ASGI
ASGI_APPLICATION = 'randomchat.asgi.application'

# Redis-based channel layer
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.getenv("REDIS_URL", "redis://localhost:6379")],
        },
    },
}
```

---

## 🧪 Dev Testing

Use [Hoppscotch](https://hoppscotch.io/websocket) or your frontend to test:

```bash
```

---

## 📁 Project Structure

```txt
randomchat/
├─ chat/
│  ├─ consumers.py     # WebSocket logic
│  ├─ views.py         # Room APIs
│  ├─ routing.py       # WebSocket URLs
│  ├─ models.py        # Room model (optional)
│
├─ randomchat/
│  ├─ asgi.py          # ASGI app
│  ├─ settings.py
│  └─ urls.py
│
├─ requirements.txt
├─ manage.py
└─ .env
```

---

## ⚙️ Redis + Render/Production Setup

* Add **Redis** to Render or Railway
* Set `REDIS_URL` in your env
* Deploy using `daphne randomchat.asgi:application` or similar

---

## 📄 License

MIT — fork it, build on it, scale it.

