pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                "C:\\Program Files\\Python311\\python.exe" --version
                "C:\\Program Files\\Python311\\python.exe" -m pip install --upgrade pip
                "C:\\Program Files\\Python311\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                "C:\\Program Files\\Python311\\python.exe" -m pytest -v -s
                '''
            }
        }

    }
}
