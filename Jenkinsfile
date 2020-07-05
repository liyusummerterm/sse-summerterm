pipeline {
  agent {
    kubernetes {
      containerTemplate {
        name 'python'
        image 'python:latest'
        ttyEnabled true
        command 'cat'
      }
    }
  }
  stages {
    stage('Environment') {
      steps {
        echo 'Hello World'
        container('python'){
          sh "pip3 install -r requirements.txt"
        }
      }
    }

    stage('Test') {
      steps {
        container('python'){
          sh "pip3 install pytest"
          sh "pytest --junitxml=build/reports.xml"
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
  post {
    always {
      junit 'build/reports.xml'
    }
  }
}