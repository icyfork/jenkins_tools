FROM python:2.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]
ENTRYPOINT ["python", "./jenkins_tools.py"]