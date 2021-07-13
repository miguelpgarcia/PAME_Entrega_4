from app.extensions import db

class Funcionario (db.Model):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20), nullable = False)
    biometria = db.Column(db.String(20), nullable = False)
    
    presença = db.relationship ('Presença', backref = 'funcionario')
 


 