Anchors are particularly useful in **Kubernetes YAML**.
``` YAML
common_labels: &labels
  app: my-app
  tier: backend

apiVersion: v1
kind: Pod
metadata:
  name: my-app-pod
  labels: *labels
spec:
  containers:
    - name: my-app
      image: my-app:latest
```

