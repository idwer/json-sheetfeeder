FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV TZ=Europe/Amsterdam

RUN pip3 install gspread oauth2client

EXPOSE 80

COPY client_secret.json /app/
COPY spreadsheet.config /app/spreadsheet.config
COPY spreadsheet.py /app/main.py
