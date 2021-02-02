# homework
1 Create vpc using cloudformation for EKS.
  cloudFormation-vpc.json   

2 Create EKS at the Tokyo site using the eksctl command tool.
  eksctl create cluster --name inspiry-test --version 1.18 --region ap-northeast-1 --with-oidc --ssh-access --ssh-public-key <your-key> --managed --nodegroup-name nodegroup-test --node-type t3.medium --nodes 2 --nodes-min 1 --nodes-max=3 --node-ami auto

3 Create ingress controller.
  kubectl apply -f ingress-controller.yaml

4 Create workload demo and expose port 80 via NLB ingress.
  kubectl apply -f workload-demo.yaml

5 About Jenkins job
  When I created the SpringBoot project, I referenced Docker's plug-in in the pop.xml file and specified the underlying image. so I can complete the containerization of the APP by specifying docker:build parameter when compiling the project in mvn command.
  The jenkins-job-pipeline.txt file is part of the pipeline code for Jenkins Job.

6 About Dockerfile
  To complete the Dockerfile topic, a example of Python flask web-hook is placed in the docker directory, where the image can be generated directly using the build.sh script.

7 About create Jenkins in k8s
  Due to time constraints, I have included a Jenkins Workload Manifests from our company's development environment in the 17-CICD directory for your reference.
