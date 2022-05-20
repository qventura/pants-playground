ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim

RUN apt-get -y update
RUN apt-get install -y python3-distutils
RUN apt-get install -y python3-apt

WORKDIR /app

COPY packages.hello_world/main.pex packages/hello_world/main.pex

CMD ./packages/hello_world/main.pex packages.hello_world.main:app
