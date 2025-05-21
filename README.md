# Status Monitor

A full-stack DevOps project to simulate real-world CI/CD and GitOps practices.

## 🧰 Tech Stack
- **Frontend**: React (Status UI)
- **Backend**: FastAPI or Flask (Health API)
- **CI/CD**: GitHub Actions
- **GitOps**: Argo CD
- **Kubernetes**: Minikube #no fund to AWS :(
- **Docker**: Containerized microservices

## 🚀 Features
- Auto-deploy to K8s via Argo CD
- CI/CD with GitHub Actions
- Frontend fetches live service status from backend
- Deployable in local environment (Minikube)

## 📦 Structure
devops-gitops-status-monitor/
├── backend/
│   ├── app/
│   │   └── main.py  # Health check API
│   └── Dockerfile
├── frontend/
│   ├── public/
│   ├── src/
│   │   └── App.jsx
│   └── Dockerfile
├── manifests/
│   ├── backend/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── frontend/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── ingress.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yaml  
├── README.md
└── argo-cd/
    └── app.yaml  


## 🛠️ Setup Instructions
> Will be filled after project progress
