FROM python:3.9

RUN apt-get update && apt-get install -y cmake protobuf-compiler \
libprotobuf-dev python3-pip python3-dev

RUN mkdir /cl_grpc_visionx_server
WORKDIR /cl_grpc_visionx_server

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

COPY poetry.lock pyproject.toml /cl_grpc_visionx_server/
RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY ./app /cl_grpc_visionx_server/app
COPY ./protos /cl_grpc_visionx_server/protos
COPY .gitignore /cl_grpc_visionx_server/.gitignore

ENTRYPOINT [ "python", "main.py" ]