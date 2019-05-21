# EKO

Echo server Docker images for testing TCP, HTTP, HTTPS

## Server

```
$ sudo docker run -p8080:8080 -p8443:8443 -p5000:5000 hackorama/eko-server
Starting EKO_SERVER_0.0.0.0_HTTP:8080_HTTPS:8443_TCP:5000 on 0.0.0.0
HTTP server on port 8080
HTTPS server on port 8443
TCP server on port 5000
```

```
$ curl -k https://localhost:8443
EKO_SERVER_0.0.0.0_HTTP:8080_HTTPS:8443_TCP:5000
```

```
$ curl -k https://localhost:8443
EKO_SERVER_0.0.0.0_HTTP:8080_HTTPS:8443_TCP:5000
```

```
$ nc localhost 5000
EKO_SERVER_0.0.0.0_HTTP:8080_HTTPS:8443_TCP:5000
hello
hello
```


## Testing clients and tools

```
$ sudo docker run -d -p 2222:22 hackorama/eko-tools
```

```
$ ssh -p 2222 root@localhost
root@localhost's password: root
EKO TEST SSH SERVER
nc, dig, netstat, curl, wget, ssh, tcpdump, traceroute, iproute, ethtool
db8296712e5c:~#
```
