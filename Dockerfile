FROM python:3.12.2-slim-bookworm

RUN mkdir -p /home/vms

COPY . /home/vms

WORKDIR /home/vms

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]

ENTRYPOINT uvicorn app:app --host=0.0.0.0 --port=${PORT:-5000}

