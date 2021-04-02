FROM python:3.9

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app
CMD ["gunicorn","--bind","0.0.0.0:5000","app:app"]