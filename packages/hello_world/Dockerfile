ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

COPY packages.hello_world/manylinux.pex main.pex

CMD ./main.pex hello_world.main:app --port 8000

