from flask import jsonify, request, make_response
import datetime
from ..Services.CardServices import CardServices
from ..Models import Card
from sqlalchemy import MetaData, Table

class CardController:

    @staticmethod
    def register_card(data, db):
        try:
            cardName = str(data.get('cardName'))
            number = str(data.get('number'))
            cvc = str(data.get('cvc'))
            validity = str(datetime.date(int(data.get('year')), int(data.get('month')), 1))
            name = str(data.get('name'))
            userHash = str(data.get('userHash'))
            r = CardServices.register_card(cardName, number, cvc, validity, name, userHash, db)

            return r 
        except:
            return make_response(jsonify({"message": "Card parameters not correct"}), 400)

       

    @staticmethod
    def get_card(data, db):
        try:
            userHash = str(data.get('userHash'))
            
            data = CardServices.get_card(userHash, db)
            for chave in data.keys():
                print(f"{chave} : {data[chave]}")
            return data
        except:
            return 'f'
    
    @staticmethod
    def get_one_card(data, db):
        try:
            userHash = str(data.get('userHash'))
            id = int(data.get('id'))

            data = CardServices.get_one_card(userHash, id, db)
            return make_response(jsonify({'cardName' : data.cardName, 'number' : data.number, 'cvc' : data.cvc, 'validity' : data.validity, 'name' : data.name}), 200)
        except:
            return make_response(400)
    
    @staticmethod
    def delete_card(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))
            id = int(data.get('id'))

            a = CardServices.delete_card(userHash, passwordHash, id, db)

            return a
        except:
            return make_response(jsonify({"message": "Erro Delete"}),400)
