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
