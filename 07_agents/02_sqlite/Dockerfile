FROM python:3.12-slim

# Grab the uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY requirements.txt .

# Install into the system Python (no venv needed inside a container)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system -r requirements.txt

RUN mkdir -p db_data

COPY vulnerable_sqlite_mcp_server.py .

COPY ./db_data/metactf_users.db ./db_data/metactf_users.db

EXPOSE 8080

CMD ["python", "vulnerable_sqlite_mcp_server.py", "http"]
