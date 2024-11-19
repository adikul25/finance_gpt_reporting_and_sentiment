FROM python:3.13.0

RUN mkdir /Streamlit

RUN apt-get update -y

RUN pip install --upgrade pip

COPY requirements.txt /Streamlit

WORKDIR /Streamlit

RUN pip install --no-cache-dir -r requirements.txt

COPY . /Streamlit

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]