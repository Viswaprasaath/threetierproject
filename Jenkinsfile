pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                git branch: 'master',
                    url: 'https://github.com/Viswaprasaath/threetierproject.git'
            }
        }

        stage('Build frontend Image') {
            steps {
                sh '''
                    cd frontend
                    docker build -t viswaprasaath/threetier-frontend:latest .
                '''
            }
        }

        stage('Build backend Image') {
            steps {
                sh '''
                    cd backend
                    docker build -t viswaprasaath/threetier-backend:latest .
                '''
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                    docker push viswaprasaath/threetier-frontend:latest
                    docker push viswaprasaath/threetier-backend:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    export KUBECONFIG=/var/lib/jenkins/.kube/config
                    kubectl apply -f kube/
                '''
            }
        }
    }
}
