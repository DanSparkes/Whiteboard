FROM alpine:3.11

ARG react_app_build_env=local

RUN apk add --no-cache --update \
    libffi-dev nodejs nodejs-npm \
    && npm install webpack -gunicorn

COPY frontend/package.json /deploy/code/frontend/package.json
WORKDIR /deploy/code/frontend
RUN npm install && npm rebuild sass
COPY frontend /deploy/code/frontend
RUN npm run build

# Pull base image
FROM alpine:3.11

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Set work directory
WORKDIR /deploy/code

COPY requirements.txt /deploy/code/

# Install dependencies
RUN apk add --no-cache --update \
    python3 build-base python3-dev \
    nginx supervisor openssl ca-certificates \
    uwsgi-python3 libjpeg-turbo-dev zlib-dev \
    && python3 -m ensurepip \
    && rm -rf /usr/lib/python*/ensurepip \
    && rm -rf /root/.cache \
    && pip3 install --upgrade pip \
    && pip3 install -r /deploy/code/requirements.txt \
    && rm -rf /var/cache/apk/* \
    && apk del build-base python3-dev

COPY conf/etc /etc/

ARG PORT

RUN mkdir -p /etc/nginx/sites-enabled \
    && mkdir -p /run/nginx \
    && ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf \
    && rm -rf /var/log/nginx/*

RUN cat /etc/nginx/sites-available/app.conf
RUN touch /var/log/messages
RUN mkdir -p /var/log/supervisor/conf.d

COPY whiteboard/scripts/configure.sh /deploy/code/scripts/configure.sh
RUN chmod +x /deploy/code/scripts/configure.sh

COPY conf/etc/supervisor/conf.d/uwsgi.conf /etc/supervisor/conf.d/uwsgi.conf
RUN true
COPY conf/etc/uwsgi/whiteboard.ini /etc/uwsgi/whiteboard.ini

RUN true
COPY whiteboard/ /deploy/code/whiteboard
RUN true
COPY templates/ /deploy/code/templates
RUN true
COPY .coveragerc /deploy/code/.coveragerc
RUN true
COPY db.sqlite3 pytest.ini manage.py /deploy/code/


RUN rm -rf whiteboard/static/*
COPY --from=0 /deploy/code/frontend/build /deploy/code/whiteboard/static

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
