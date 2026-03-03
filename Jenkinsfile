pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/siddeshahs06-dot/PYTEST_API_DB_FRAMEWORK.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v -s'
            }
        }
    }
}
