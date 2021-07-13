from app.funcionario.model import Presença
from flask import request, jsonify
from app.extensions import db
from flask.views import MethodView 




class PresençaCreate (MethodView):
    def get(self):
        presença = Presença.query.all()
        return jsonify([presença.json() for presença in presença]), 200


    def post(self):
        dados = request.json 
        dia = dados.get('dia')
        horario_chegada = dados.get('horario_chegada')
        horario_saida = dados.get ('horario_saida')

        if not isinstance (dia,str):
            return {'error':'tipo invalido'}


        presença = Presença(dia, horario_chegada, horario_saida)
        db.session.add (presença)
        db.session.commit()

        return presença.json(), 200

class PresençaDetails(MethodView):
    def get(self, id):
        presença = Presença.query.get_or_404(id)

        return presença.json(), 200

    def put(self, id):
        presença=Presença.query.get_or_404(id)
        dados = request.json

        dia = dados.get('dia')
        horario_chegada = dados.get('horario_chegada')
        horario_saida = dados.get ('horario_saida')

       
       

        presença.dia = dia
        presença.horario_chegada = horario_chegada
        presença.horario_saida = horario_saida
       


        db.session.commit()

        return presença.json(), 200

    def patch(self, id):
        presença=Presença.query.get_or_404(id)
        dados = request.json

        dia = dados.get('dia', presença.dia)
        horario_chegada = dados.get('horario_chegada', presença.horario_chegada)
        horario_saida = dados.get ('horario_saida', presença.horario_saida)

        

        presença.dia = dia
        presença.horario_chegada = horario_chegada
        presença.horario_saida = horario_saida
        db.session.commit()

        return presença.json(), 200
    
    def delete(self, id):
        presença=Presença.query.get_or_404(id)
        db.session.delete(presença)
        db.session.commit()
        return presença.json(), 200



