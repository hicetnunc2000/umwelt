FROM ubuntu:18.04
#FROM golang:1.14.4-buster 
#LABEL maintainer="Steven Allen <steven@stebalien.com>"

# Install deps
RUN apt-get update && apt-get install -y \
    libssl-dev \
    ca-certificates \
    fuse \
    wget \
    git \
    make \
    gcc

RUN wget https://golang.org/dl/go1.14.4.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf go1.14.4.linux-amd64.tar.gz

    #&& echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile
ENV PATH "$PATH:/usr/local/go/bin"
#RUN git clone https://go.googlesource.com/go goroot \
#    && cd goroot \
#    && git checkout go1.14.6 \
#    && cd src \
#    && ./all.bash \
#    && cd ..

#RUN export PATH=$PATH:/usr/local/go/bin
CMD source ~/.profile

RUN git clone https://github.com/ipfs/go-ipfs.git \
    && cd go-ipfs \
    && make install

# Swarm TCP; should be exposed to the public
EXPOSE 4001
# Swarm UDP; should be exposed to the public
EXPOSE 4001/udp
# Daemon API; must not be exposed publicly but to client services under you control
EXPOSE 5001
# Web Gateway; can be exposed publicly with a proxy, e.g. as https://ipfs.example.org
EXPOSE 8080
# Swarm Websockets; must be exposed publicly when the node is listening using the websocket transport (/ipX/.../tcp/8081/ws).
EXPOSE 8081

ENTRYPOINT ipfs
# Execute the daemon subcommand by default
CMD ["daemon", "--enable-pubsub-experiment"]