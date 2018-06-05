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


class Aluno(Usuario, db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(50))
    usuario = db.Column(db.Integer,db.ForeignKey('usuarios.id'))

    def __init__(self, nome ,cargo,cpf,rg,rua,numero,bairro,login, senha, matricula,usuario):
        super(Aluno, self).__init__(nome ,cargo,cpf,rg,rua,numero,bairro,login,senha)
        self.matricula = matricula
        self.usuario = usuario

    def __repr__(self):
        return "<aluno %r>" % self.usuario.nome

class Questao(db.Model):
    __tablename__ = "questoes"

    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.String(1000))
    enunciado1 = db.Column(db.String(1000))
    enunciado2 = db.Column(db.String(1000))
    enunciado3 = db.Column(db.String(1000))
    enunciado4 = db.Column(db.String(1000))
    resposta = db.Column(db.String(1000))
    disciplina = db.Column(db.Integer,db.ForeignKey('disciplinas.id'))
    status = db.Column(db.Boolean)

    def __init__(self,pergunta, enunciado1, enunciado2, enunciado3, enunciado4,resposta,status,disciplina):
        self.pergunta = pergunta
        self.enunciado1 = enunciado1
        self.enunciado2 = enunciado2
        self.enunciado3 = enunciado3
        self.enunciado4 = enunciado4
        self.resposta = resposta
        self.disciplina = disciplina
        self.status = status

    def __repr__(self):
        return "<questao %r>" % self.enunciado


