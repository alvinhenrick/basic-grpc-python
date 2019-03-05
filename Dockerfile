FROM python:3.6 as base

FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY . /basic-grpc-python

WORKDIR /basic-grpc-python

CMD ["python", "server.py"]