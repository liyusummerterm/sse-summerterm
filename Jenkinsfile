pipeline {
  agent any
  stages {
    stage('Environment') {
      steps {
        echo 'Hello World'
        sh '''touch TestFile
sleep 30'''
      }
    }

    stage('Test') {
      steps {
        echo 'Test'
        sh '''sleep 30
ls
ip addr'''
      }
    }

    stage('Deploy') {
      steps {
        sh '''sleep 30
ls
ip addr'''
      }
    }

  }
}