FROM python:latest

RUN pip3 install --upgrade pip

RUN apt-get update \
&& apt-get install -y libsodium-dev \
libsecp256k1-dev \
libgmp-dev \
pkg-config

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]