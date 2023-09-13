import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def listar_usuarios():
    return render_template('listar_usuarios.html')

@app.route('/table.html')
def table():
    return send_from_directory("static", 'table.html')

if __name__ == '__main__':
    app.run(debug=True)

