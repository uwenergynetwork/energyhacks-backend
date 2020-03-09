from app.common import getDb, buildResponse, checkCORS
import json


def applications(request):

    cors = checkCORS(request)
    if cors:
        return cors

    request_json = request.get_json()
    print(request_json)

    if request.method == 'POST':
        if "email" not in request_json:
            return buildResponse('Must contain an email', 400)

        with getDb().connect() as conn:
            conn.execute("INSERT into applications VALUES (%s)",
                         ",".join(request_json.values()))

        return buildResponse('', 200)
    elif request.method == 'GET':

        with getDb().connect() as conn:
            res = conn.execute("select * from applications")

        return json.dumps([dict(r) for r in res])

    elif request.method == 'PATCH':
        if "email" not in request_json:
            return buildResponse('Must contain an email', 400)
    else:
        return buildResponse('Must be a POST, GET or PATCH request', 400)
