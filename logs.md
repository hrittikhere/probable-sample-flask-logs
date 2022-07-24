sudo docker build -t hrittik/sample-flask .

```logs

(env) hrittik@hrittik:~/probable-sample-flask-logs$ sudo docker build -t probable-sample-flask-logs:latest .
Sending build context to Docker daemon  93.18kB
Step 1/6 : FROM python:3.8-alpine
 ---> 2c5051ee52e6
Step 2/6 : COPY app/ /app
 ---> Using cache
 ---> 0e093540a1f3
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> 96fbbeb13d98
Step 4/6 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> 4e9b3391cc06
Step 5/6 : EXPOSE 9000
 ---> Using cache
 ---> 0db44ce50678
Step 6/6 : CMD ["python", "main.py", "--host=0.0.0.0"]
 ---> Using cache
 ---> 3a80cf19e9c3
Successfully built 3a80cf19e9c3
Successfully tagged probable-sample-flask-logs:latest

```


```bash
(env) hrittik@hrittik:~/probable-sample-flask-logs$ sudo docker image ls
REPOSITORY                   TAG          IMAGE ID       CREATED          SIZE
probable-sample-flask-logs   latest       3a80cf19e9c3   45 seconds ago   58.2MB
python                       3.8-alpine   2c5051ee52e6   5 days ago       46.8MB

```

```
sudo docker run -d -p 9000:9000 probable-sample-flask-logs:latest
```


```
hrittik@hrittik:~$ minikube start
😄  minikube v1.26.0 on Ubuntu 20.04
✨  Using the virtualbox driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🔄  Restarting existing virtualbox VM for "minikube" ...
🐳  Preparing Kubernetes v1.24.1 on Docker 20.10.16 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```


```
hrittik@hrittik:~$ minikube image ls
k8s.gcr.io/pause:3.7
k8s.gcr.io/pause:3.6
k8s.gcr.io/kube-scheduler:v1.24.1
k8s.gcr.io/kube-proxy:v1.24.1
k8s.gcr.io/kube-controller-manager:v1.24.1
k8s.gcr.io/kube-apiserver:v1.24.1
k8s.gcr.io/etcd:3.5.3-0
k8s.gcr.io/coredns/coredns:v1.8.6
gcr.io/k8s-minikube/storage-provisioner:v5
docker.io/library/probable-sample-flask-logs:latest
```