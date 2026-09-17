pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Greatest of Two Numbers Program...'
                bat 'python greatest.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Greatest of Two Numbers Program...'
                bat 'python test_greatest.py'
            }
        }
    }
}