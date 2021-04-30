FROM ubuntu:latest

RUN apt-get update
RUN apt-get install --no-install-recommends --no-install-suggests -y gnupg2 ca-certificates wget vim git build-essential locales \
      && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \
      && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/pjreddie/darknet.git
# RUN sed -i s/GPU=0/GPU=1/ /darknet/Makefile
# RUN sed -i s/CUDNN=0/CUDNN=1/ /darknet/Makefile
RUN cd darknet \
      && make
RUN ln -s /darknet/libdarknet.so /usr/lib/libdarknet.so

# YOLOv3重み
RUN wget -O /darknet/yolov3.weights https://pjreddie.com/media/files/yolov3.weights
RUN wget -O /darknet/darknet53.conv.74 https://pjreddie.com/media/files/darknet53.conv.74

# YOLOv3-tiny重み
RUN wget -O /darknet/yolov3-tiny.weights https://pjreddie.com/media/files/yolov3-tiny.weights
RUN wget -O /darknet/yolov3-tiny.conv.11 https://drive.google.com/u/0/uc?id=18v36esoXCh-PsOKwyP2GWrpYDptDY8Zf&export=download
