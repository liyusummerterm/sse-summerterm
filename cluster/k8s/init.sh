#!/bin/bash

snap install microk8s --classic

microk8s.enable dashboard dns ingress istio registry storage helm

token=$(microk8s kubectl -n kube-system get secret | grep default-token | cut -d " " -f1)
microk8s kubectl -n kube-system describe secret $token

microk8s.add-node