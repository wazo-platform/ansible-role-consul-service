pipeline {

  agent {
    label 'molecule-aws && small'
  }

  stages {

    stage ('Test') {
      steps {
        checkout scm
        sshagent(credentials: ['ssh-github-wazo-bot']) {
          sh 'tox'
        }
      }
    }

  }

}
