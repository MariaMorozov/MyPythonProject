def userInput

pipeline {
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                dir('docker_api'){
                    script {
                        sh "docker build -t MyPythonProject ."
                    }
                }
            }
        }
        stage('Test Docker image') {
            steps {
                dir('docker_api/test') {
                    script{
                        sh "sh ./basic.tests.sh"
                    }
                }
            }
        }
        stage('Upload image to repository') {
            steps {
                sh "pwd"
            }
        }
        stage('Print Inputed string') {
            steps {
                println("Input was " + userInput)
            }
        }
    }
}