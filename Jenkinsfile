pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'webapp-demo'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} python -c "import flask; print('Flask import successful')"
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                    # Add your deployment commands here
                    # For example: docker push to a registry
                '''
            }
        }
    }
    
    post {
        always {
            sh 'docker system prune -f'
        }
    }
} 