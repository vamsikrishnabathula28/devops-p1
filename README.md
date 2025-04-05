# Docker CI/CD Demo Application

A simple web application demonstrating Docker containerization and CI/CD with Jenkins.

## Features

- Flask web application
- Docker containerization
- Jenkins CI/CD pipeline
- Automated testing
- Continuous deployment

## Setup and Running

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will be available at http://localhost:8080

## Docker

Build and run with Docker:
```bash
docker build -t webapp-demo .
docker run -p 8080:8080 webapp-demo
```

## Jenkins Pipeline

The Jenkinsfile contains the CI/CD pipeline configuration:
- Build stage: Creates Docker image
- Test stage: Runs application tests
- Deploy stage: Deploys the application

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── Jenkinsfile        # Jenkins pipeline
└── templates/         # HTML templates
    └── index.html     # Main page template
```

## Prerequisites

- Docker installed on your system
- Jenkins server with Docker plugin installed
- Git for version control

## Local Development

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   python app.py
   ```

## Docker Build and Run

1. Build the Docker image:
   ```bash
   docker build -t webapp-demo .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 webapp-demo
   ```

The application will be available at http://localhost:5000

## CI/CD Pipeline

The Jenkinsfile defines a pipeline with the following stages:

1. **Build**: Creates a Docker image
2. **Test**: Runs basic tests on the container
3. **Deploy**: Tags the image and prepares for deployment

### Setting up Jenkins

1. Install Jenkins on your server
2. Install required plugins:
   - Docker Pipeline
   - Pipeline
   - Git
3. Configure Docker credentials in Jenkins
4. Create a new Pipeline job and point it to this repository

## Best Practices Implemented

- Multi-stage Docker builds to minimize image size
- Environment variable configuration
- Basic security considerations
- Automated testing in CI/CD pipeline
- Cleanup of Docker resources

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 