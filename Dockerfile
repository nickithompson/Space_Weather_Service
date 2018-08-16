FROM python:3
ADD run.py /
RUN apt-get update && apt-get install -y python3-tk
RUN pip install -r requirements.txt
CMD ["python", "./run.py"]
