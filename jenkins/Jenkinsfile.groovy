def userInput

pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Check working dir'
            }
        }
        stage('Check Working Directory') {
            steps {
                sh "pwd"
            }
        }
    }
}