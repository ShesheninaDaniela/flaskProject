FROM python:3.8.5

RUN mkdir -p /usr/src/test_calculator
WORKDIR /usr/src/test_calculator

COPY . /usr/scr/test_calculator

RUN pip install flask
RUN pip install pytz

EXPOSE 5000

CMD ["python", "/usr/scr/test_calculator/app.py"]