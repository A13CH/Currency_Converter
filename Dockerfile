# Dockerfile to create the container image for the Currency converter app
FROM python:3.12
LABEL maintainer="Alec Hoelscher <alechoelscher@Alecs-MacBook-Pro.com>"

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/America/Phoenix /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

COPY . /Currency_Converter
RUN pip install --no-cache-dir --upgrade -r /Currency_Converter/requirements.txt
RUN chmod +x /Currency_Converter/healthcheck.sh
WORKDIR /Currency_Converter/

EXPOSE 8000

#  prevents Python from writing .pyc files to disk
#  ensures that the python output is sent straight to terminal (e.g. the container log) without being first buffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/currency_converter

#  playing with the secret key
ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

CMD ["python3.12",  "-m", "streamlit", "run", "--server.port", "8000", "./src/Currency_Converter.py"]
