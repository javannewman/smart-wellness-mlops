# Smart Wellness Tracker – End-to-End MLOps Project

> Predict wellness scores using simulated health data heart rate, sleep hours via containerized, orchestrated, and monitored MLOps pipeline.

# Architecture
[ generate.py ] 
       │
       ▼
[ data/wellness.csv ] ⇄ [ DVC + MinIO (S3) ]
       │
       ▼
[ train.py ] ───► [ MLflow ]
       │
       ▼
[ model.joblib ]
       │
       ▼
[ FastAPI + Docker ]
       │
       ▼
[ Kubernetes (Minikube) ]
       │
       ▼
[ Prometheus + Grafana ]


## Tools

| Category             | Tools                                              
|----------------------|-------------------------------------------
| Version Control      | Git + GitHub                                       
| Data Versioning      | DVC + MinIO (via S3 protocol)                      
| Experiment Tracking  | MLflow (local file system backend)                
| ML Framework         | scikit-learn                                       
| Serving              | FastAPI + Uvicorn                                  
| Containerization     | Docker                                             
| Deployment           | Kubernetes & Docker   
| Monitoring           | Prometheus + Grafana                               
---

## 📁 Project Structure

smart-wellness-mlops/
│
├── app/
│ ├── main.py # FastAPI app
│ └── train.py # Training + MLflow logging
│
├── data/ # Raw DVC versioned data
├── models/ # Saved models (joblib)
├── pipelines/ # (Optional) Prefect flows
├── k8s/
│ └── deployment.yaml # K8s deployment + service
├── Dockerfile # FastAPI container
├── generate_data.py # Simulate IoT health data
├── requirements.txt
├── dvc.yaml
├── mlruns/ # Local MLflow tracking
└── README.md

