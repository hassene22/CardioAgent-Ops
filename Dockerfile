FROM python:3.12-slim

WORKDIR /app
COPY app.py .
COPY static ./static

ENV PORT=8050
EXPOSE 8050

CMD ["python", "app.py"]
