from cgitb import html
from webbrowser import get
from flask import Flask, render_template, request, flash, redirect, url_for
import random

# -- Estruturas e Funcoes ---


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


def mudarValoresKnapSack(W, wt, val, n):
    wt.clear()
    val.clear()
    for i in range(0, 5):
        wt.append(random.randint(1, 32))
        val.append(random.randint(1, 32))
    wt.sort()
    val.sort()
    W = random.randint(15, 30)
    n = len(val)
    return W, wt, val, n


adj_list = {
    "1": ["2", "7", "8"],
    "2": ["7", "1", "8"],
    "3": ["7"],
    "4": ["6", "8"],
    "5": ["5", "10"],
    "6": ["4", "5"],
    "7": ["1", "3", "4"],
    "8": ["1", "4", "9"],
    "9": ["8"],
    "10": ["5"],

}
# ---  Variaveis Globais ---
global val
val = [1, 6, 18, 22, 26]
global wt
wt = [1, 2, 5, 6, 7]
global W
W = 11
global n
n = len(val)

# --- Aplicacao ---

app = Flask(__name__)  # sempre ao iniciar um site
app.config['SECRET_KEY'] = "minha-palavra-secreta"

# criar a primeira página do site
# route -> caminho que vem depois do dominio

# funcao -> o que quero exibir naquela página
# template


@app.route('/', methods=['GET', 'POST'])
def homepage():
    no = "1"
    if request.method == "GET":
        return render_template("homepage.html", no=no)

    else:

        palpite = str(request.form.get("name"))

        if (palpite in adj_list[no]):
            no = palpite
            return redirect(url_for('caminho', no_destino=no))
        else:
            return redirect(url_for('errou'))


@app.route('/caminho/<no_destino>', methods=['GET', 'POST'])
def caminho(no_destino):
    no = no_destino
    global val
    global wt
    global W
    global n
    resposta = knapSack(W, wt, val, n)
    if request.method == "GET":
        return render_template("caminho.html", no=no,
                               valor0=val[0], peso0=wt[0],
                               valor1=val[1], peso1=wt[1],
                               valor2=val[2], peso2=wt[2],
                               valor3=val[3], peso3=wt[3],
                               valor4=val[4], peso4=wt[4],
                               resposta=resposta, peso=W
                               )

    else:
        try:
            valor = int(request.form.get("valor"))
            if(valor == resposta):
                flash("Resposta Certa!", "success")
                return redirect(url_for('caminho', no_destino=no))
            if(valor != resposta):
                flash("Resposta errada!", "warning")
                return redirect(url_for('caminho', no_destino=no))
        except:
            palpite = str(request.form.get("name"))
            if (palpite == "10" and palpite in adj_list[no]):
                return redirect(url_for('vitoria'))
            if (palpite in adj_list[no]):
                no = palpite
                W, wt, val, n = mudarValoresKnapSack(W, wt, val, n)
                return redirect(url_for('caminho', no_destino=no))
            else:
                return redirect(url_for('errou'))


@app.route('/errou', methods=['GET', 'POST'])
def errou():
    return render_template("errou.html")


@app.route('/vitoria', methods=['GET', 'POST'])
def vitoria():
    return render_template("vitoria.html")


@app.route('/modal')
def modal():
    return render_template('modal.html',)


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
