FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    kubernetes \
    prometheus-client

EXPOSE 8000
EXPOSE 9100

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8000"]