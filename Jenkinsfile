pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'flask-app'
        DOCKER_TAG = 'latest'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} python -c "import app; print(\'Flask app imported successfully\')"'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo "Deployment stage - In a real environment, this would push to a registry and deploy to a server"'
                sh 'docker run -d -p 5000:5000 --name flask-app-container ${DOCKER_IMAGE}:${DOCKER_TAG} || true'
                sh 'docker stop flask-app-container || true'
                sh 'docker rm flask-app-container || true'
                sh 'docker run -d -p 5000:5000 --name flask-app-container ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }
    }
    
    post {
        always {
            sh 'docker ps -a | grep flask-app-container || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
} 