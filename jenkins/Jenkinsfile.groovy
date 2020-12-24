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
                        sh "sudo chmod 755 basic.tests.sh"
                        sh "./basic.tests.sh"
                    }
                }
            }
        }

     }
}