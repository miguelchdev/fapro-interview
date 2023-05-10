FROM python:3.9-alpine
WORKDIR /opt/fapro_sii/

COPY ./requirements.txt /opt/fapro_sii/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /opt/fapro_sii/requirements.txt

COPY . /opt/fapro_sii

EXPOSE 80

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
