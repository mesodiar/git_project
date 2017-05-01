FROM python:3
ENV APPLICATION_ROOT /code/

RUN mkdir $APPLICATION_ROOT
ADD . $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT

ADD requirements.txt $APPLICATION_ROOT
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
