from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return "6006021610040 ธงไชย เซียงนอก"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=80)
   # app.run(debug = True)
