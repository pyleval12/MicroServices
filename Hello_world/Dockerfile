FROM python:3.12.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY hw.py .

ENV FLASK_APP=hw.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
# flask run --host=0.0.0.0
# --port=5000
# docker build -t hw:1.0 .
# docker run -d -p 5000:5000 hw:1.0