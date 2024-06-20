FROM python:3.10.10

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# WORKDIR src

# CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:5000
# CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --preload --bind=0.0.0.0:5000
# CMD chmod u+x docker.app.sh
CMD chmod a+x docker/*.sh
