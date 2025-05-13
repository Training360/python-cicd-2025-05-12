FROM python:3.13.3
WORKDIR /app
COPY pyproject.toml .
RUN pip install --editable .
COPY src src
CMD ["flask", "--app", "src/employees", "run", "--host", "0.0.0.0"]