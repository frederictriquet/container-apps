FROM python:3.9-slim-buster

WORKDIR /usr/src/app
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY client.py requirements.txt ./
RUN python3 -m venv $VIRTUAL_ENV && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python", "./client.py" ]
ENTRYPOINT ["/opt/venv/bin/python3", "/usr/src/app/client.py"]
