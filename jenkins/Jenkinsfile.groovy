def userInput

pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                dir('CoolNewDirectory') {
                    git branch: 'main', credentialsId: 'github_cred', url: 'https://github.com/MariaMorozov/MyPythonProject.git'
                    echo 'Check working dir'
                }
            }
        }
        stage('Check Working Directory') {
            steps {
                sh "pwd"
            }
        }
    }
}