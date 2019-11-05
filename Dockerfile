FROM dockerproxy.bale.ai/python:3.7-slim

WORKDIR /vip_admin
RUN pip install --upgrade pip && \
	echo $TZ > /etc/timezone \
	cp /usr/share/zoneinfo/Asia/Tehran /etc/localtime

COPY ./requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY ./ ./
RUN pip3 install -e .
CMD template start
