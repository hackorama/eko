FROM python:2.7-alpine

COPY eko.py .
COPY gencert.sh .

RUN apk add --no-cache openssl \
    && sh gencert.sh

ENV HOST=0.0.0.0 \
    HTTP_PORT=8080 \
    HTTPS_PORT=8443 \
    TCP_PORT=5000 \
    VERBOSE=0 \
    NAME=""

EXPOSE $HTTP_PORT $HTTPS_PORT $TCP_PORT

ENTRYPOINT ["sh", "-c", "python -u eko.py $HOST $HTTP_PORT $HTTPS_PORT $TCP_PORT $VERBOSE $NAME"]
CMD []
