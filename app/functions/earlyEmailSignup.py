from app.common import getDb, buildResponse, checkCORS, getMailchimpClient
from mailchimp3.mailchimpclient import MailChimpError

from email.utils import parseaddr

earlySignupList = "2f3ef0ad67"


def earlyEmailSignup(request):

    cors = checkCORS(request)
    if cors:
        return cors

    request_json = request.get_json()
    print(request_json)

    if request.method == 'POST':
        if "email" not in request_json:
            return buildResponse('Missing email', 400)

        if '@' not in parseaddr(request_json["email"])[1]:
            return buildResponse('Invalid email', 400)

        try:
            print(getMailchimpClient().lists.members.create(list_id=earlySignupList, data={
                "email_address": request_json["email"],
                "status": "subscribed"
            }))
        except MailChimpError as errorData:
            return buildResponse("Email already subscribed!", 400)

        with getDb().connect() as conn:
            conn.execute(
                "INSERT into early_signups VALUES (NULL, %s)", request_json["email"])

        return buildResponse('', 200)
    else:
        return buildResponse('Must be a POST request', 400)
