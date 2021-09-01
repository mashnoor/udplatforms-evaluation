FROM python:3.9.6-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN mkdir src

RUN pip install -U pip
ADD requirements.txt /app
RUN pip install -r requirements.txt

COPY src/ /app/src/

EXPOSE 8030
CMD ["python", "src/main.py"]