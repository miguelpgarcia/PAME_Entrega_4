from app.extensions import db

class Presenca (db.Model):
    __tablename__ = 'presenca'
    dia = db.Column(db.String, nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    horario_chegada = db.Column(db.String(20), nullable = False)
    horario_saida = db.Column(db.String(20), nullable = False)

    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))

    def json(self):
        return {'dia':self.dia,
        'horario_chegada':self.horario_chegada,
        'horario_saida':self.horario_saida
        }
 


