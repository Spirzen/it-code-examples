kubectl get pods,deployments,svc
kubectl describe pod my-pod
kubectl apply -f deploy.yaml
kubectl delete -f deploy.yaml
kubectl logs my-pod
kubectl exec -it my-pod -- sh
kubectl port-forward svc/app 8080:80
kubectl rollout status deployment/my-app
kubectl scale deployment/my-app --replicas=3
kubectl config view
kubectl config use-context prod
kubectl top pod
kubectl explain pod.spec
kubectl diff -f deploy.yaml
