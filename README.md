# k8s-grpc-helloworld

- [x] Run client to call server and get message, using `ClusterIP` to communicate within cluster.
- [x] Show Deployments, Pods, Services in Dashboard.

```
$ kubectl create -f helloworld.yaml
$ kubectl exec terminal-87 -- python3 app/greeter_client.py
Greeter client received: Hello, you!
Greeter client received: Hello again, you!
```
