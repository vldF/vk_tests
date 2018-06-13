from flask import Flask
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['POST'])
def req():
    return '0460daaa'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

