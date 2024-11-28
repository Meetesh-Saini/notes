FROM python:3.9-slim

ENV FLASK_KEY="your_secret_key_here"

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN apt-get update && apt-get install -y gnupg curl 
RUN curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor && echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/8.0 main" | tee /etc/apt/sources.list.d/mongodb-org-8.0.list \ 
   && apt-get update && apt-get install -y mongodb-org

RUN mkdir -p /data/db && chown -R mongodb:mongodb /data/db

EXPOSE 5000

# RUN python /app/init_db.py

# CMD ["sh", "-c", "service mongodb start && python app.py"]
CMD ["sh", "-c", "mongod --dbpath /data/db --bind_ip 0.0.0.0 --logpath /var/log/mongodb.log & python /app/init_db.py && python app.py"]
