FROM python:3.9-slim

WORKDIR /app

COPY REPORT.pdf /app/

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000"]
