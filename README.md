# 🐍 Python Web App with Docker, Helm & GitHub Actions


---

## 📁 Project Structure

```
├── app # Python application code
│   ├── Dockerfile # Docker image build definition
│   ├── main.py # Entry point of the app
│   └── requirements.txt # Python dependencies
├── .github
│   └── workflows
│   └── myjob.yaml # GitHub Actions workflow for CI/CD
├── k8s
│   └── python-web-app-chart # Helm chart for Kubernetes
│   ├── Chart.yaml # Helm chart metadata
│   ├── .helmignore # Ignore rules for packaging
│   ├── templates/ # Kubernetes resource templates
│   │   ├── deployment.yaml
│   │   ├── _helpers.tpl
│   │   ├── hpa.yaml
│   │   ├── ingress.yaml
│   │   ├── NOTES.txt
│   │   ├── serviceaccount.yaml
│   │   ├── service.yaml
│   │   └── tests/
│   │   └── test-connection.yaml
│   └── values.yaml # Default Helm values
└── README.md # Project documentation
```
# Python Flask Web App

## Overview

This is a simple Python Flask web application that responds to a `GET` request with a message including the application version and the latest commit SHA.


- **Version A, B, C** values are dynamically set by the GitHub Actions workflow.
- **Commit SHA** is automatically updated after each new commit.

## Project Structure

```
├── app # Python application code
│   ├── Dockerfile # Docker image build definition
│   ├── main.py # Entry point of the app
│   └── requirements.txt # Python dependencies
```

# Github Workflow 

## Overview


## 📂 Workflow File: `.github/workflows/ci-cd.yaml`

```
├── .github
│   └── workflows
│   └── myjob.yaml # GitHub Actions workflow for CI/CD
```
This GitHub Actions workflow automates the CI/CD process for a Python web application using Docker, Helm, and GitHub Container Registry 

- Builds a Docker image from the application
- Tags it with version and commit hash
- Pushes it to GHCR
- Updates the Kubernetes Helm chart's `values.yaml`
- Commits and pushes back the changes
- Packages and pushes the Helm chart to GHCR as an OCI package

### 🧱 Trigger

This workflow is triggered **on push** to the `main` branch:

```yaml
on:
  push:
    branches:
      - main

