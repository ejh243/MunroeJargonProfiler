FROM python:3.5

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "runserver.py"]
