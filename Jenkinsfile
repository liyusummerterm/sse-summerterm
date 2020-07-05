pipeline {
  agent any
  stages {
    stage('Environment') {
      steps {
        echo 'Hello World'
        sh '''#!/bin/bash
apt update
apt install python3-pip
pip3 install -r requirements.txt'''
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