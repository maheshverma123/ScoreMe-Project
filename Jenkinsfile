pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar_id')  // Ensure this matches your secret token ID in Jenkins
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository from GitHub and specify the branch explicitly
                git branch: 'main', url: 'https://github.com/maheshverma123/ScoreMe-Project.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    script {
                        // Running sonar-scanner with token from environment
                        sh '''
                            echo "Running SonarQube analysis..."
                            /opt/sonar-scanner/bin/sonar-scanner -X \
                            -Dsonar.projectKey=scoreme \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://3.94.197.71:9000/ \
                            -Dsonar.login=${SONAR_TOKEN}
                        '''
                    }
                }
            }
        }

        stage('Security Check - OWASP Dependency-Check') {
            steps {
                echo "Running OWASP Dependency-Check..."
                sh '''
                    docker run --rm -v /home/ec2-user/ScoreMe-Project:/project -v /home/ec2-user/output:/output owasp/dependency-check \
                    --scan /project --out /output -l /output/dependency-check.log --nvdApiKey c122cc92-2617-46e7-bedd-c74bd3a9b3bf
                '''
            }
        }

        stage('Code Quality - Lizard Cyclomatic Complexity') {
            steps {
                echo "Running Lizard Cyclomatic Complexity..."
                // Run lizard directly, no Docker needed
                sh '''
                    lizard ${WORKSPACE}
                '''
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    def qg = waitForQualityGate()  // Wait for the quality gate status
                    if (qg.status != 'OK') {
                        error "Quality Gate failed: ${qg.status}"  // Stop the pipeline if quality gate fails
                    }
                }
            }
        }
    }
    post {
        success {
            slackSend (
                channel: '#devops', 
                color: 'good', 
                message: "Build Successful: ${env.JOB_NAME} - ${env.BUILD_NUMBER}"
            )
        }
        failure {
            slackSend (
                channel: '#devops', 
                color: 'danger', 
                message: "Build Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}"
            )
        }
        always {
            echo "Pipeline finished"
        }
    }
}
