from flask import jsonify, request, make_response
from ..Services.TransferenceServices import TransferenceServices

class TransferenceController:

    @staticmethod
    def transference(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))
            value = str(data.get('value'))
            receiverName = str(data.get('receiverName'))
            receiverCpf = str(data.get('receiverCpf'))
            receiverPhone = str(data.get('receiverPhone'))
            
            return TransferenceServices.transference(userHash, passwordHash, value, receiverName, receiverCpf, receiverPhone, db)
        except:
            return make_response("dsada", 400)