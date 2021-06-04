# kubernetes-config-files
 
 ## Starting minikube
 ```
 minikube start
 ```
 
 ## Creating secret and config map
 ```
 kubectl apply -f config.yaml
 kubectl apply -f mongo-deployment.yaml
 ```
 
 ## Creating mongo deployment and service
 ```
 kubectl apply -f mongo-deployment.yaml
 ```
 
 ## Creating mongo-express deployment and service
 ```
 kubectl apply -f mongo-express-deployment.yaml
 ```
 
 ## Creating external IP for mong-express service
 ```
 minikube service mongo-express-service
 ```
