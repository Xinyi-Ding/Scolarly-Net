FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y ruby-full && gem install anystyle-cli
COPY ./app /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
