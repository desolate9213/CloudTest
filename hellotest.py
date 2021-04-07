from flask import Flask, render_template
app = Flask (__name__)
@app.route('/')
def Home():
    return "test"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=80)
   # app.run(debug = True)
