from app.common import getDb, buildResponse, checkCORS
import json

import decimal
import datetime


def alchemyencoder(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


def applications(request):

    cors = checkCORS(request)
    if cors:
        return cors

    request_json = request.get_json()
    print(request_json)

    bits = ["travel", "first_hack", "rating_diversity"]

    if request.method == 'POST':
        if "email" not in request_json:
            return buildResponse('Must contain an email', 400)

        with getDb().connect() as conn:
            conn.execute("INSERT into applications VALUES ({})".format(
                ",".join(request_json[w] if w in bits else '"{0}"'.format(request_json[w]) for w in request_json.keys())))

        return buildResponse('', 200)
    elif request.method == 'GET':

        with getDb().connect() as conn:
            res = conn.execute("select * from applications")

        try:
            return json.dumps([dict(r) for r in res], default=alchemyencoder)
        except:
            return buildResponse('Empty db', 400)

    elif request.method == 'PATCH':
        if "email" not in request_json:
            return buildResponse('Must contain an email', 400)
    else:
        return buildResponse('Must be a POST, GET or PATCH request', 400)
