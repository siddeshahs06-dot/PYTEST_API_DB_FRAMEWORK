pipeline {
    agent any

    stages {

stage('Install Dependencies') {
    steps {
        bat '''
        python --version
        pip --version
        pip install --upgrade pip
        pip install -r requirements.txt
        '''
    }
}
    }
}
