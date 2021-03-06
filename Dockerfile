FROM python:alpine

COPY ./requirements.txt /requirements.txt
COPY ./subscribe /subscribe
COPY ./main.py /main.py

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf requirements.txt

EXPOSE 9000

ENTRYPOINT ["python", "/main.py"]
