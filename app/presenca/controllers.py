from app.presenca.model import Presenca
from flask import request, jsonify
from app.extensions import db
from flask.views import MethodView 




class PresencaCreate (MethodView):
    def get(self):
        presenca = Presenca.query.all()
        return jsonify([presenca.json() for presenca in presenca]), 200


    def post(self):
        dados = request.json 
        dia = dados.get('dia')
        horario_chegada = dados.get('horario_chegada')
        horario_saida = dados.get ('horario_saida')
        funcionario_id = dados.get ('funcionario_id')

        if not isinstance (dia,str):
            return {'error':'tipo invalido'}


        presenca = Presenca(dia=dia, horario_chegada=horario_chegada, horario_saida=horario_saida, funcionario_id= funcionario_id)
        db.session.add (presenca)
        db.session.commit()

        return presenca.json(), 200

class PresencaDetails(MethodView):
    def get(self, id):
        presenca = Presenca.query.get_or_404(id)

        return presenca.json(), 200

    def put(self, id):
        presenca=Presenca.query.get_or_404(id)
        dados = request.json

        dia = dados.get('dia')
        horario_chegada = dados.get('horario_chegada')
        horario_saida = dados.get ('horario_saida')
        funcionario_id = dados.get ('funcionario_id')

       
       

        presenca.dia = dia
        presenca.horario_chegada = horario_chegada
        presenca.horario_saida = horario_saida
        presenca.funcionario_id = funcionario_id
       


        db.session.commit()

        return presenca.json(), 200

    def patch(self, id):
        presenca=Presenca.query.get_or_404(id)
        dados = request.json

        dia = dados.get('dia', presenca.dia)
        horario_chegada = dados.get('horario_chegada', presenca.horario_chegada)
        horario_saida = dados.get ('horario_saida', presenca.horario_saida)
        funcionario_id = dados.get ('funcionario_id', presenca.funcionario_id)

        

        presenca.dia = dia
        presenca.horario_chegada = horario_chegada
        presenca.horario_saida = horario_saida
        presenca.funcionario_id = funcionario_id
        db.session.commit()

        return presenca.json(), 200
    
    def delete(self, id):
        presenca=Presenca.query.get_or_404(id)
        db.session.delete(presenca)
        db.session.commit()
        return presenca.json(), 200



