FROM openfaas/classic-watchdog:0.18.1 as watchdog

FROM python:2.7-alpine
RUN mkdir -p /home/app


COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

RUN addgroup -S app && adduser -S -G app app
RUN apk update \
    && apk upgrade \
    && apk --no-cache add --update gcc tcl apache2 ca-certificates cmake gfortran git wget curl graphicsmagick \
    apk-tools curl build-base supervisor cups-client dcron bind-tools rsync libxml2-utils libxslt
RUN apk add --no-cache jpeg-dev zlib-dev
RUN pip install Pillow
RUN pip install numpy
RUN pip install dlib
RUN pip install face_recognition
RUN chown app /home/app



WORKDIR /home/app
COPY requirements.txt .
RUN pip install -r requirements.txt
#COPY index.py .
COPY handler.py .
ENV fprocess="python handler.py"

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
