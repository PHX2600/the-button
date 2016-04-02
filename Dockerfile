FROM alpine:3.3
MAINTAINER Dan Petro <AltF4Warrior@Gmail.com> & Chris Kankiewicz <Chris@ChrisKankiewicz.com>

RUN mkdir -pv /opt/app

RUN apk add --update python py-tornado \
    && apk del --purge gcc git tar wget && rm -rf /var/cache/apk/*

COPY src/ /opt/app/

WORKDIR "/opt/app"

CMD ["python", "button.py"]
