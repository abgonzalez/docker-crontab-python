
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y vim-tiny && \
    apt-get install -y dos2unix &&\
    apt install -y python3.8
 
ENV PYTHONPATH=/usr/bin/python3.8
ENV PATH = "$PATH:/usr/bin/python3.8" 
RUN ln -s /usr/bin/python3.8  /usr/bin/python   
RUN cd /usr && mkdir deliveroo
COPY ./src /usr/deliveroo
COPY ./tst /usr/deliveroo
WORKDIR /usr/deliveroo
RUN dos2unix *
#CMD ["/bin/sh", "./run_test.sh"]
#CMD [“sleep”, “infinity”]