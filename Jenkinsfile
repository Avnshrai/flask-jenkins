def img
pipeline {
    // setting up dockhub information needed to push image.
    environment {
        registry = "ecarmona1992/project1"
        registrycredential = 'docker-hub-login'
        dockerimage = ''
    }
    agent any
    // first step is to download git file
    stages {
        stage('download') {
            steps {
                git 'https://github.com/ecarmona1992/SimpleFlaskUI.git'
                echo 'Finshed downloading git'
                // force stop docker and clean up images
                sh "docker system prune -af"
            }
        }

        stage('Build Image') {
            steps {
                script {
                    // img = registry + ":${env.BUILD_ID}"
                    img = registry + ":${env.BUILD_ID}"
                    dockerImage = docker.build("${img}")
                }
            }
        }

        stage('Test File') {
           steps {
                // Run venv
                echo 'Running test'
                // sh "docker run -d -p 5000:5000 ${img}"
                sh "docker run -d -p 5000:5000 ${img}"
          }
        }

        stage('stop container') {
           steps {
            sh "docker stop ${img}"
          }
        }


        stage('Push To DockerHub') {
            steps {
                script {
                    docker.withRegistry( 'https://registry.hub.docker.com ', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }

    }
}