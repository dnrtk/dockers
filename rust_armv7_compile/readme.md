# docker image作成
```shell
docker build -t rust_armv7_compile:latest .
```

# クロスコンパイル(Linux)
```shell
docker run -it -v "$PWD":/build rust_armv7_compile:latest
```

# クロスコンパイル(Windows)
```shell
docker run -it -v "%cd%\\":/build rust_armv7_compile:latest
docker run -it -v "%cd%\\":/build rust_armv7_compile:latest cargo run --target arm-unknown-linux-gnueabihf --release
```
