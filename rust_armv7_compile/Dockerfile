FROM rust:latest

WORKDIR /build

RUN dpkg --add-architecture armhf && \
  apt-get update
RUN \
  rustup target add arm-unknown-linux-gnueabihf

RUN apt-get install -y gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf cmake
RUN apt-get install -y libfreetype6-dev:armhf libfontconfig1-dev:armhf

ENV CC=arm-linux-gnueabihf-gcc
ENV CXX=arm-linux-gnueabihf-g++
ENV AR=arm-linux-gnueabihf-ar
ENV TARGET=arm-linux-gnueabihf-

ENV CARGO_TARGET_ARM_UNKNOWN_LINUX_GNUEABIHF_LINKER=arm-linux-gnueabihf-gcc
ENV PKG_CONFIG_ALLOW_CROSS=1
ENV PKG_CONFIG_LIBDIR=/usr/lib/arm-linux-gnueabihf/pkgconfig

CMD ["cargo", "build", "--target", "arm-unknown-linux-gnueabihf", "--release"]
