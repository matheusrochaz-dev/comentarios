from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        with open("index.txt", "r", encoding="utf-8") as f:
            comentarios = f.read().replace("\n", "<br>")
    except FileNotFoundError:
        comentarios = "Nenhum comentário ainda."
    return render_template("index.html", comentarios=comentarios)

@app.route('/comentar', methods=['POST'])
def comentar():
    comentario = request.form.get("comentario", "").strip()
    if comentario:
        with open("index.txt", "a", encoding="utf-8") as f:
            f.write(comentario + "\n\n")
    return redirect(url_for("index"))  # ✅ Correto

if __name__ == '__main__':
    app.run(debug=True)
