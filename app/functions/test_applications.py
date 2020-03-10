from unittest.mock import Mock
from app.functions.applications import applications
from app.common import getDb
import json

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'applications_test.json')


def test_addsSignupToDb():
    with open(my_file) as f:
        data = json.load(f)

    req = Mock(get_json=Mock(return_value=data), method="POST")
    applications(req)

    bits = ["travel", "first_hack", "rating_diversity"]

    testQuery = "INSERT into applications VALUES ({})".format(
        ",".join(data[w] if w in bits else '"{0}"'.format(data[w]) for w in data.keys()))

    print(testQuery)

    assert(
        getDb().queries[0] == testQuery)


def test_getFromDb():
    req = Mock(method="GET")
    res = applications(req)

    print(res)
