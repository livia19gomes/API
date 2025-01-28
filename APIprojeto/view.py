from flask import Flask, jsonify
from main import app, con

@app.route('/livro', methods = ['GET'])
def livro():
    cur = con.cursor()
    cur.execute("SELECT id_livro, titulo, autor, ano_publicacao FROM livro")
    livros = cur.fetchall()
    livro_dic = []
    for livro in livros:
        livro_dic.append({
            'id_livro': livro[0],
            'titulo': livro[1],
            'autor': livro[2],
            'ano_publicacao': livro[3]
        })
        return jsonify(mensagem='Lista de livros', livros=livro_dic)
