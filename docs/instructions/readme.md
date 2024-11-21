# install kubeflow

Checking your versions:

Prerequisites
currento version is 1.9.0. It targets Kubernetes 1.29+
A default StorageClass
Kustomize 5.2.1+
Kubectl in a version that is compatible with your Kubernetes cluster

Example:

```
(base) fr69nr@APM3LH9FV5M66D0 kubeflow % kubectl version                                              
Client Version: v1.31.2
Kustomize Version: v5.4.2
Server Version: v1.30.6+rke2r1

```
Storage class:

```
(base) fr69nr@APM3LH9FV5M66D0 kubeflow % kubectl get storageclass                                     
NAME                         PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
k8s-test-lb-auth (default)   csi.lightbitslabs.com   Delete          Immediate           true                   103m
(base) fr69nr@APM3LH9FV5M66D0 kubeflow % kubectl get storageclass --all-namespaces                    
NAME                         PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
k8s-test-lb-auth (default)   csi.lightbitslabs.com   Delete          Immediate           true                   103m
```
Looking some GPUS:

```
kubectl get nodes --show-labels | grep gpu.count
```

Two approaches were checked:

1 - JUJU: https://charmhub.io/kubeflow

2 - Manually: Creating your own automation

Due to my willing on learn, deployment was manually performed.

Findings:

Poprt forward works great:

```
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80 --address=0.0.0.0
```

I had a problem with open files limit. It was missing a new limits config:

```
Linux kernel subsystem changes to support many pods
    sudo sysctl fs.inotify.max_user_instances=2280
    sudo sysctl fs.inotify.max_user_watches=1255360
```
