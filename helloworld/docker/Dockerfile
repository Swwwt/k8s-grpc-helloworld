FROM ubuntu:bionic
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install grpcio -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install protobuf -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install grpcio-tools -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD app /app/