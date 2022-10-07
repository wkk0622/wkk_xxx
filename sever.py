from flask import Flask, request
from plugins import process_func

app = Flask(__name__)


@app.route('/', methods=["POST"])
def listening():  # 监听功能
    ev = request.json  # 避免request.json重复调用
    print(ev)  # 参考gocq数据结构

    for each in process_func:
        each(ev)
    # 加载API
    return '{}'


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5701)
