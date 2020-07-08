pipeline {
  agent {
    kubernetes {
      yaml """
spec:
  containers:
  - name: python
    image: python:latest
    command:
    - cat
    tty: true
  - name: helm
    image: alpine/helm:2.16.9
    command:
    - cat
    tty: true
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    command:
    - /busybox/cat
    tty: true
"""
    }
  }
  stages {
    stage('Environment') {
      steps {
        echo 'Hello World'
        container('python'){
          retry(3) {
            sh "pip3 install -r requirements.txt"
          }
        }
      }
    }

    stage('Test') {
      steps {
        container('python'){
          retry(3) {
            sh "pip3 install pytest"
          }
          sh "pytest --color=yes --junitxml=build/reports.xml"
        }
      }
    }

    stage('Build Container Image') {
      steps {
        container('kaniko'){
          retry(3) {
            sh "/kaniko/executor --dockerfile `pwd`/Dockerfile --context `pwd` --destination=registry.container-registry:5000/chestnut/backend --insecure"
          }
        }
      }
    }

    stage('Deploy For Test') {
      steps {
        container('helm'){
          sh "helm upgrade --install backend-test --wait --cleanup-on-fail ./backend-chart"
        }
      }
    }
  
    stage('Deploy For Production') {
      steps {
        container('helm'){
          sh "helm upgrade --install backend --wait --cleanup-on-fail ./backend-chart"
        }
      }
    }
  
  }
  post {
    always {
      junit 'build/reports.xml'
    }
  }
}