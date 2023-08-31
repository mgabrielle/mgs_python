from flask import Flask

# criar rota dentro do app
app = Flask('Meu app')

@app.route('/')
def hello():
    return "Hello World"

@app.route('/novo')
def novo():
    return 'Nova página'
