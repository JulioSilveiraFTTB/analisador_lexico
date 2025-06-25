"""
Módulo principal da aplicação Flask para o analisador léxico de Pascal.

Este módulo inicializa o app Flask, define as rotas e integra o analisador léxico,
permitindo que o usuário envie códigos ou arquivos para análise via interface web.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from analisador import analyze_code

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Rota principal da aplicação.
    - GET: Renderiza a página inicial, exibindo o formulário e, se houver,
      o resultado da análise.
    - POST: Recebe código via upload de arquivo, executa a análise léxica
      e armazena o resultado na sessão.
    """
    if request.method == "POST":
        code = None
        code_text = request.form.get('code_text')
        file = request.files.get("file")

        if code_text:
            code = code_text
        elif file and file.filename != '':
            code = file.read().decode("utf-8")

        if code:
            tokens = analyze_code(code)
            session['code'] = code
            session['tokens'] = tokens
        else:
            session.pop('code', None)
            session.pop('tokens', None)

        return redirect(url_for('index'))

    code = session.pop('code', None)
    tokens = session.pop('tokens', [])

    response = make_response(
        render_template("index.html", code=code, tokens=tokens)
    )
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    app.run(debug=True)
