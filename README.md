# Smart Wellness Tracker – End-to-End MLOps Project

> Predict wellness scores using simulated health data heart rate, sleep hours via containerized, orchestrated, and monitored MLOps pipeline.

# Architecture


<img width="400" alt="Architecture Overview" src="https://github.com/user-attachments/assets/a333e4aa-2263-4aa4-aec1-039bb623542c" />



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

# Project Structure
<img width="802" height="554" alt="Image" src="https://github.com/user-attachments/assets/d64887c3-9319-4a78-9085-a0653e4d5fce" />

# DVC Push to MinIO aka S3

<img width="923" height="341" alt="Image" src="https://github.com/user-attachments/assets/39ba3242-bbe6-40de-8e36-6b41a44a6121" />

<img width="923" height="341" alt="Image" src="https://github.com/user-attachments/assets/94c3781c-3e87-4061-bcb2-be995c3b8882" />

# MLfLOW UI Experiment

<img width="955" height="356" alt="Image" src="https://github.com/user-attachments/assets/29c8a39e-e797-42a1-bae4-8936cce86742" />