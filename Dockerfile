# syntax=docker/dockerfile:1

FROM python:3-alpine
COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "mozilfun.py"]