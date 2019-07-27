from time import sleep

from flask import Flask, Response
from flask import request
from flask import render_template
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/find/', methods=['POST'])
def find():
    sleep(100000)
    if request.method == 'POST':
        if "findText" in request.form.keys:
            findText = request.form["findText"]
            # todo: Запустить асинхронно цепочку - очистака Сергея, запрос к сервису Романа, запрос к БД
        else:
            return "Error field"
    return "success: " + findText


@app.route("/stream")
def stream():
    def eventStream():
        while True:
            if random.randint(0, 100) == 33:
                yield "data: {'rand is 33'}"
    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run()
