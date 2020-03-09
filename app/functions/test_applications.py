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

    # Ensure that the
    testQuery = "INSERT into applications VALUES ({})".format(
        ",".join(data.values()))

    assert(
        getDb().queries[0] == testQuery)
