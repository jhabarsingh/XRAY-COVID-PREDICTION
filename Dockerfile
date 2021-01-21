FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m pip install --upgrade pipa
RUN pip install -r requirements.txt
COPY . /code/
