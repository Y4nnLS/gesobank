import datetime
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exists
from ..Models.User import User
from flask import make_response, jsonify
from ..Cryptography.AES import encrypt_message, decrypt_message
from ..Cryptography.RSA import rsa_decrypt_message

class TransferenceServices:

    @staticmethod
    def transference(userHash:str, passwordHash:str, value:str, receiverName:str, receiverCpf:str, receiverPhone:str, db: SQLAlchemy):
        try:
            if db.session.query(exists().where(User.userHash == userHash,User.passwordHash == passwordHash)):

                p1 = db.session.query(User).filter_by(userHash=userHash).first()
                
                receiverCpf = str(rsa_decrypt_message(decrypt_message(p1.privatekey), receiverCpf))
                receiverName = str(rsa_decrypt_message(decrypt_message(p1.privatekey), receiverName))
                receiverPhone = str(rsa_decrypt_message(decrypt_message(p1.privatekey), receiverPhone))
                receiverCpf = encrypt_message(receiverCpf)

                if db.session.query(exists().where(User.name == receiverName, User.cpf == receiverCpf, User.phone == receiverPhone)):
                    p1.balance = decrypt_message(p1.balance)

                    value = float(rsa_decrypt_message(decrypt_message(p1.privatekey), value))
                    receiverName = str(rsa_decrypt_message(decrypt_message(p1.privatekey), receiverName))

                    p2 = db.session.query(User).filter_by(cpf=receiverCpf).first()
                    p2.balance = decrypt_message(p2.balance)

                    if(float(p1.balance) >= value):
                        p1.balance = str(float(p1.balance) - value)
                        p1.balance = encrypt_message(p1.balance)
                        if(p2.balance == "0.00"): 
                            p2.balance = str(value)
                            p2.balance = encrypt_message(p2.balance)
                            db.session().commit()
                            db.session().close()
                            return
                        p2.balance = str(float(p2.balance) + value)
                        p2.balance = encrypt_message(p2.balance)
                        db.session().commit()
                        db.session().close()
                    else:
                        return make_response(jsonify({"message": "Insufficient amount, no balance"}), 400)
                else:
                    return make_response(jsonify({"message": "Insufficient amount, no balance"}), 400)
                return make_response(jsonify({"message": "Successful Transference"}), 200)
        except:
            return make_response(jsonify({"message": "Transference parameters not right to put in database"}), 400)