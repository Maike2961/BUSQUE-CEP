from flask import redirect, render_template,request, flash
import requests
from api import app


@app.route("/")
def index():
    
    return redirect("/busca")

@app.route("/busca", methods=["GET", "POST"])
def busca_cep():
    content = {
        "rua": "",
        "bairro": "",
        "cidade": "",
        "uf": "",
        "cep": "",
        "ddd": ""
    }
    if request.method == "POST":
        cep = request.form["cep"]
        link_cep = f'https://viacep.com.br/ws/{cep}/json/'
        resp = requests.get(link_cep)
        if(len(cep) == 8):
            try:
                dicta = resp.json()
                content = {
                    "rua": dicta['logradouro'],
                    "bairro": dicta['bairro'],
                    "cidade": dicta['localidade'],
                    "uf": dicta['uf'],
                    "cep": dicta['cep'],
                    "ddd": dicta['ddd']
                }
                print(content)
            except Exception as e:
                print(f"Erro na requisição {e}")
        elif(len(cep) > 8 or len(cep) < 8):
            flash("Digite corretamente o cep desejado", 'warning')
        else:
            flash("Erro tente novamente", 'danger')
    else:
        print("Erro de conexão")
    return render_template('index.html', content=content)
