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
        container('node'){
          sh "apk update && apk add git"
          sh "sed -i '/resolved \"https/d' frontend/yarn.lock || exit 0"
          retry(3) {
            sh "cd frontend && yarn config set registry http://npm-verdaccio.npm-registry:4873/ && yarn install --color=always"
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
          sh "cd frontend && yarn test:ci --color=always"
        }
      }
    }

    stage('Build Container Image') {
      steps {
        container('buildkit'){
          retry(3) {
            sh "buildctl --addr tcp://buildkitd:1234 build --frontend=dockerfile.v0 --local context=`pwd` --local dockerfile=`pwd` --output type=image,name=registry.container-registry:5000/chestnut/frontend-vue,push=true,registry.insecure=true"
          }
        }
      }
    }

    stage('Deploy For Test') {
      steps {
        container('helm'){
          sh "set +e; helm delete frontend-vue-test --purge ; exit 0"
          sh "helm upgrade --install frontend-vue-test --wait --cleanup-on-fail ./frontend-chart"
        }
      }
    }
  
    stage('Test Test'){
      failFast true
      parallel {
        stage('Get /'){
          steps{
            httpRequest responseHandle: 'NONE', url: 'http://frontend-vue-test-frontend-chart/', wrapAsMultipart: false
          }
        }
        stage('Get /_just_test'){
          steps{
            httpRequest responseHandle: 'NONE', url: 'http://frontend-vue-test-frontend-chart/_just_test', wrapAsMultipart: false
          }
        }
      }
    }
  
    stage('Clean up Test') {
      steps {
        container('helm') {
          sh "helm delete frontend-vue-test --purge ; exit 0"
        }
      }
    }


    stage('Deploy For Production') {
      steps {
        container('helm'){
          sh "helm upgrade --install frontend-vue --wait --cleanup-on-fail ./frontend-chart"
        }
      }
    }
    
  }
}