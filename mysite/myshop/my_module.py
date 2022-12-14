import json
from urllib.request import urlopen


def check_session(request, session_name):
    return session_name in request.session


def read_json(url):
    url_response = urlopen(url)
    data = json.loads(url_response.read().decode())
    return data