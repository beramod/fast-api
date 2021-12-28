from starlette.requests import Request
from src.crud.mongodb.api_history.ninies_api_history import NinesApiHistoryCollection


class ApiHistoryUtil:
    @classmethod
    async def logging_api_history(cls, request: Request, response_time, status_code, error_message = None):
        a_key = request.state.query_params.get('aKey')
        u_key = request.state.query_params.get('uKey')
        referer = request.state.referer
        access_key = a_key if a_key else request.state.session.get('id')
        access_category = 'apiKey' if a_key else 'userKey'
        body = None
        if error_message:
            body = error_message
        doc = {
            'clientIp': request.client.host,
            'port': request.client.port,
            'accessCategory': access_category,
            'accessKey': access_key,
            'referer': referer,
            'method': request.method,
            'path': request.method,
            'parameter': request.state.query_params,
            'body': body,
            'responseTime': response_time,
            'statusCode': status_code
        }
        return await NinesApiHistoryCollection.insert_api_history(doc)