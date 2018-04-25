from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class UsuarioForm(FlaskForm):
    nome = StringField("username", validators=[DataRequired()])
    cargo  = StringField("username", validators=[DataRequired()])
    rg = StringField("username", validators=[DataRequired()])
    cpf = StringField("username", validators=[DataRequired()])
    rua = StringField("username", validators=[DataRequired()])