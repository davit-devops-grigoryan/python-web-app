# Python Web App with Docker, Helm & GitHub Actions

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


# 🚀 Python Web App CI/CD with Helm & GitHub Actions

This repository contains a Python web application deployed using Kubernetes and Helm, with CI/CD powered by GitHub Actions.

## 🛠 GitHub Actions: Modify Helm Values & Inject App Version

A GitHub Actions job automatically modifies the `values.yaml` file inside the Helm chart before deployment. It updates:

- Docker image name and tag
- Application version details (`a`, `b`, `c`)
- Commit SHA

These values are passed into the web application and rendered in the HTTP response.

### 🔧 Workflow Snippet

```yaml
- name: Modify image name and tag in values.yaml, also pass env variable in python web app, for visualize in http responce
  run: |
    yq e '.image.repository = "ghcr.io/${{ github.repository }}/myapp"' -i k8s/python-web-app-chart/values.yaml
    yq e '.image.tag =  "'"${{ env.TAG }}_${{ env.COMMIT_SHA }}"'"' -i k8s/python-web-app-chart/values.yaml
    yq e '.version.a = ${{ env.VERSION_A }}' -i k8s/python-web-app-chart/values.yaml
    yq e '.version.b = ${{ env.VERSION_B }}' -i k8s/python-web-app-chart/values.yaml
    yq e '.version.c = ${{ env.VERSION_C }}' -i k8s/python-web-app-chart/values.yaml
    yq e '.version.commitSha = "${{ env.COMMIT_SHA }}"' -i k8s/python-web-app-chart/values.yaml


## 📦 CI/CD Pipeline and Runner Setup

This repository is already configured with a GitHub Actions self-hosted runner.

### ✅ Runner Information

If you open the repository **Settings > Actions > Runners**, you'll find a **registered runner** that is ready to execute workflows.

Runner-host located in GCP

You can **test the CI/CD pipeline** by pushing changes to the `main` branch or triggering workflows manually (depending on the workflow configuration).

### 🔐 Commit Guidelines

When committing any changes that interact with workflows or push to the repository from scripts or CI:

- **Always use a GitHub access token**.
- Make sure your token has the required permissions:
  - `contents: write`
  - `packages: write`
  - `id-token: write`
  - `attestations: write`

Using a token ensures that your actions are authenticated and workflows execute properly.

---
