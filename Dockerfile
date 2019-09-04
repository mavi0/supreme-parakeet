# Container for containernet testing

FROM ubuntu:xenial
MAINTAINER Eleanor Davies <ele@nordavi.es>

RUN apt-get update \
    && apt-get install -y iperf3 iputils-ping\
    && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
