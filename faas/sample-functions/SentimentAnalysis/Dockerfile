FROM openfaas/classic-watchdog:0.18.8 as watchdog

FROM python:2.7-alpine
RUN pip install textblob && \
    python -m textblob.download_corpora

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

RUN addgroup -g 1000 -S app && adduser -u 1000 -S app -G app
USER 1000

WORKDIR /home/app

COPY requirements.txt   .
RUN pip install -r requirements.txt

RUN python -m textblob.download_corpora

COPY handler.py .
ENV fprocess="python handler.py"

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
