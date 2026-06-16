pipeline {
    agent any

    environment {
        HF_USERNAME = "jenkins96"
        HF_SPACE = "fastapi-demo"
    }

    stages {
        

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy to Hugging Face') {
            steps {
                withCredentials([
                    string(credentialsId: 'hf-token', variable: 'HF_TOKEN')
                ]) {
                    sh '''
                        git config --global user.email "jenkins@example.com"
                        git config --global user.name "Jenkins"

                        git remote remove hf || true

                        git remote add hf \
                        https://${HF_USERNAME}:${HF_TOKEN}@huggingface.co/spaces/${HF_USERNAME}/${HF_SPACE}

                        git push hf HEAD:main --force
                    '''
                }
            }
        }
    }
}