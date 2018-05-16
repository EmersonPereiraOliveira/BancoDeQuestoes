from flask import Flask, render_template, url_for, request, flash, url_for, redirect
from app import app, db

from app.models.forms import UsuarioForm, ProfessorForm
from app.models.tables import Usuario, Professor

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return "Pronto! Servidor OK"


@app.route("/cadastrar-professor", methods=["GET", "POST"])
def cadastrar_professor():
    if request.method == "POST":
        # Usuário
        nome = request.form.get("nome")
        cargo = request.form.get("cargo")
        cpf = request.form.get("cpf")
        rg = request.form.get("rg")
        rua = request.form.get("rua")
        numero = request.form.get("numero")
        bairro = request.form.get("bairro")
        login = request.form.get("login")
        senha = request.form.get("senha")
        #Professor
        area = request.form.get("area")
        institucional = request.form.get("institucional")



        if nome and cargo and cpf and rg and rua and numero and bairro and login and senha and institucional and area:
            usuario = Usuario(nome, cargo, cpf, rg, rua, numero, bairro, login, senha)
            db.session.add(usuario)
            db.session.commit()
            usuario = Usuario.query.filter_by(cpf=cpf).first()
            professor = Professor(institucional, area, usuario.id)
            db.session.add(professor)
            db.session.commit()

            flash("Cadastro de usuário realizado com sucesso!")
            return redirect(url_for('cadastrar_professor'))


    form_usuario = UsuarioForm()
    form_professor = ProfessorForm()
    data = [form_usuario, form_professor]
    return render_template("cadastrar-professor.html", data=data)


@app.route("/cadastrar-disciplina", methods=["GET", "POST"])
def cadastrar_disciplina():
    if request.method == "POST":
        descricao = request.form.get("descricao")
        nome = request.form.get("nome")
        professor = request.form.get("professor")

        if descricao and nome and professor:
            disciplina = Disciplina(nome, descricao, professor)
            db.session.add(disciplina)
            db.session.commit()

            flash("Cadastro de disciplina realizado com sucesso!")
            return redirect(url_for('cadastrar_disciplina'))

    form_disciplina = DisciplinaForm()
    data = form_disciplina
    return render_template("cadastrar-disciplina.html", data=data)