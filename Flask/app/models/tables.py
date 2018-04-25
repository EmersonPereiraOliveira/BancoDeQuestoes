from app import db

class Usuario(db.Model):
    # Cria a tabela usuarios
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    cpf = db.Column(db.String(50))
    rg = db.Column(db.String(50))
    rua = db.Column(db.String(50), unique=True)
    numero = db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    login = db.Column( db.String(50))
    senha = db.Column(db.String(50))


    # Defini os atributos de inicialização
    def __init__(self, nome ,cargo,cpf,rg,rua,numero,bairro,login,senha):
        self.nome = nome
        self.cargo = cargo
        self.cpf = cpf
        self.rg = rg
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.login = login
        self.senha = senha


    # Retorna informações sobre o usuário
    def __repr__(self):
            return "<usuario %r>" % self.nome

class Professor(db.Model) :
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    constitucional = db.Column(db.String(50))
    area = db.Column(db.String(50))
    usuario = db.Column(db.Integer,db.ForeignKey(usuario.id))

    def __init__(self, constitucional,area,usuario):
        self.constitucional = constitucional
        self.area = area
        self.usuario = usuario

    def __repr__(self):
        return "<professor %r>" % self.usuario.nome


class Disciplina(db.Model):
    __tablename__ = "disciplinas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(dbString(50))
    professor = db.Column(db.Integer, db.ForeignKey(professor.id))

    def __init__(self,nome,descricao,professor):
        self.nome = nome
        self.descricao = descricao
        self.professor = professor

    def __repr__(self):
        return "<disciplina %r>" % self.nome

