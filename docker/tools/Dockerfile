FROM alpine

RUN apk add --no-cache \
  bash \
  bind-tools \
  ethtool \
  iproute2 \
  net-tools \
  netcat-openbsd \
  openssh \
  tcpdump \
  && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
  && ssh-keygen -t rsa     -f /etc/ssh/ssh_host_rsa_key     -q -P ""  \
  && ssh-keygen -t ecdsa   -f /etc/ssh/ssh_host_ecdsa_key   -q -P ""  \
  && ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -q -P ""  \
  && echo "root:root" | chpasswd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
