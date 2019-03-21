def project = ' dev_deploy_tools'
def  appName = 'jenkins-tools'
def  feSvcName = "${appName}"
def  imageTag = "pdkhai/${appName}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

pipeline {
  agent any
  environment {
      JENKINS_CREDS = credentials('jenkins-creds')
  }
  stages {
    stage('Build and push image with Container Builder') {
      // agent {
      //     docker { image 'docker:stable-git' }
      // }
      steps {
        sh "docker build -t ${imageTag} ."
        sh "docker push ${imageTag}"
      }
    }
    stage('Test') {
      // agent {
      //     docker { image 'docker:stable-git' }
      // }
      steps {
        sh "docker run -e JENKINS_USER=$JENKINS_CREDS_USR -e JENKINS_PASSWORD=$JENKINS_CREDS_PSW ${imageTag} find test_keyword"
      }
    }
    stage('Deploy Production') {
      // Production branch
      when { branch 'master' }
      steps{
        sh """echo Deploy production
        kubectl apply -f secret.yml
        kubectl apply -f service/development.yml
        kubectl apply -f development/development.yml
        """
      }
    }
    stage('Deploy Dev') {
      // Developer Branches
      when {
        not { branch 'master' }
      }
      steps {
        sh """echo Deploy dev
        kubectl apply -f secret.yml
        kubectl apply -f service/production.yml
        kubectl apply -f production/production.yml
        """
      }
    }
  }
}
