FROM python:3 AS python
COPY tftool /usr/local/lib/python3.10/site-packages/tftool
USER nobody
ENTRYPOINT ["python3", "-m", "tftool"]

FROM python AS latest

FROM alpine:3.15 AS alpine
RUN apk add --no-cache \
        python3
COPY tftool /usr/lib/python3.9/site-packages/tftool/
USER nobody
ENTRYPOINT ["python3", "-m", "tftool"]

FROM debian:bullseye AS debian
RUN apt-get -q -o=Dpkg::Use-Pty=0 update \
    && DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes \
       apt-get -q -o=Dpkg::Use-Pty=0 install --no-install-recommends --yes \
        python3 \
    && rm -rf /var/lib/apt/lists
COPY tftool /usr/local/lib/python3.9/dist-packages/tftool/
USER nobody
ENTRYPOINT ["python3", "-m", "tftool"]

FROM barnabyshearer/dockerfromscratch:10.1-python AS dockerfromscratch
COPY tftool /usr/lib/python3.8/site-packages/tftool
USER nobody
ENTRYPOINT ["python3", "-m", "tftool"]

FROM python:3.10-alpine AS python-alpine
COPY tftool /usr/local/lib/python3.10/site-packages/tftool
USER nobody
ENTRYPOINT ["python3", "-m", "tftool"]

FROM python:3.10-slim AS python-slim
COPY tftool /usr/local/lib/python3.10/site-packages/tftool
USER nobody
ENTRYPOINT ["python3", "-m", "tftool"]
