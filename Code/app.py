from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

usuarios = []

class Usuarios(Resource):

    def get(self, name):
        usuario = next(filter(lambda x: x['name'] == name, usuarios), None)
        return {'usuario': usuario}, 200 if usuario else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, usuarios), None):
            return {'message': "O usuário '{}' já existe".format(name)}
    
        data = request.get_json()
        usuario = {'name': name, 'cpf': data['cpf'], 'email': data['email'], 'data_cadastro': data['data_cadastro']}
        usuarios.append(usuario)
        return usuario

    def delete(self, name):
        global usuarios
        usuarios = list(filter(lambda x: x['name'] != name, usuarios))
        return {'message': "Item Deletado"}

    def put(self, name):
        data = request.get_json()
        usuario = next(filter(lambda x: x['name'] == name, usuarios), None)
        if usuario is None:
            usuario = {'name': name, 'cpf': data['cpf'], 'email': data['email'], 'data_cadastro': data['data_cadastro']}
            usuarios.append(usuario)
        else:
            usuario.update(data)
        return usuario

class ListarUsuarios(Resource):
    def get(self):
        return {'usuarios': usuarios}


api.add_resource(Usuarios, '/usuarios/<string:name>')
api.add_resource(ListarUsuarios, '/usuarios')

app.run()