FROM eko-server:latest

RUN apk add --no-cache \
  tcpdump \
  iproute2 \
  net-tools \
  ethtool \
  netcat-openbsd \
  bind-tools \
  openssh \
  && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
  && echo "root:root" | chpasswd

EXPOSE 22
