FROM python:3.5.2

ADD ./requirements.txt /
RUN pip install -r requirements.txt

ADD ./compose/django/start.sh /
RUN sed -i 's/\r//' start.sh
RUN chmod +x start.sh

ADD ./advertisement-server /app
WORKDIR /app