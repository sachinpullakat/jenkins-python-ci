pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Checking Python and Git'
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated unit tests'
                bat 'python -m unittest -v test_app.py'
            }
        }

        stage('Build') {
            steps {
                echo 'Generating build report'
                bat 'echo Python CI Pipeline - BUILD SUCCESSFUL > build-report.txt'
                bat 'echo Unit tests executed by Jenkins >> build-report.txt'
                archiveArtifacts artifacts: 'build-report.txt,app.py,test_app.py',
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Pipeline completed!'
        }
        failure {
            echo 'FAILURE: Check Console Output.'
        }
    }
}
