FROM python:3.11

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libjpeg-dev && \
    apt-get clean

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8064

CMD ["uvicorn", "api:app", "--host", "0.0.0.0","--port", "8064"]