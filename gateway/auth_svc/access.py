# video @ 1:54:00
import os, requests


def login(request):
    auth = request.authorization
    if not auth:
        return None, ("missing credentials - auth_svc/access.py line 7 - not authorized", 401)

    basicAuth = (auth.username, auth.password)

    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login", auth=basicAuth
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
    