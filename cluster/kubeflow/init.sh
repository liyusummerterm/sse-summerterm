microk8s enable kubeflow
microk8s.kubectl expose deployment ambassador --type=NodePort --name=ambassador-nodeport-service --namespace=kubeflow
