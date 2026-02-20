 EduManage Pro – DevOps Powered Student Management System

EduManage Pro is a Flask-based Student Management System deployed using a complete DevOps workflow including Infrastructure as Code, Containerization, CI/CD automation, Cloud hosting, and Monitoring.



 Live Application

🔗 http://13.233.237.42:5000  
 (Update EC2 IP if changed)



 Architecture

Developer → GitHub → Jenkins (CI/CD) → Docker → AWS EC2 → Prometheus → Grafana


 Tech Stack

- Backend: Python (Flask)
- Database: SQLite
- Containerization: Docker
- Infrastructure: Terraform
- Cloud: AWS EC2
- CI/CD: Jenkins
- Monitoring: Prometheus + Grafana
- Version Control: Git & GitHub



 Project Structure


student-management-flask/
├── app.py
├── templates/
├── static/
├── docker/Dockerfile
├── terraform/
├── monitoring/
├── Jenkinsfile
└── README.md




 Features

- Admin Authentication
- Student CRUD Operations
- File Upload (Photo & Documents)
- Dashboard Analytics
- Dockerized Deployment
- Automated CI/CD
- Infrastructure as Code
- Monitoring & Observability

---

 Docker


docker build -t student-management-app .
docker run -d -p 5000:5000 student-management-app
 Terraform

Provisioned Resources:

VPC

Public Subnet

Internet Gateway

Route Table

Security Group

EC2 Instance (Ubuntu)

Key Pair

Docker Installation via User Data

Public IP Assignment

terraform init
terraform plan
terraform apply
terraform destroy

CI/CD Pipeline

Every Git push triggers:

Code checkout

Docker image build

Deployment to EC2

Automatic container restart

Pipeline defined in Jenkinsfile.

Monitoring

Monitoring stack deployed via Docker Compose.

Service	Port
Prometheus	9090
Grafana	3000
Node Exporter	9100
cd monitoring
docker compose up -d


Security

Admin-only access

AWS Security Groups

SSH Key Pair authentication

Infrastructure isolation via VPC

Container isolation via Docker

 Author

Geo Mathew George
GitHub: https://github.com/geomg21

LinkedIn: https://www.linkedin.com/in/geo-mathew-george-27a857314
