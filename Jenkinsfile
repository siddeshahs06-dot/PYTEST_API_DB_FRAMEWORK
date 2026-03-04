pipeline {
    agent any

    stages {

        stage('Install Requirements') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v -s --html=report.html'
            }
        }
    }
}
