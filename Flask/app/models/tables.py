from app import db

class Usuario(db.Model):
    # Cria a tabela usuarios
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(50))
    setor = db.Column(db.Integer, db.ForeignKey('setores.id'))

    # Defini os atributos de inicialização
    def __init__(self, nome, email, senha, setor):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.setor = setor

    # Retorna informações sobre o usuário
    def __repr__(self):
            return "<usuario %r>" % self.nome