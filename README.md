# 🚀 Enterprise-Grade Web Server Automation with Ansible

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

## 📋 Project Overview

This project demonstrates a complete DevOps workflow for deploying a scalable web server infrastructure using Infrastructure as Code (IaC) principles. It showcases modern DevOps practices and tools while implementing industry best practices for security, monitoring, and automation.

### 🎯 Key Features

- **Infrastructure as Code (IaC)**
  - Ansible playbooks for automated deployment
  - Version-controlled infrastructure
  - Reproducible environments
  - Configuration management

- **Container Orchestration**
  - Docker containerization
  - Multi-container application support
  - Container health monitoring
  - Automated container deployment

- **High Availability**
  - Load balancing configuration
  - Failover support
  - Service redundancy
  - Health checks

- **Security Implementation**
  - UFW firewall configuration
  - Secure Nginx setup
  - Docker security best practices
  - System hardening
  - Regular security updates

- **Monitoring & Logging**
  - Prometheus metrics collection
  - Grafana dashboards
  - Application logging
  - System metrics monitoring
  - Performance tracking

## 🛠️ Technology Stack

### Core Technologies
- **Ansible**: Configuration management and automation
- **Docker**: Containerization and orchestration
- **Nginx**: Reverse proxy and web server
- **Python Flask**: Web application framework

### Monitoring & Logging
- **Prometheus**: Metrics collection and storage
- **Grafana**: Visualization and dashboards
- **Node Exporter**: System metrics collection

### Security
- **UFW**: Firewall management
- **SSL/TLS**: Secure communication
- **Docker Security**: Container security

## 📁 Project Structure

```
ansible-project/
├── inventory/
│   └── hosts                 # Server inventory
├── roles/
│   ├── common/              # Basic server setup
│   ├── nginx/               # Nginx configuration
│   ├── docker/              # Docker installation
│   ├── webapp/              # Flask application
│   ├── firewall/            # Security configuration
│   └── monitoring/          # Monitoring setup
└── site.yml                 # Main playbook
```

## 🚀 Getting Started

### Prerequisites
- Ansible 2.9+
- Docker
- Python 3.8+
- Ubuntu 20.04 LTS (target servers)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vamsikrishnabathula28/ansible-web-server-deployment.git
   cd ansible-web-server-deployment
   ```

2. Update inventory:
   ```bash
   # Edit inventory/hosts with your server details
   nano inventory/hosts
   ```

3. Run the playbook:
   ```bash
   ansible-playbook -i inventory/hosts site.yml
   ```

## 📸 Application Output Examples

### Web Application Interface
![Web Application](https://raw.githubusercontent.com/vamsikrishnabathula28/docker-jenkins-cicd-demo/main/templates/index.html)

### Jenkins Pipeline Output
```bash
Started by user admin
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/docker-jenkins-cicd-demo
[Pipeline] {
  [Pipeline] stage
  [Pipeline] { (Build)
    [Pipeline] sh
    + docker build -t webapp-demo .
    Successfully built abc123def456
    Successfully tagged webapp-demo:latest
  }
  [Pipeline] stage
  [Pipeline] { (Test)
    [Pipeline] sh
    + docker run --rm webapp-demo python -m pytest
    ============================= test session starts ==============================
    collected 3 items
    test_app.py::test_home_page PASSED
    test_app.py::test_about_page PASSED
    test_app.py::test_contact_page PASSED
    ============================== 3 passed in 1.52s ==============================
  }
  [Pipeline] stage
  [Pipeline] { (Deploy)
    [Pipeline] sh
    + docker tag webapp-demo:latest webapp-demo:v1.0.0
    + docker push webapp-demo:v1.0.0
    The push refers to repository [webapp-demo]
    v1.0.0: Pushed
  }
}
[Pipeline] End of Pipeline
Finished: SUCCESS
```

### Docker Container Logs
```bash
$ docker logs webapp-demo
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

### Application API Response
```bash
$ curl http://localhost:8080/api/health
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2024-03-14T12:00:00Z"
}
```

### Load Balancer Status
```bash
$ curl http://localhost:8080/status
{
  "active_servers": 2,
  "total_requests": 1234,
  "average_response_time": "45ms",
  "server_status": {
    "web1": "healthy",
    "web2": "healthy"
  }
}
```

### Monitoring Dashboard
![Monitoring Dashboard](https://raw.githubusercontent.com/vamsikrishnabathula28/docker-jenkins-cicd-demo/main/templates/monitoring.png)

## 📸 Application Status and Troubleshooting

### Connection Status
```bash
$ curl -v http://localhost:8080
*   Trying 127.0.0.1:8080...
* connect to 127.0.0.1 port 8080 failed: Connection refused
* Failed to connect to localhost port 8080: Connection refused
* Could not resolve host: localhost
* Closing connection 0
curl: (7) Failed to connect to localhost port 8080: Connection refused
```

### Docker Container Status
```bash
$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                    NAMES
abc123def456   webapp-demo    "python app.py"          2 minutes ago   Up 2 minutes   0.0.0.0:8080->8080/tcp   webapp-demo
```

### Container Logs
```bash
$ docker logs webapp-demo
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:8080
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

### Troubleshooting Steps

1. Check if the container is running:
   ```bash
   docker ps | grep webapp-demo
   ```

2. Verify port mapping:
   ```bash
   docker port webapp-demo
   # Should show: 8080/tcp -> 0.0.0.0:8080
   ```

3. Check container logs for errors:
   ```bash
   docker logs webapp-demo
   ```

4. Test container connectivity:
   ```bash
   docker exec webapp-demo curl localhost:8080
   ```

5. Verify firewall settings:
   ```bash
   sudo ufw status
   # Should show: 8080/tcp ALLOW IN Anywhere
   ```

### Common Issues and Solutions

1. **Connection Refused Error**
   - Ensure the container is running: `docker start webapp-demo`
   - Check port conflicts: `netstat -tulpn | grep 8080`
   - Verify firewall rules: `sudo ufw allow 8080/tcp`

2. **Container Not Starting**
   - Check resource limits: `docker stats webapp-demo`
   - View detailed logs: `docker logs webapp-demo --tail 100`
   - Verify environment variables: `docker inspect webapp-demo`

3. **Application Not Responding**
   - Restart the container: `docker restart webapp-demo`
   - Check application logs: `docker logs webapp-demo -f`
   - Verify network connectivity: `docker network inspect bridge`

### Health Check Endpoint
```bash
$ curl http://localhost:8080/health
{
  "status": "healthy",
  "container_id": "abc123def456",
  "uptime": "2m 30s",
  "memory_usage": "45MB",
  "cpu_usage": "2.3%"
}
```

### Application Metrics
```bash
$ curl http://localhost:8080/metrics
{
  "requests_total": 156,
  "error_count": 0,
  "response_time_ms": 45,
  "active_connections": 3,
  "memory_usage_mb": 45,
  "cpu_usage_percent": 2.3
}
```

## 🔒 Security Features

- **Firewall Configuration**
  - UFW rules for essential ports
  - Default deny policy
  - IP whitelisting support

- **Nginx Security**
  - SSL/TLS configuration
  - Security headers
  - Rate limiting
  - DDoS protection

- **Docker Security**
  - Non-root containers
  - Resource limits
  - Network isolation
  - Image scanning

## 📊 Monitoring & Logging

### Metrics Collection
- System metrics (CPU, Memory, Disk)
- Application metrics
- Container metrics
- Network metrics

### Visualization
- Custom Grafana dashboards
- Real-time monitoring
- Alert configuration
- Performance tracking

## 🔄 CI/CD Integration

The project is designed to integrate with various CI/CD platforms:
- Jenkins
- GitHub Actions
- GitLab CI
- Azure DevOps

## 📈 Performance Optimization

- Nginx optimization
- Docker container optimization
- System resource management
- Load balancing configuration
- Caching strategies

## 🎯 Best Practices

- Infrastructure as Code (IaC)
- Configuration Management
- Automated Deployment
- Security Hardening
- Monitoring & Alerting
- High Availability
- Scalability
- Documentation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vamsi Krishna Bathula**
- GitHub: [@vamsikrishnabathula28](https://github.com/vamsikrishnabathula28)

## 🙏 Acknowledgments

- Ansible Community
- Docker Community
- Open Source Community 