FROM python:3.9-slim

WORKDIR /app

COPY cipher.py /app/

RUN mkdir ./out

RUN python3 cipher.py 'ctf{SuperCiph3rI$C00l!}'

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000"]
