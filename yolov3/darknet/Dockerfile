FROM ubuntu:latest

RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y gnupg2 ca-certificates \
            git build-essential \
      && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/pjreddie/darknet.git
RUN git clone https://github.com/pjreddie/darknet.git \
        && cd darknet \
        && make
