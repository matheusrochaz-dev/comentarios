from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open("index.txt", "r", encoding="utf-8") as f:
            comentarios = f.read()
    except FileNotFoundError:
        comentarios = "Nenhum comentário ainda."

    # Lê o HTML base
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Insere os comentários no lugar da variável
    return html.replace("{{comentarios}}", comentarios)

@app.route('/comentar', methods=['POST'])
def comentar():
    comentario = request.form.get("comentario", "").strip()
    if comentario:
        with open("index.txt", "a", encoding="utf-8") as f:
            f.write(comentario + "\n\n")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
