FROM python:3

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y postgresql-client


COPY . /app/
COPY ./entrypoint /

RUN sed -i 's/\r$//g' /entrypoint

RUN chmod u+x /entrypoint

ENTRYPOINT ["/entrypoint"]