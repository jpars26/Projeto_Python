import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData


#cria o banco
engine = db.create_engine('sqlite:///banco.db', echo=True)

#cria uma coleçao de objetos de tabela
meta = MetaData()



class Db_Model():
    
    user_tbl = Table(
        'Usuario', meta,
        Column('id', Integer, primary_key = True),
        Column('nome', String),
        Column('cpf', String),
        Column('email', String),
        Column('data_cadastro', String),

    )

    #inserir dados
    def insert(self, user):
        
        ins = self.user_tbl.insert()
        ins = self.user_tbl.insert().values(nome = user['nome'] , cpf = user['cpf'], email = user['email'] , data_cadastro = user['data_cadastro'])
        conn = engine.connect()
        result = conn.execute(ins)
        return result

    #atualizar dados
  #  def atualizar(self, user):
        
        
   #     att = self.user_tbl.update(user).where(user.c.nome['nome'] == user['nome']).values(nome = user['nome'])
    #    conn = engine.connect()
   #     conn.execute(att)
   #     s = user_tbl.select()
   #     conn.execute(s).fetchall()

    #deleta do banco pelo ID
    #delete = user_tbl.delete().where(user_tbl.c.id > 1)
    #conn.execute(delete)