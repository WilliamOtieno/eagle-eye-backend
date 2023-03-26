FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN python manage.py migrate || true

CMD python manage.py runserver 0.0.0.0:$PORT
