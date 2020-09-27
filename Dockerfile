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

RUN chown -R www-data:www-data /dailymed-api
RUN chmod -R 750 /dailymed-api

USER www-data
