FROM python:3.10-slim
WORKDIR /app
COPY ./app /app/app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
# uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload