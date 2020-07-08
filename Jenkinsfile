pipeline {
  agent {
    kubernetes {
      yaml """
spec:
  containers:
  - name: node
    image: node:lts-alpine
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
        container('node'){
          retry(3) {
            sh "cd frontend && yarn install --color=always"
          }
        }
      }
    }

    stage('Build') {
      steps {
        container('node'){
          sh "cd frontend && yarn build --color=always"
        }
      }
    }

    stage('Test') {
      steps {
        container('node'){
          sh "cd frontend && yarn lint --color=always"
        }
      }
    }

    stage('Build Container Image') {
      steps {
        container('kaniko'){
          retry(3) {
            sh "/kaniko/executor --dockerfile `pwd`/Dockerfile --context `pwd` --destination=registry.container-registry:5000/chestnut/frontend-vue --insecure"
          }
        }
      }
    }

    stage('Deploy') {
      steps {
        sh "sleep 10"
      }
    }
  
  }
}