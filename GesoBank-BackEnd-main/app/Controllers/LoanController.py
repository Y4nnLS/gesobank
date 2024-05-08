from flask import jsonify, request, make_response
from ..Services.LoanServices import LoanServices

class LoanController:

    @staticmethod
    def loan(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))
            value = str(data.get('value'))

            return LoanServices.loan(userHash, passwordHash, value, db)
        except:
            return make_response("dsdsda", 400)