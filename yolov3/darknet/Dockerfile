FROM ubuntu:latest

RUN apt-get update
RUN apt-get install --no-install-recommends --no-install-suggests -y gnupg2 ca-certificates wget git build-essential \
      && rm -rf /var/lib/apt/lists/*
RUN apt-get -y install locales \
      && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN git clone https://github.com/pjreddie/darknet.git \
      && cd darknet \
      && make
RUN ln -s /darknet/libdarknet.so /usr/lib/libdarknet.so

RUN wget -O /darknet/yolov3.weights https://pjreddie.com/media/files/yolov3.weights
RUN wget -O /darknet/yolov3-tiny.weights https://pjreddie.com/media/files/yolov3-tiny.weights
