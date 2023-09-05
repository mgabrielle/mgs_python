'''from flask import Flask

# criar rota dentro do app
app = Flask('Meu app')

@app.route('/')
def hello():
    return "Hello World"

@app.route('/novo')
def novo():
    return 'Nova página'
'''

from flask import Flask, render_template


app = Flask('Meu app')

posts = [
    {
        'titulo': 'Minha primeira postagem',
        'texto': 'teste'
    },
    {
        'titulo': 'Segundo Post',
        'texto': 'teste'
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts # Mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)


