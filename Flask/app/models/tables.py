from app import db

class Usuario(db.Model):
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


class Professor(Usuario, db.Model) :
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    institucional = db.Column(db.String(50))
    area = db.Column(db.String(50))
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    def __init__(self, nome ,cargo,cpf,rg,rua,numero,bairro,login,senha, institucional,area,usuario):
        super(Professor, self).__init__(nome ,cargo,cpf,rg,rua,numero,bairro,login,senha)
        self.institucional = institucional
        self.area = area
        self.usuario = usuario

    def __repr__(self):
        return "<professor %r>" % self.usuario.nome


class Disciplina(db.Model):
    __tablename__ = "disciplinas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(50))
    professor = db.Column(db.Integer, db.ForeignKey('professores.id'))

    def __init__(self,nome,descricao,professor):
        self.nome = nome
        self.descricao = descricao
        self.professor = professor

    def __repr__(self):
        return "<disciplina %r>" % self.nome


class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(50))
    usuario = db.Column(db.Integer,db.ForeignKey('usuarios.id'))

    def __init__(self,matricula,usuario):
        self.matricula = matricula
        self.usuario = usuario

    def __repr__(self):
        return "<aluno %r>" % self.usuario.nome

class Questao(db.Model):
    __tablename__ = "questoes"

    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(1000))
    resposta = db.Column(db.Boolean)
    status = db.Column(db.Boolean)
    disciplina = db.Column(db.Integer,db.ForeignKey('disciplinas.id'))

    def __init__(self,enunciado,resposta,status,disciplina):
        self.enunciado = enunciado
        self.disciplina = disciplina
        self.resposta = resposta
        self.status =status

    def __repr__(self):
        return "<questao %r>" % self.enunciado

