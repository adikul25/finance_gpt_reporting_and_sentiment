FROM python:3.13.0

RUN mkdir /FastAPI

COPY requirements.txt /FastAPI

WORKDIR /FastAPI

RUN apt-get update -y

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn

COPY ./app /FastAPI/app

EXPOSE 8000

WORKDIR /FastAPI/app

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]