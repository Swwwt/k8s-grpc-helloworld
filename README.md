# k8s-grpc-helloworld

- [x] Run gRPC client and server in Python
- [x] Build docker image *swwwt/k8s-grpc*
- [x] Deploy service in k8s (using `ClusterIP` to communicate within cluster)
- [x] Show Deployments, Pods, Services in k8s Dashboard

```
$ kubectl create -f helloworld.yaml
$ kubectl exec terminal-87 -- python3 app/greeter_client.py
Greeter client received: Hello, you!
Greeter client received: Hello again, you!
```
