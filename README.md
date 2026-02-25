# Uptime Monitor

A simple uptime monitoring app that lets you check if a website is reachable.

This project was built to learn cloud deployment, Docker, and AWS ECS.

---

## 🚀 Live Demo


http://13.217.33.231:8000/monitor


> Note: The IP may change when the container restarts.

---

## 📌 Features

- Enter a URL and check if it’s up
- Shows HTTP status (like 200, 404, etc.)
- Simple one-page UI
- Dashboard for multiple targets
- Deployed to AWS ECS Fargate using Docker

---

## 🛠 Tech Stack

- Python
- FastAPI
- Docker
- AWS ECS Fargate
- Amazon ECR
- HTML + JavaScript

---

## 🧠 What I Learned

- How to containerize an app with Docker
- How to push images to AWS ECR
- How to run containers on ECS Fargate
- How networking works (ENI, public IPs, security groups)
- How to debug deployment issues

---

## 📂 Project Structure


uptime-monitor/
├── app/
│ ├── main.py
│ └── monitor.py
├── Dockerfile
├── requirements.txt
└── task-def.json


---

## ▶️ Run Locally

### 1. Clone the repo


git clone https://github.com/alvinmdancy/uptime-monitor.git

cd uptime-monitor


### 2. Create virtual environment


python -m venv .venv
source .venv/bin/activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Start the app


uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/monitor


---

## 🐳 Run with Docker


docker build -t uptime-monitor .
docker run -p 8000:8000 uptime-monitor


---

## ☁️ Deployment Overview

1. Build Docker image  
2. Push image to AWS ECR  
3. Run task on ECS Fargate  
4. Access via public IP  

---

## ⚠️ Notes

- This project uses in-memory storage, so data resets when the container restarts.
- Public IP changes when the ECS task restarts.
- Future improvement: add a load balancer and database.

---

## 📈 Future Improvements

- Stable URL using Load Balancer
- Store targets in DynamoDB
- Response time tracking
- Better UI styling
- CI/CD with GitHub Actions

---

## 👤 Author

**Alvin Dancy**  
https://github.com/alvinmdancy
