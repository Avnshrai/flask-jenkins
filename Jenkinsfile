def img
pipeline {
    // setting up dockhub information needed to push image.
    environment {
        registry = "avnshrai/project1"
        registrycredential = 'docker-hub-login'
        dockerimage = ''
    }
    agent any
    // first step is to download git file
    stages {
        stage('download') {
            steps {
                git 'https://github.com/Avnshrai/flask-jenkins.git'
                echo 'Finshed downloading git'
                sh "docker stop project1"
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
//         stage('Build test Image') {
//             steps {
//                 sh "docker build -f Dockerfile.test -t test ."
//             }
//         }

        stage('Test File') {
           steps {
                // Run venv
                echo 'Running test'
                // sh "docker run -d -p 5000:5000 ${img}"
                sh 'pip install -r requirements.txt'
                sh 'python3 test.py'
          }
        }

        // stage('stop container') {
        //    steps {
        //     sh "docker stop project1"
        //   }
        // }


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

    post {
        always {
            emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }
    }
}
