FROM python:3.13-slim


RUN mkdir /Fastcut

WORKDIR /Fastcut


COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

RUN chmod a+x /Fastcut/docker/*.sh


CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]