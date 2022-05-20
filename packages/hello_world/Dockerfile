ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

COPY packages.hello_world/main.pex packages/hello_world/main.pex

CMD ./packages/hello_world/main.pex packages.hello_world.main:app
