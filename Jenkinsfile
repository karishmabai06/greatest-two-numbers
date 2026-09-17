pipeline {
    agent any

    environment {
        // Your Python path on Windows
        PYTHON = 'C:/Users/Karis/AppData/Local/Programs/Python/Python313/python.exe'
    }

    parameters {
        string(name: 'NUM1', defaultValue: '10', description: 'First number')
        string(name: 'NUM2', defaultValue: '20', description: 'Second number')
        string(name: 'NUM3', defaultValue: '30', description: 'Third number')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Run the Python program with parameters
                    bat "\"%PYTHON%\" greatest_of_three.py ${params.NUM1} ${params.NUM2} ${params.NUM3}"
                }
            }
        }
    }
}

