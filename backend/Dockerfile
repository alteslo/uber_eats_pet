FROM python:3.10.6-slim

WORKDIR /backend

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN mkdir /var/lib/postgresql
RUN mkdir /var/lib/postgresql/data
RUN chmod -R 777 /var/lib/postgresql/data


EXPOSE 8080
EXPOSE 5432

COPY . /backend