pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'staging', 'prod'], description: 'Select environment')
    }

    stages {
        stage('Set Environment Variables') {
            steps {
                script {
                    if (params.ENV == "dev") {
                        env.ENV = "Development"
                        env.MESSAGE = "Hello Developer!"
                    } else if (params.ENV == "staging") {
                        env.ENV = "Staging"
                        env.MESSAGE = "Testing in progress..."
                    } else if (params.ENV == "prod") {
                        env.ENV = "Production"
                        env.MESSAGE = "Welcome, End User!"
                    }
                }
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 greet.py'
            }
        }
    }
}