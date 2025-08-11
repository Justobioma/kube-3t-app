# 🚀 Kubernetes 3-Tier Application Deployment
This repository contains a complete 3-tier application architecture deployed on Kubernetes using Minikube. It includes:

- **Frontend**: A Node.js app served via Docker and exposed through a Kubernetes Service
- **Backend**: A FastAPI application containerized and deployed via Kubernetes
- **Ingress**: An NGINX Ingress controller routing traffic to the appropriate services

---
## 📁 Folder Structure
. ├── frontend/ │   ├── Dockerfile │   ├── frontend.yaml │   ├── frontend-service.yaml │   └── [Node.js app files] ├── backend/ │   ├── Dockerfile │   ├── backend.yaml │   ├── backend-service.yaml │   └── [FastAPI app files] ├── ingress/ │   └── ingress.yam

---
## 🧱 Architecture Overview
[Browser] | [Ingress Controller] |         | [/api]     [/] |         | [Backend]  [Frontend] | [Optional: Database]---

---
## 🛠️ Prerequisites

- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/)
- Admin access for running `minikube tunnel`

---
## 🚀 Deployment Steps

### 1. Start Minikube

```bash
minikube start --driver=hyperv --memory=2048 --cpus=2 --hyperv-virtual-switch="MinikubeSwitch"

```
### 2. Enable Ingress Addon

```bash
minikube addons enable ingress
```
### 3. Use Minikube’s Docker Daemon

```bash
eval $(minikube docker-env)
```
### 4. Build Docker Images (Optional if already pushed to Docker Hub)

```bash
docker build -t your-dockerhub-username/frontend-app ./frontend
docker build -t your-dockerhub-username/backend-app ./backend
```
### 5. Apply Kubernetes Manifests

```bash
kubectl apply -f frontend/frontend.yaml
kubectl apply -f frontend/frontend-service.yaml

kubectl apply -f backend/backend.yaml
kubectl apply -f backend/backendservice.yaml

kubectl apply -f ingress/ingress.yaml
```
### 6. Start Minikube Tunnel

```bash
minikube tunnel
```
⚠️ Run this in a separate terminal with admin privileges.

### 7. Add Host Entry (Optional)

```bash
echo "$(minikube ip) backend.local" | sudo tee -a /etc/hosts
```
### 🌐 Access the App
- Frontend: http://backend.local/
- Backend API: http://backend.local/api/greet

### 📦 Docker Images
- Frontend: 
- Backend: 

### 📘 Resources
- Kubernetes Ingress Docs
- FastAPI Deployment Guide
- Node.js Docker Best Practices

### 🙌 Author
Obioma
DevOps Enthusiast | Cloud Architect in Training 🚀
Feel free to connect or contribute!

### 📜 License
This project is licensed under the MIT License.

---



