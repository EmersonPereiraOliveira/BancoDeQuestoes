from flask import Flask, render_template, url_for, request
from app import app, db

from app.models.forms import UsuarioForm, ProfessorForm
from app.models.tables import Usuario, Professor

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return "Pronto! Servidor OK"


@app.route("/cadastrar-professor")
def cadastrar_professor():
    form_usuario = UsuarioForm()
    form_professor = ProfessorForm()
    data = [form_usuario, form_professor]
    return render_template("cadastrar-professor.html", data=data)
