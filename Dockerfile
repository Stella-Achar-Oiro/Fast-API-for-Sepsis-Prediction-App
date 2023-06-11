FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8091

CMD ["uvicorn", "API_app:app", "--host", "0.0.0.0", "--port", "8091", "--reload"]
