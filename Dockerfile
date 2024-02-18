FROM alpine:latest

RUN apk add --no-cache python3

RUN mkdir -p /home/data /home/output

COPY project3.py /home/data/script.py
COPY IF.txt /home/data/IF.txt
COPY Limerick-1.txt /home/data/Limerick-1.txt

CMD ["python3", "/home/data/script.py"]