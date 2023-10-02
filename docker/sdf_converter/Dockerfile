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
# RUN wget -O ./openbabel-2.3.1.tar.gz https://sourceforge.net/projects/openbabel/files/openbabel/2.3.1/openbabel-2.3.1.tar.gz/download
RUN ls -lrt && tar zxf openbabel-2.3.1.tar.gz
# RUN mkdir build && cd build && cmake ../openbabel-2.3.1 && make && make install



COPY main.py .

CMD ["gunicorn","-b", "0.0.0.0:8080", "main:app"]

EXPOSE 8080