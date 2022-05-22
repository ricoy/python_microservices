FROM python:3.10-alpine

WORKDIR /app

RUN pip install pipenv

ADD hello_world_service.ini .
ADD hello_world_service.py .
ADD Pipfile .
ADD Pipfile.lock .
ADD .env .
ADD start.sh .

COPY app ./app

RUN apk update && \
    apk add --no-cache python3-dev build-base linux-headers pcre-dev bash && \
    pip3 install pipenv && \
    pipenv lock -r > requirements.txt && \
    pip3 uninstall --yes pipenv && \
    pip3 install -r requirements.txt && \
    apk del python3-dev

EXPOSE 5000

CMD [ "./start.sh"]


