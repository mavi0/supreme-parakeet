# Container for containernet testing

FROM ubuntu:trusty
MAINTAINER Eleanor Davies <ele@nordavi.es>

RUN apt-get update \
    && apt-get install -y iperf3 iputils-ping net-tools

CMD ["/bin/bash"]
