from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html', nombre="nombre")

if __name__ == '__main__':
    app.run(port=8080,debug=True)