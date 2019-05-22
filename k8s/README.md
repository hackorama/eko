# EKO k8s example

Using MiniKube

```
hackorama@hackorama k8s  (master %=) $ kubectl apply -f eko.yaml
namespace/eko unchanged
service/eko-service created
statefulset.apps/eko-server created
```

```
hackorama@hackorama k8s  (master %=) $ kubectl get pods -n eko; kubectl get svc -n eko
NAME           READY   STATUS    RESTARTS   AGE
eko-server-0   1/1     Running   0          7s
NAME          TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)                                   AGE
eko-service   NodePort   10.103.13.57   <none>        80:30080/TCP,443:30443/TCP,55:30055/TCP   25s
```

```
hackorama@hackorama k8s  (master %=) $ minikube ip
192.168.64.3
```

```
hackorama@hackorama k8s  (master %=) $ curl http://192.168.64.3:30080
CLIENT HOST      : 172.17.0.1:61704
REQUEST_TYPE PATH: GET /
SERVER VERSION   : SimpleHTTP/0.6
REQUEST VERSION  : HTTP/1.1
PROTOCOL VERSION : HTTP/1.0
HEADERS          : Host: 192.168.64.3:30080
User-Agent: curl/7.54.0
Accept: */*

EKO_SERVER_0.0.0.0_HTTP:80_HTTPS:443_TCP:55
```

```
hackorama@hackorama k8s  (master %=) $ curl -k http://192.168.64.3:30443
CLIENT HOST      : 172.17.0.1:61707
REQUEST_TYPE PATH: GET /
SERVER VERSION   : SimpleHTTP/0.6
REQUEST VERSION  : HTTP/1.1
PROTOCOL VERSION : HTTP/1.0
HEADERS          : Host: 192.168.64.3:30443
User-Agent: curl/7.54.0
Accept: */*

EKO_SERVER_0.0.0.0_HTTP:80_HTTPS:443_TCP:55
```

```
hackorama@hackorama k8s  (master %=) $ nc 192.168.64.3 30055
EKO_SERVER_0.0.0.0_HTTP:80_HTTPS:443_TCP:55
hello
hello
^C
```

```
hackorama@hackorama k8s  (master %=) $ kubectl logs eko-server-0  -n eko
Starting EKO_SERVER_0.0.0.0_HTTP:80_HTTPS:443_TCP:55 on 0.0.0.0
HTTP server on port 80
HTTPS server on port 443
TCP server on port 55
Connection from: 172.17.0.1:61722
172.17.0.1 61722: hello

172.17.0.1 61722:
```
