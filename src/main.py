from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<string:nombre>')
def hello_world(nombre=None):
    return render_template('base.html', nombre=nombre)

if __name__ == '__main__':
    app.run(port=8080, debug=True)