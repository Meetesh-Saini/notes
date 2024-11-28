FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000
EXPOSE 8000

CMD ["sh", "-c", "python app.py & python -m http.server 8000 --directory ./to_give"]
