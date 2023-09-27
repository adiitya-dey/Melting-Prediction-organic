FROM python:3.11-slim
WORKDIR /app


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080

COPY app.py .
COPY scripts.sh .

CMD ["gunicorn","-b", "0.0.0.0:8080", "app:app"]
# CMD ["python", "app.py"]