FROM python:3
COPY tftool /usr/local/lib/python3.10/site-packages/tftool
USER nobody
ENTRYPOINT ["python3", "-m", "tftool"]
