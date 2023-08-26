FROM python:3.9-alpine

LABEL maintainer="Rayron Victor"

ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

ARG WWWGROUP
ARG WWWUSER

WORKDIR /app

#ENV TZ=UTC
#
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apk update && \
    apk add --no-cache bash supervisor && \
    apk add gcc python3-dev musl-dev postgresql-dev jpeg-dev zlib-dev libffi-dev rust rustup && \
    apk add postgresql-libs py3-cffi libjpeg && \
    apk add postgresql-client

RUN addgroup --gid $WWWGROUP djando
RUN adduser -D -G djando -u $WWWUSER djando

COPY start-container /usr/local/bin/start-container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN chmod +x /usr/local/bin/start-container

EXPOSE 8000

ENTRYPOINT ["start-container"]
