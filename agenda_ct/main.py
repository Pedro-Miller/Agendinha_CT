import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from functions import cria_tabela, login, cadastrar, cria_evento, eventear, eventos

cria_tabela()

calendario = Flask(__name__)
calendario.secret_key = "abc"  
logado = False






@calendario.route("/")
def rota_root():
    return render_template("base.html")


@calendario.route("/cadastro")
def rota_cadastro():
    return render_template("cadastro.html")

@calendario.route("/cadastro", methods =["POST"])
def cadastrando():
    if request.method == "POST":
        n = request.form["nome"]
        d = request.form["dre"]
        s = request.form["senha"]
        return cadastrar(n, d, s)
    
@calendario.route("/login")
def rota_login():
    return render_template("login.html")
    
@calendario.route("/login", methods =["POST"])
def logando():
    if request.method == "POST":
        dre = request.form["dre"]
        senha = request.form["senha"]
        return login(dre,senha)
        
@calendario.route("/home")
def rota_home():
        return render_template("home.html")

@calendario.route("/agenda")
def rota_agenda():
        return render_template("cria.html", evento = "Aqui aparecerão os seus eventos", descricao = "Aqui aparecerão as descrições dos eventos")

@calendario.route("/agenda", methods =["POST"])
def adicionando_evento():
        if request.method == "POST":
            evento = request.form["evento"]
            dia = request.form["dia"]
            mes = request.form["mes"]
            descricao = request.form["descricao"]
            return cria_evento(evento, descricao, dia, mes)

@calendario.route("/criar")
def criar():
            return render_template("criar eventos.html")

@calendario.route("/criar", methods =["POST"])
def criando():
        if request.method == "POST":
            evento = request.form["evento"]
            descricao  = request.form["descrição"]
            dia = request.form["dia"]
            mes = request.form["mes"]
            return eventear(evento, descricao, dia, mes)

@calendario.route("/eventos")
def rota_eventos():
            return render_template("eventos.html")

@calendario.route("/eventos", methods =["POST"])
def eventualmente():
        if request.method == "POST":
            data = request.form["mesada"]
            return render_template("eventos.html", data = data)



calendario.run()

