class BaseController:
    @classmethod
    def response(self, response, message, code):
        return {
            'result': response,
            'message': message,
            'code': code
        }

class BaseHandler:
    pass