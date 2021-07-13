from app.extensions import db

class Presença (db.Model):
    __tablename__ = 'presença'
    dia = db.Column(db.Integer, primary_key = True)
    horario_chegada = db.Column(db.String(20), nullable = False)
    horario_saida = db.Column(db.String(20), nullable = False)

    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))


