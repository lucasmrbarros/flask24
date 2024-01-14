from flask_restful import  Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'Hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            return hotel, 200
        return {'message' : 'Hotel Not Found'}, 404
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"Message:" : "The hotel '{}' already exists!".format(hotel_id)}, 400

        dados = Hotel.argumentos.parse_args()

        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()

        return hotel.json() , 200
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_exisente = HotelModel.find_hotel(hotel_id)

        if hotel_exisente:
            hotel_exisente.update_hotel(**dados)
            hotel_exisente.save_hotel()
            return hotel_exisente.json(), 200
        novo_hotel = HotelModel(hotel_id, **dados)
        return novo_hotel.json(), 201
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            hotel.delete_hotel()
            return {'Messsage':'Hotel Deleted.'}
        return {'Message: ' : 'Hotel Not Found'}, 404