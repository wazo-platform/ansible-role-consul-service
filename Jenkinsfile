pipeline {

  agent none

  stages {

    stage ('Lint') {
      agent {
        label 'molecule-aws-debian13-small'
      }
      steps {
        script { checkout scm }
          sh 'tox -e linters'
      }
      post {
        always {
          cleanWs()
        }
      }
    }

    stage ('Test') {
      parallel {
        stage ('Debian 11 & 12 / Ansible 8') {
          agent {
            label 'molecule-aws-debian12-small'
          }
          steps {
            script { checkout scm }
            withCredentials([
                [$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS Jenkins community'],
            ]) {
              sh "aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 119948825560.dkr.ecr.eu-west-1.amazonaws.com"
              sh 'tox -e molecule-ansible8'
              sh 'tox -e molecule-ansible8-debian12'
            }
          }
          post {
            always {
              cleanWs()
            }
          }
        }

        stage ('Debian 13 / Ansible 13') {
          agent {
            label 'molecule-aws-debian13-small'
          }
          steps {
            script { checkout scm }
            withCredentials([
                [$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS Jenkins community'],
            ]) {
              sh "aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 119948825560.dkr.ecr.eu-west-1.amazonaws.com"
              sh 'tox -e molecule-ansible13'
            }
          }
          post {
            always {
              cleanWs()
            }
          }
        }

      }
    }

  }
}
