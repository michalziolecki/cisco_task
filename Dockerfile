FROM python:3.10

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock /
COPY pyproject.toml /
RUN poetry install --no-root
WORKDIR /app/
COPY . /app/
RUN poetry install

EXPOSE 8000
HEALTHCHECK --timeout=10s --retries=2 --interval=30s CMD curl --fail http://localhost:8000/_/health  || exit 1
CMD ["/bin/bash", "-c", "/app/deploy/run.sh"]
