from app.funcionario.model import Funcionario
from flask import request, jsonify
from app.extensions import db
from flask.views import MethodView 
import bcrypt



class FuncionariosCreate (MethodView): #/funcionario/create
    def get(self):
        funcionario=Funcionario.query.all()
        return jsonify([funcionario.json() for funcionario in funcionario]), 200


    def post(self):
        dados = request.json 
        nome = dados.get('nome')
        cpf = dados.get ('cpf')
        idade = dados.get ('idade')
        email = dados.get ('email')
        senha = dados.get ('senha')
    

        if not isinstance (nome,str):
            return {'error':'tipo invalido'}

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())


        funcionario = Funcionario(nome=nome, cpf=cpf, idade=idade, email=email, senha_hash=senha_hash)
        db.session.add (funcionario)
        db.session.commit()

        return funcionario.json(), 200

class FuncionariosDetails(MethodView): #/funcionario/details/<int:id>
    def get(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        
        return funcionario.json(), 200

    def put(self, id):
        funcionario=Funcionario.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome')
        email = dados.get ('email')
        cpf = dados.get ('cpf')
        idade = dados.get ('idade')
       

        funcionario.nome = nome
        funcionario.email = email
        funcionario.cpf = cpf
        funcionario.idade = idade


        db.session.commit()

        return funcionario.json(), 200

    def patch(self, id):
        funcionario=Funcionario.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome', funcionario.nome)
        email = dados.get ('email', funcionario.email)
        cpf = dados.get ('cpf', funcionario.cpf)
        idade = dados.get ('idade', funcionario.idade)
        

        funcionario.nome = nome
        funcionario.email = email
        funcionario.cpf = cpf
        funcionario.idade = idade

        db.session.commit()

        return funcionario.json(), 200
    
    def delete(self, id):
        funcionario=Funcionario.query.get_or_404(id)
        db.session.delete(funcionario)
        db.session.commit()
        return funcionario.json(), 200



