from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/echo/<arg>')
def echo(arg):
    return "Echo: {}!".format(arg)

if __name__ == '__main__':
    app.run()