from flask import Flask
from flask_restful import Api
from resource.hoteis import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)
#configurando a conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

@app.before_request
def create_database():
    database.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sqlAlchemy import database
    database.init_app(app)
    app.run(debug=True)