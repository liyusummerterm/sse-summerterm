pipeline {
  agent {
    kubernetes {
      yaml """
spec:
  containers:
  - name: python
    image: python:alpine
    command:
    - cat
    tty: true
  - name: helm
    image: alpine/helm:2.16.9
    command:
    - cat
    tty: true
  - name: buildkit
    image: moby/buildkit:v0.6.2-rootless
    command:
    - cat
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
        container('buildkit'){
          retry(3) {
            //sh "/kaniko/executor --dockerfile `pwd`/Dockerfile --context `pwd` --destination=registry.container-registry:5000/chestnut/backend --insecure"
            sh "buildctl --addr tcp://buildkitd:1234 build --frontend=dockerfile.v0 --local context=`pwd` --local dockerfile=`pwd` --output type=image,name=registry.container-registry:5000/chestnut/backend,push=true,registry.insecure=true"
          }
        }
      }
    }

    stage('Deploy For Test') {
      steps {
        container('helm'){
          sh "helm status backend-test | grep \"STATUS: DEPLOYED\" || helm delete backend-test --purge"
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