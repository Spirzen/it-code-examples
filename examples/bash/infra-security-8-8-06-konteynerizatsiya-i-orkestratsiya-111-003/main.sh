# Контекст и конфигурация
kubectl config view
kubectl config view -o jsonpath='{.users[*].name}'
kubectl config get-contexts
kubectl config current-context
kubectl config use-context cluster-name
kubectl config set-credentials kubeuser/foo.kubernetes.com --username=kubeuser --password=kubepassword
kubectl config set-context --current --namespace=my-namespace
kubectl config unset users.foo

# Просмотр и поиск ресурсов
kubectl get pods,deployments,svc
kubectl get pods --all-namespaces
kubectl get pods -o wide
kubectl describe nodes my-node
kubectl events --types=Warning
kubectl diff -f ./my-manifest.yaml

# Обновление ресурсов
kubectl rollout history deployment/frontend
kubectl rollout undo deployment/frontend
kubectl rollout restart deployment/frontend
kubectl label pods my-pod new-label=awesome
kubectl annotate pods my-pod icon-url-
kubectl autoscale deployment foo --min=2 --max=10

# Создание ресурсов
kubectl apply -f ./manifest.yaml
kubectl create deployment nginx --image=nginx
kubectl explain pods

# Масштабирование
kubectl scale --replicas=3 rs/foo
kubectl scale --current-replicas=2 --replicas=3 deployment/mysql
kubectl scale --replicas=5 rc/foo rc/bar rc/baz

# Работа с запущенными Pod
kubectl logs my-pod
kubectl logs my-pod -c my-container
kubectl logs -f my-pod
kubectl run nginx --image=nginx -n mynamespace
kubectl attach my-pod -i
kubectl port-forward my-pod 5000:6000
kubectl exec --stdin --tty my-pod -- /bin/sh
kubectl debug my-pod -it --image=busybox:1.28
kubectl top pod POD_NAME --containers

# Deployment и Service
kubectl logs deploy/my-deployment
kubectl port-forward svc/my-service 5000
kubectl exec deploy/my-deployment -- ls
