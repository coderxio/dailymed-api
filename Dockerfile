FROM python:3.8.2

RUN pip install poetry

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /dailymed-api

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . ./

ENV PYTHONPATH=/dailymed-api/api

RUN poetry install

ARG user1=www-data

RUN chown -R ${user1}:${user1} /dailymed-api
RUN chmod -R 750 /dailymed-api

USER ${user1}
