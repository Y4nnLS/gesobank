import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exists
from flask import make_response, jsonify
from ..Models.Card import Card
from ..Models.User import User
from ..Cryptography.AES import encrypt_message, decrypt_message
from ..Cryptography.RSA import rsa_decrypt_message

class CardServices:

    @staticmethod
    def register_card(cardName:str, number:str, cvc:str, validity:str, name:str, userHash:str, db: SQLAlchemy):
        try:
            if(db.session.query(exists().where(User.userHash == userHash))).scalar():

                userData = db.session.query(User).filter_by(userHash=userHash).first()
                number = rsa_decrypt_message(decrypt_message(userData.privatekey), number)
                cvc = rsa_decrypt_message(decrypt_message(userData.privatekey), cvc)
                validity = rsa_decrypt_message(decrypt_message(userData.privatekey), validity)
                
                encrypt_number = encrypt_message(number)
                encrypt_cvc = encrypt_message(cvc)
                encrypt_validity = encrypt_message(validity)

                new_card = Card(cardName = cardName, number = encrypt_number, cvc = encrypt_cvc, validity = encrypt_validity, name = name, userHash = userHash)
                db.session().add(new_card)
                db.session().commit()
                db.session().close()
                return make_response(jsonify({"message": "Card registered successfully"}), 200)
        except:
            return make_response(jsonify({"message": "Card parameters not right to put in database"}), 400)
       
    
    @staticmethod
    def get_one_card(userHash:str, id:int, db:SQLAlchemy):
       try:
            if db.session.query(exists().where(User.userHash == userHash)).scalar():
                if id != None:
                    p1 = db.session.query(Card).filter_by(userHash=userHash, id=id).first()
                    p1.number = decrypt_message(p1.number)
                    p1.cvc = decrypt_message(p1.cvc)
                    p1.validity = decrypt_message(p1.validity)
                    return p1
                else:
                    return make_response(jsonify({"message": "Id not exist"}), 400)
                
            return make_response(jsonify({"message": "User not exist"}), 400)
       except:
           return make_response(jsonify({"message": "User not exist"}), 400)
            

    @staticmethod
    def delete_card(userHash:str, passwordHash:str, id:int, db:SQLAlchemy):
        try:
            if db.session.query(exists().where(User.userHash == userHash, User.passwordHash == passwordHash)).scalar():
                if id != None:
                    p1 = db.session.query(Card).filter_by(id=id, userHash = userHash).first()
                    db.session().delete(p1)
                    db.session().commit()
                    db.session().close()
                    return 'ok'
                else:
                    return make_response(jsonify({"message": "Id not exist"}), 400)
                    
            return make_response(jsonify({"message": "User not exist"}), 400)
        except:
           return make_response(jsonify({"message1": "User not exist"}), 400)