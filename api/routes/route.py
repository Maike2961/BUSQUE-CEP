from flask import redirect, render_template,request, flash
import requests
from api import app


@app.route("/")
def index():
    return redirect("/busca")

@app.route("/busca", methods=["GET", "POST"])
def busca_cep():
    if request.method == "POST":
        cep = request.form["cep"]
        link_cep = f'https://viacep.com.br/ws/{cep}/json/'
        resp = requests.get(link_cep)
        if(len(cep) == 8):
            try:
                dicta = resp.json()
                content =  dictas(dicta['logradouro'], dicta['bairro'],  dicta['localidade'], dicta['uf'],  dicta['cep'],dicta['ddd'])
                print(content)
            except Exception as e:
                print(f"Erro na requisição {e}")
        elif(len(cep) > 8 or len(cep) < 8):
            flash("Digite corretamente o cep desejado", 'warning')
        else:
            flash("Erro tente novamente", 'danger')
    else:
        print("Erro de conexão")
        content = {
            "rua": "",
            "bairro": "",
            "cidade": "",
            "uf": "",
            "cep": "",
            "ddd": ""
        }
    return render_template('index.html', content=content)


def dictas(rua, bairro, cidade, uf, cep,ddd):
    content = {
        "rua": rua,
        "bairro": bairro,
        "cidade": cidade,
        "uf": uf,
        "cep": cep,
        "ddd": ddd
    }
    return content
