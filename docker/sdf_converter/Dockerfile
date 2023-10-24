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

RUN apt-get update -y && apt-get install openbabel -y

COPY apps ./apps

CMD ["uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "8080"]

EXPOSE 8080