from flask import Flask, request
from flask_restful import Resource, Api
from db import Db_Model

app = Flask(__name__)
api = Api(app)
db_model = Db_Model()


usuarios = []


class Usuarios(Resource):

    def get(self, nome):
        usuario = next(filter(lambda x: x['nome'] == nome, usuarios), None)
        return {'usuario': usuario}, 200 if usuario else 404

    def post(self, nome):
        if next(filter(lambda x: x['nome'] == nome, usuarios), None):
            return {'message': "O usuário '{}' já existe".format(nome)}
    
        data = request.get_json()
        usuario = {'nome': nome, 'cpf': data['cpf'], 'email': data['email'], 'data_cadastro': data['data_cadastro']}
        usuarios.append(usuario)
        db_model.insert(usuario)
        return usuario

    def delete(self, nome):
        global usuarios
        usuarios = list(filter(lambda x: x['nome'] != nome, usuarios))
        return {'message': "Item Deletado"}

    def put(self, nome):
        data = request.get_json()
        usuario = next(filter(lambda x: x['nome'] == nome, usuarios), None)
        if usuario is None:
            usuario = {'nome': nome, 'cpf': data['cpf'], 'email': data['email'], 'data_cadastro': data['data_cadastro']}
            usuarios.append(usuario)
            db_model.atualizar(usuario)
        else:
            usuario.update(data)
            db_model.atualizar(data)
        return usuario

class ListarUsuarios(Resource):
    def get(self):
        return {'usuarios': usuarios}


api.add_resource(Usuarios, '/usuarios/<string:nome>')
api.add_resource(ListarUsuarios, '/usuarios')

app.run()