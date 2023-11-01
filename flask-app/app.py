from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # You can specify the port using the `port` parameter in the `run` method.
    app.run(host='0.0.0.0', port=5000)

