from flask import Flask, render_template, url_for, request, flash, url_for, redirect
from app import app, db

from app.models.forms import ProfessorForm, CrudProfessorForm
from app.models.tables import Usuario, Professor

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/cadastrar-professor", methods=["GET", "POST"])
def cadastrar_professor():
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
        area = request.form.get("area")
        institucional = request.form.get("institucional")
        usuario = request.form.get("usuario")

        if nome and cargo and cpf and rg and rua and numero and bairro and login and senha and institucional and area and usuario:
            professor = Professor(nome, cargo, cpf, rg, rua, numero, bairro, login, senha, institucional, area, usuario)
            db.session.add(professor)
            db.session.commit()
            print("Entrou")
            flash("Cadastro de professor realizado com sucesso!")
            return redirect(url_for('listar_professor'))

    form_professor = ProfessorForm()
    return render_template("professor/cadastrar-professor.html", form_professor=form_professor)


@app.route("/atualizar-professor/<int:id>", methods=["GET","POST"])
@app.route('/atualizar-professor', methods=['POST'])
def atualizar_professor(id):
    if id != None and request.method == "GET":
        professor = Professor.query.filter_by(id=id).first()
        form_professor = ProfessorForm()
        return render_template('professor/atualizar-professor.html', form_professor=form_professor, professor=professor)
    elif request.method == "POST":
        nome = request.form.get("nome")
        cargo = request.form.get("cargo")
        cpf = request.form.get("cpf")
        rg = request.form.get("rg")
        rua = request.form.get("rua")
        numero = request.form.get("numero")
        bairro = request.form.get("bairro")
        login = request.form.get("login")
        senha = request.form.get("senha")
        area = request.form.get("area")
        institucional = request.form.get("institucional")
        usuario = request.form.get("usuario ")
        #Não permitir alterar o usuário
        if nome and cargo and cpf and rua and bairro and login and area and institucional:
            professor = Professor.query.filter_by(id=id).first()
            professor.nome = nome
            professor.cargo = cargo
            professor.cpf = cpf
            professor.rua = rua
            professor.bairro = bairro
            professor.login = login
            professor.senha = senha
            professor.area = area
            professor.institucional = institucional
            db.session.commit()
            flash("Atualização realizada com sucesso!")
        return redirect(url_for('listar_professor'))



@app.route("/listar-professor", methods=["GET", "POST"])
def listar_professor():
    professor = db.session.query(Professor).all()
    return render_template("professor/listar-professor.html", professor=professor)


@app.route('/excluir-professor/<int:id>', methods=['GET', 'POST'])
def excluir_professor(id):
    professor = Professor.query.filter_by(id=id).first()
    if professor:
        db.session.delete(professor)
        db.session.commit()
        flash("Exclusão realizada com sucesso!")
        return redirect(url_for('listar_professor'))
    else:
        flash("Exclusão não conluída!")
        return redirect(url_for('listar_professor'))


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
