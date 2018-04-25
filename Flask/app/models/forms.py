from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class UsuarioForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    cargo = StringField("cargo", validators=[DataRequired()])
    rg = StringField("rg", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    rua = StringField("rua", validators=[DataRequired()])
    numero = StringField("numero", validators=[DataRequired()])
    bairro = StringField("bairro", validators=[DataRequired()])
    login = StringField("login", validators=[DataRequired()])
    senha = StringField("senha", validators=[DataRequired()])


class ProfessorForm(FlaskForm):
    institucional = StringField("institucional", validators=[DataRequired()])
    area = StringField("area", validators=[DataRequired()])
    usuario = StringField("usuario", validators=[DataRequired()])


class DisciplinaForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    descricao = StringField("descricao", validators=[DataRequired()])
    professor = StringField("professor", validators=[DataRequired()])
