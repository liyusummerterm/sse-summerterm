pipeline {
  agent {
    kubernetes {
      containerTemplate {
        name 'node'
        image 'node:lts-alpine'
        ttyEnabled true
        command 'cat'
      }
    }
  }
  stages {
    stage('Environment') {
      steps {
        container('node'){
          sh "cd frontend && yarn install"
        }
      }
    }

    stage('Build') {
      steps {
        container('node'){
          sh "cd frontend && yarn build"
        }
      }
    }

    stage('Test') {
      steps {
        container('node'){
          sh "cd frontend && yarn lint"
        }
      }
    }

    stage('Deploy') {
      steps {
        sh '''#!/bin/bash
echo I\\\'m fine
sleep 5
ls'''
      }
    }
  
  }
}