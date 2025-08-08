# Smart Wellness Tracker – End-to-End MLOps Project

> Predict wellness scores using simulated health data heart rate, sleep hours via containerized, orchestrated, and monitored MLOps pipeline.

# Architecture

<img width="872" height="39" alt="Image" src="https://github.com/user-attachments/assets/c97666ef-ec11-4944-a064-4f9f4181e632" />
<img width="500" alt="Architecture Overview" src="https://github.com/user-attachments/assets/a333e4aa-2263-4aa4-aec1-039bb623542c" />



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

