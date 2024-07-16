FROM python

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py", "--host", "0.0.0.0"]