from flask import Flask, request
from plugins import process_func

app = Flask(__name__)


@app.route('/', methods=["POST"])
def listening():
    wkk = request.json
    print(wkk)

    for each in process_func:
        each(wkk)

    return '{}'


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5701)
