def project = ' dev_deploy_tools'
def  appName = 'jenkins-tools'
def  feSvcName = "${appName}"
def  imageTag = "pdkhai/${appName}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

pipeline {
  agent none
  environment {
    DOCKER_HUB_CREDS = credentials('docker-hub-credentials')
  }  stages {
    stage('Build and push image with Container Builder') {
      steps {
        sh "docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PWD"
        sh "docker build -t ${imageTag} ."
        sh "docker push ${imageTag}"
      }
    }
    stage('Test') {
      steps {
        sh """
          docker run -it -e JENKINS_USER=$JENKINS_USER -e JENKINS_PASSWORD=$JENKINS_PASSWORD jenkins-tools find test_keyword > response
          cat response
        """
      }
    }
    stage('Deploy Production') {
      // Production branch
      when { branch 'master' }
      steps{
        sh "echo Deploy production"
      }
    }
    stage('Deploy Dev') {
      // Developer Branches
      when { 
        not { branch 'master' } 
      } 
      steps {
        sh "echo Deploy dev"
      }     
    }
  }
}
