def project = ' dev_deploy_tools'
def  appName = 'jenkins-tools'
def  feSvcName = "${appName}-frontend"
def  imageTag = "pdkhai/${appName}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

pipeline {
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
          sudo docker run -it -e JENKINS_USER=admin -e JENKINS_PASSWORD=74ad002863b64d54aec63cb95e690490 jenkins-tools find test_keyword
          cd /go/src/sample-app
          go test
        """
      }
    }
    stage('Deploy Production') {
      // Production branch
      when { branch 'master' }
      steps{
      }
    }
    stage('Deploy Dev') {
      // Developer Branches
      when { 
        not { branch 'master' } 
      } 
      steps {
      }     
    }
  }
}
