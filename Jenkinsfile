pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-management-flask .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 --name flask-app student-management-flask
                '''
            }
        }
    }
}
