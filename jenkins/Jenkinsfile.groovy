def userInput

pipeline {
    agent {
        label 'docker-node'
    }

    stages {
        stage('Build Docker image') {
            steps {
                dir('docker_api'){
                    script {
                        sh "sudo docker build -t mypythonproject ."
                    }
                }
            }
        }
        stage('Test Docker image') {
            steps {
                dir('docker_api/tests') {
                    script{
                        sh "./basic.tests.sh"
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
                println("Empty " )
            }
        }
    }
}