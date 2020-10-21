import logging

from requests_oauthlib import OAuth2Session

from posrocket.excaptions import NotFoundException
from posrocket.excaptions.not_authenticated_exception import NotAuthenticatedException
from posrocket.excaptions.not_authorized_exception import NotAuthorizedException
from posrocket.utils.pagination import Pagination

logger = logging.getLogger("posrocket-sdk")


def _handle_response(result):
    if result.status_code == 404:
        raise NotFoundException("The endpoint you requested does not exist")
    if result.status_code == 403:
        raise NotAuthorizedException("You don't have access to this endpoint, "
                                     "please check if you provide a valid and active token and your have the correct scopes.")
    if result.status_code == 401:
        raise NotAuthenticatedException("Invalid Access Token")
    logger.info(result.content)
    if result.content:
        output = result.json()
        logger.info(output)
        return output
    else:
        return ""


class LocationRequiredMixin:

    def __init__(self, access_token, location_id, prod=False):
        self.location_id = location_id
        super(LocationRequiredMixin, self).__init__(access_token, prod=prod)

    def get_service_url(self):
        return self.service_url % self.location_id

    def get_update_service_url(self):
        return self.update_service_url % (self.location_id, self.tab_id)

    def get_calculate_service_url(self):
        return self.calculate_service_url % self.location_id


class Requests:

    def __init__(self, access_token, prod=False):
        self.access_token = access_token
        self.client = OAuth2Session(token=access_token)
        if prod:
            self.base_url = 'https://developer.posrocket.com/api/v1'
        else:
            self.base_url = 'https://launchpad.rocketinfra.com/api/v1'

    def get_service_url(self):
        return self.service_url

    def _generate_url(self, url):
        if url.startswith("http"):
            return url
        if url.startswith("/"):
            url = url[1:]

        return "%s/%s" % (self.base_url, url)

    def request(self, method, url, params=None, **kwargs):
        params = params if params else {}
        result = self.client.request(method, self._generate_url(url), params=params, **kwargs)
        print(result.content)
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
        logger.info('***********8')
        logger.info(url)
        return self.request("DELETE", url, **kwargs)

    def get_list(self, **kwargs):
        params = kwargs
        url = self.get_service_url()
        response = self.get(url, params=params)
        pagination = Pagination(response, self.model_cls)
        return pagination

    def get_detail(self, pk, **kwargs):
        url = self.get_service_url()
        response = self.get(f"{url}/{pk}")
        return self.model_cls(**response)

    def get_with_filter(self, query_string, **kwargs):
        url = self.get_service_url()
        response = self.get(f"{url}?{query_string}")
        return self.model_cls(**response)
