FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p db_data

COPY vulnerable_sqlite_mcp_server.py .

COPY ./db_data/metactf_users.db ./db_data/metactf_users.db

EXPOSE 8080

CMD ["python", "vulnerable_sqlite_mcp_server.py", "http"]
