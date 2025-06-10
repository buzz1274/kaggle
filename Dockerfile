FROM python:3.11-slim-bookworm AS base-image

ARG POETRY_ARGS

ENV POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTIONS=1 \
    WORKDIR_PATH="/opt/downloader"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    apt-utils \
    git

RUN pip install --no-cache-dir --upgrade pip poetry
COPY downloader/ .


WORKDIR $WORKDIR_PATH

RUN poetry lock
RUN poetry install ${POETRY_ARGS}

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["sleep infinity"]
