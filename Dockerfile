FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY products.py /app

CMD ["python3", "products.py"]

