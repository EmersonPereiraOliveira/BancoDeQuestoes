from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class ProfessorForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    cargo = StringField("cargo", validators=[DataRequired()])
    rg = StringField("rg", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    rua = StringField("rua", validators=[DataRequired()])
    numero = StringField("numero", validators=[DataRequired()])
    bairro = StringField("bairro", validators=[DataRequired()])
    login = StringField("login", validators=[DataRequired()])
    senha = StringField("senha", validators=[DataRequired()])
    institucional = StringField("institucional", validators=[DataRequired()])
    area = StringField("area", validators=[DataRequired()])
    usuario = StringField("usuario", validators=[DataRequired()])


class DisciplinaForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    descricao = StringField("descricao", validators=[DataRequired()])
    professor = StringField("professor", validators=[DataRequired()])

class QuestaoForm(FlaskForm):
    pergunta = StringField("pergunta", validators=[DataRequired])
    enunciado1 = StringField("enunciado1", validators=[DataRequired()])
    enunciado2 = StringField("enunciado2", validators=[DataRequired()])
    enunciado3 = StringField("enunciado3", validators=[DataRequired()])
    enunciado4 = StringField("enunciado4", validators=[DataRequired()])
    resposta = StringField("resposta", validators=[DataRequired()])
    disciplina = StringField("disciplina", validators=[DataRequired()])
    status = StringField("status", validators=[DataRequired()])



class AlunoForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    cargo = StringField("cargo", validators=[DataRequired()])
    rg = StringField("rg", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    rua = StringField("rua", validators=[DataRequired()])
    numero = StringField("numero", validators=[DataRequired()])
    bairro = StringField("bairro", validators=[DataRequired()])
    login = StringField("login", validators=[DataRequired()])
    senha = StringField("senha", validators=[DataRequired()])
    matricula = StringField("matricula", validators=[DataRequired()])
    usuario = StringField("usuario", validators=[DataRequired()])



