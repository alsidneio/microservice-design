FROM python:3.14.0rc1-slim-bullseye

RUN apt-get update \
&& apt-get install -y --no-install-recommends --no-install-suggests \
build-essential default-libmysqlclient-dev pkg-config libffi-dev \
&& pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 5000
CMD [ "python3", "server.py"]
