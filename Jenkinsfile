pipeline {
  agent any
  stages {
    stage('Environment') {
      steps {
        echo 'Hello World'
        sh '''#!/bin/bash
echo I\\\'m fine
touch TestFile
sleep 30'''
      }
    }

    stage('Test') {
      steps {
        echo 'Test'
        sh '''#!/bin/bash
echo I\\\'m fine
sleep 30
ls
ip addr'''
      }
    }

    stage('Deploy') {
      steps {
        sh '''#!/bin/bash
echo I\\\'m fine
sleep 30
ls
ip addr'''
      }
    }

  }
}