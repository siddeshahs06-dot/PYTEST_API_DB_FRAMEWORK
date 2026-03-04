pipeline {
    agent any
    stages {
        stage('Upgrade Pip') {
            steps {
                bat 'python -m pip install --upgrade pip'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
    }
}
