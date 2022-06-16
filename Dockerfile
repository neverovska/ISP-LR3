# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/bakery

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add zlib-dev jpeg-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements .
RUN pip install -r requirements

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/bakery/entrypoint.sh"]