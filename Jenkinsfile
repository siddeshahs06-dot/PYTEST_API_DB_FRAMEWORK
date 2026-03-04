pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                "C:\\python.exe" --version
                "C:\\python.exe" -m pip install --upgrade pip
                "C:\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                "C:\\python.exe" -m pytest -v -s
                '''
            }
        }

    }
}
