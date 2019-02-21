FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install requests
RUN pip install bs4
RUN pip install pandas

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]