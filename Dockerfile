FROM alpine:3.3
MAINTAINER Dan Petro <AltF4Warrior@Gmail.com> & Chris Kankiewicz <Chris@ChrisKankiewicz.com>

RUN mkdir -pv /opt/app

COPY ./ /opt/app/

RUN apk add --update gcc libffi-dev musl-dev python-dev py-pip py-tornado sqlite \
    && pip install -r /opt/app/requirements.txt \
    && apk del --purge gcc && rm -rf /var/cache/apk/*

RUN cd /opt/app/ && sqlite3 database.db < schema.sql

CMD ["python", "/opt/app/src/button.py"]
