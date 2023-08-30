FROM python

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

RUN sed -i 's/\r$//g' ./entrypoint

RUN chmod u+x /app/entrypoint

ENTRYPOINT ["/app/entrypoint"]