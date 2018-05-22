from flask import Flask, render_template, url_for, request, flash, url_for, redirect
from app import app, db

from app.models.forms import UsuarioForm, ProfessorForm, CrudProfessorForm
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

<<<<<<< HEAD
@app.route("/editar-professor/<int:id>", methods=["GET","POST"])
def editar_professor():
    professor = db.session.query(Professor).filter_by(_id=id).first

    if request.method == "POST":
        nome = request.form.get("nome")
        cargo = request.form.get("cargo")
        cpf = request.form.get("cpf")
        rg = request.form.get("rg")
        rua = request.form.get("rua")
        numero = request.form.get("numero")
        bairro = request.form.get("bairro")
        login = request.form.get("login")
        senha = request.form.get("senha")
        # Professor
        #area = request.form.get("area")
        #institucional = request.form.get("institucional")

        if nome and cargo and cpf and rg and rua and numero and bairro and login and senha :
            professor.nome = nome
            professor.cargo = cargo
            professor.cpf = cpf
            professor.rg = rg
            professor.rua = rua
            professor.numero = numero
            professor.bairro = bairro
            professor.login = login
            professor.senha = senha

            db.session.commit
            return redirect(url_for(editar_professor))

        return render_template("editar_professor",data=data)
    form_professor = ProfessorForm()


@app.route("/buscar-professor", methods=["GET", "POST"])
def buscar_professor():
    #usuario = db.session.query(Usuario).filter_by().first
    form_professor = ProfessorForm()
    professor = db.session.query(Professor).all()
    data = [form_professor, professor]
    return render_template("buscar-professor.html", data=data)



@app.route("/crud-professor", methods=["GET","POST"])
def crud_professor():
    form_crud_professor = CrudProfessorForm()
    #usuario = db.session.query(Usuario).all()
    usuario = db.session.query(Usuario).first()
    professor = db.session.query(Professor).all()
    data = [form_crud_professor, usuario, professor]
    return render_template("crud-professor.html", data=data)



@app.route("/crud-professor-executar/<int:id>", methods=["GET","POST"])
def crud_professor_executar():
    professor = db.session.query(Professor).filter_by(_id=id).first

    if request.method == "POST":
        nome = request.form.get("nome")
        cargo = request.form.get("cargo")
        cpf = request.form.get("cpf")
        rg = request.form.get("rg")
        rua = request.form.get("rua")
        numero = request.form.get("numero")
        bairro = request.form.get("bairro")
        login = request.form.get("login")
        senha = request.form.get("senha")


        if nome and cargo and cpf and rg and rua and numero and bairro and login and senha :
            professor.nome = nome
            professor.cargo = cargo
            professor.cpf = cpf
            professor.rg = rg
            professor.rua = rua
            professor.numero = numero
            professor.bairro = bairro
            professor.login = login
            professor.senha = senha

            db.session.commit
            return redirect(url_for(editar_professor))

        return render_template("editar_professor",data=data)
    form_professor = ProfessorForm()
=======

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
>>>>>>> 2f4a1c3f9dad5a21cd49574c48a061325d3e7145
