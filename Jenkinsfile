def project = ' dev_deploy_tools'
def  appName = 'jenkins-tools'
def  feSvcName = "${appName}"
def  imageTag = "pdkhai/${appName}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

pipeline {
  agent any
  stages {
    stage('Build and push image with Container Builder') {
      steps {
        sh "sudo docker build -t ${imageTag} ."
        sh "sudo docker push ${imageTag}"
      }
    }
    stage('Test') {
      steps {
        sh """
          sudo docker run -it -e JENKINS_USER=$JENKINS_USER -e JENKINS_PASSWORD=$JENKINS_PASSWORD jenkins-tools find test_keyword > response
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
