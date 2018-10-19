"""
POSRocket Request Module
"""
import requests


def _handle_response(result):
    if result.status_code == 404:
        return {"error": "Not Found"}, result.status_code

    if result.content:
        return result.json(), result.status_code
    else:
        return "", result.status_code


class POSRocketRequest:

    def __init__(self, auth_token, base_url):
        self.auth_token = auth_token
        self.base_url = base_url

    def _set_headers(self):
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Bearer %s' % self.auth_token,
        }
        return headers

    def _generate_url(self, url):
        if url.startswith("http"):
            return url
        if url.startswith("/"):
            url = url[1:]

        return "%s/%s" % (self.base_url, url)

    def request(self, method, url, params=None, **kwargs):
        params = params if params else {}
        result = requests.request(method, self._generate_url(url), headers=self._set_headers(), params=params, **kwargs)
        return _handle_response(result)

    def get(self, url, params=None, **kwargs):
        return self.request("GET", url, params=params, **kwargs)

    def post(self, url, data, **kwargs):
        return self.request("POST", url, json=data, **kwargs)

    def put(self, url, data, **kwargs):
        return self.request("PUT", url, json=data, **kwargs)

    def patch(self, url, data, **kwargs):
        return self.request("PATCH", url, json=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)
