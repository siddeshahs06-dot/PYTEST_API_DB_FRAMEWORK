pipeline {
    agent any
    stages {
        stage('Test Python') {
            steps {
                bat 'where python'
                bat 'python --version'
                bat 'python -c "print(123)"'
            }
        }
    }
}
