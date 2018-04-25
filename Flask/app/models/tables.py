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
    email = db.Column(db.String(50))


    # Defini os atributos de inicialização
    def __init__(self, nome ,cargo,cpf,rg,rua,numero,bairro,login,senha, email):
        self.nome = nome
        self.cargo = cargo
        self.cpf = cpf
        self.rg = rg
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.login = login
        self.senha = senha
        self.email = email

    # Retorna informações sobre o usuário
    def __repr__(self):
            return "<usuario %r>" % self.nome

class Professor(db.Model) :
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    codInstitucional = db.Column(db.String(50))
    area = db.Column(db.String(50))
    usuario = db.Column(db.Integer,db.ForeignKey('usuarios.id'))

    def __init__(self, codInstitucional,area,usuario):
        self.codInstitucional = codInstitucional
        self.area = area
        self.usuario = usuario

    def __repr__(self):
        return "<professor %r>" % self.usuario.nome


class Disciplina(db.Model):
    __tablename__ = "disciplinas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(dbString(50))
    professor = db.Column(db.Integer, db.ForeignKey('professores.id'))

    def __init__(self,nome,descricao,professor):
        self.nome = nome
        self.descricao = descricao
        self.professor = professor

    def __repr__(self):
        return "<disciplina %r>" % self.nome

class Assunto(db.Model):
    __tablename__ = "assuntos"

    disciplina = db.Column(db.Integer, db.ForeignKey('disciplinas.id'))
    id = db.Column(db.Integer, primary_key=True)
    assunto = db.Column(db.String(50))
    descricao = db.Column(db.String(30))

    def __init__(self, disciplina, id, assunto, descricao):
        self.disciplina = disciplina
        self.id = id
        self.assunto = assunto
        self.descricao = descricao

    def __repr__(self):
        return "<assunto %r>" % self.descricao

class Questao(db.Model):
    __tablename__ = "questoes"

    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(300))
    resposta = db.Conlumn(db.String(300))
    assunto = db.Column(db.Integer, db.ForeignKey('assuntos.id'))
    status = db.Column(db.String(50))


    def __init__(self, id, enunciado, resposta, assunto, status):
        self.id = id
        self.enunciado = enunciado
        self.resposta = resposta
        self.assunto = assunto
        self.status = status

    def __repr__(self):
        return "<questao %r>" % self.enunciado

