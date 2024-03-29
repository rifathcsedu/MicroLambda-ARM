FROM openfaas/classic-watchdog:0.18.1 as watchdog

FROM python:3-alpine

# Allows you to add additional packages via build-arg
ARG ADDITIONAL_PACKAGE

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog
RUN apk --no-cache add ${ADDITIONAL_PACKAGE}

# Add non root user
RUN addgroup -S app && adduser app -S -G app
RUN apk update \
    && apk upgrade \
    && apk --no-cache add --update gcc tcl apache2 ca-certificates cmake gfortran git wget curl graphicsmagick \
    apk-tools curl build-base supervisor cups-client dcron bind-tools rsync libxml2-utils libxslt
RUN apk add --no-cache jpeg-dev zlib-dev
RUN pip install Pillow
RUN pip install numpy
RUN pip install dlib
RUN pip install face_recognition
WORKDIR /home/app/

COPY index.py           .
COPY requirements.txt   .

RUN chown -R app /home/app && \
  mkdir -p /home/app/py && chown -R app /home/app
USER app
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python

RUN pip install -r requirements.txt --target=/home/app/python

RUN mkdir -p function
RUN touch ./function/__init__.py

WORKDIR /home/app/function/
COPY function/requirements.txt	.

RUN pip install -r requirements.txt --target=/home/app/python

WORKDIR /home/app/

USER root

COPY function           function
RUN echo "$(ls)"
RUN chown -R app:app ./ && \
  chmod -R 777 /home/app/python

USER app

ENV fprocess="python3 index.py"
EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
