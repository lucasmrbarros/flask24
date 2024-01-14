from sqlAlchemy import database
class HotelModel(database.Model): #heranca pora a mondelagem da tabela no BD
    #Nome da tabela
    __tablename__ = 'hoteis'

    #mapemaneto
    #pk
    hotel_id = database.Column(database.String, primary_key = True)
    nome = database.Column(database.String(80))
    estrelas = database.Column(database.Float(precision=1))
    diaria = database.Column(database.Float(precision=2))
    cidade = database.Column(database.String(80))

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome' : self.nome,
            'estrelas' : self.estrelas,
            'diaria' : self.diaria,
            'cidade' : self.cidade
        }

    #verifica se o id do hotel é unico
    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id = hotel_id).first()
        if hotel:
            return hotel
        return None

    #salva o hotel no banco de dados
    def save_hotel(self):
        database.session.add(self)
        database.session.commit()

    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def delete_hotel(self):
        database.session.delete(self)
        database.session.commit()