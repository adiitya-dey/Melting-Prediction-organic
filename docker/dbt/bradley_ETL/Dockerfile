# temp stage
FROM python:3.11-slim as builder
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
# RUN pip install -r requirements.txt


#final stage
FROM python:3.11-slim
WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY  --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY main.py .
COPY bradley_clean_data ./bradley_clean_data
COPY profiles.yml .


CMD ["gunicorn","-b", "0.0.0.0:8080", "app:main"]
# CMD ["python", "app.py"]
EXPOSE 8080