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
            sh 'tox -e molecule-ansible8'
            sh 'tox -e molecule-ansible8-debian12'
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
            sh 'tox -e molecule-ansible13'
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
