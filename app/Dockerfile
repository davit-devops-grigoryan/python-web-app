FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
