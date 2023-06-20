FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN pip install tensorflow==2.10.0

COPY . /app

CMD ["uvicorn", "qa_app:app", "--host", "0.0.0.0", "--port", "8000"]

