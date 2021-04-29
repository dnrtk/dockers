FROM ubuntu:latest

RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y gnupg2 ca-certificates \
            wget git build-essential \
      && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/pjreddie/darknet.git \
        && cd darknet \
        && make

RUN wget -O /darknet/yolov3.weights https://pjreddie.com/media/files/yolov3.weights
RUN wget -O /darknet/yolov3-tiny.weights https://pjreddie.com/media/files/yolov3-tiny.weights
