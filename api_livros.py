'''1 objetivo - Criar um api que disponibiliza a consulta/criação/edição/exclusão de livros
#2 URL base - localhost
#3 Endpoints: 
    - localhost/livros (GET) / Obter todos os livros
    - localhost/livros (POST) / Criar novos livros
    - localhost/livros/id (GET) / Obter livros por id
    - localhost/livros/id (PUT) / Adicionar livros
    - localhost/livros/id (DELETE) / Deletar livros por id
#4 Quais recursos - livros
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Howling'
    },
    {
         'id': 3,
        'titulo': 'James Clear',
        'autor': 'Habitos Atomicos'
    }
]

#consultar(todos)
@app.route('/livros', methods = ['GET'])
def obter_livros():
    return jsonify(livros)

#criar
@app.route('/livros', methods = ['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#consultar(id)
@app.route('/livros/<int:id>', methods = ['GET'])
def consultar_livroid(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#editar
@app.route('/livros/<int:id>', methods = ['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
    return jsonify(livros[indice])
#excluir
@app.route('/livros', methods = 'DELETE')
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True )