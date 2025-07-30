# 🐍 Django App - Containerized & Kubernetes-Ready

A Django web application packaged with Docker, tested via GitHub Actions CI/CD, and deployed with Helm into Kubernetes.

---

## 📘 Project Overview

This project is a Django-based web application with:

- Docker containerization
- GitHub Actions CI/CD pipeline
- PostgreSQL database integration
- Kubernetes deployment using Helm
- Secure environment variable management via ConfigMap and Secrets

---

## 🔌 API Usage Examples

> Example: `GET /api/posts/`

```json
[
  {
    "id": 1,
    "title": "Hello World",
    "content": "This is a post.",
    "published": true
  }
]
