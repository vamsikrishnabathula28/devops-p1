# 🚀 Docker Jenkins CI/CD Demo

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://www.jenkins.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

## 📋 Project Overview

This project demonstrates a complete CI/CD pipeline using Docker and Jenkins. It showcases modern DevOps practices and tools while implementing industry best practices for containerization, automation, and deployment.

### 🌐 Application Access

The application is accessible at: [http://localhost:5000](http://localhost:5000)

### 🎯 Key Features

- **Containerization**
  - Docker containerization
  - Multi-container application support
  - Container health monitoring
  - Automated container deployment

- **CI/CD Pipeline**
  - Jenkins automation
  - Automated testing
  - Continuous deployment
  - Pipeline visualization

- **Application Features**
  - Flask web application
  - RESTful API endpoints
  - Health check endpoints
  - Performance monitoring

## 🛠️ Technology Stack

### Core Technologies
- **Docker**: Containerization and orchestration
- **Jenkins**: CI/CD automation
- **Python**: Application development
- **Flask**: Web framework

### Testing & Quality
- **Pytest**: Unit testing
- **Jenkins Pipeline**: Automated testing
- **Code Quality**: Linting and style checks

## 📁 Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── Jenkinsfile        # Jenkins pipeline
└── templates/         # HTML templates
    └── index.html     # Main page template
```

## 🚀 Getting Started

### Prerequisites
- Docker
- Jenkins
- Python 3.8+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vamsikrishnabathula28/docker-jenkins-cicd-demo.git
   cd docker-jenkins-cicd-demo
   ```

2. Build the Docker image:
   ```bash
   docker build -t flask-app .
   ```

3. Run the container:
   ```bash
   docker run -d -p 5000:5000 --name flask-app-container flask-app
   ```

## 📸 Application Output Examples

### Docker Container Status
```bash
$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                    NAMES
abc123def456   flask-app      "python app.py"          2 minutes ago   Up 2 minutes   0.0.0.0:5000->5000/tcp   flask-app-container
```

### Container Logs
```bash
$ docker logs flask-app-container
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

### Application API Response
```bash
$ curl http://localhost:5000/api/health
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2024-03-14T12:00:00Z"
}
```

## 🔄 CI/CD Pipeline

The Jenkinsfile defines a pipeline with the following stages:

1. **Build**: Creates a Docker image
2. **Test**: Runs application tests
3. **Deploy**: Tags and pushes the image

### Setting up Jenkins

1. Install Jenkins on your server
2. Install required plugins:
   * Docker Pipeline
   * Pipeline
   * Git
3. Configure Docker credentials in Jenkins
4. Create a new Pipeline job and point it to this repository

## 🎯 Best Practices

- Containerization
- Automated Testing
- Continuous Integration
- Continuous Deployment
- Code Quality
- Documentation
- Security
- Monitoring

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vamsi Krishna Bathula**
- GitHub: [@vamsikrishnabathula28](https://github.com/vamsikrishnabathula28)

## 🙏 Acknowledgments

- Docker Community
- Jenkins Community
- Open Source Community 