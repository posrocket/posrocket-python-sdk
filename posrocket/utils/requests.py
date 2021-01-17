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
        # import json
        # response ='''{"data":[
		# 	{
		# 	    "id": "b6c4fe25-a9d8-4f51-ae6f-3653554b60bc",
		# 	    "name": "10%",
		# 	    "type": "PERCENTAGE",
		# 	    "amount": 0,
		# 	    "rate": 0.1,
		# 	    "locations": [
		# 		"fd78954f-71cb-4b36-b451-0cddeeebcb66",
		# 		"b6c4fe54-a9d9-4f51-ae6f-3653554b60bc",
		# 		"8a68d3d0-7bc0-4bd9-b6bd-283607447f90",
		# 		"a27e29d6-9ec1-44f6-be81-b267f4ba1b41"
		# 	    ],
		# 	    "color": "6F7077",
		# 	    "pin_required": false,
		# 	    "after_tax": false,
		# 	    "item_applicable": false,
		# 	    "automatic": false,
		# 	    "start_date": "2020-02-02 02:00:00",
		# 	    "end_date": "2021-12-22 02:00:00",
		# 	    "days": [{"day":"SUNDAY","time":{"start":"08:00","end":"18:00"}},{"day":"WEDNESDAY","time":{"start":"08:00","end":"18:00"}},{"day":"FRIDAY","time":{"start":"08:00","end":"18:00"}}],
			    
		# 	    "items": [
		# 	    "ca63a0e3-4c12-42d4-b9f6-4754aa0eede4",
		# 	    "a6a6dcb9-86d4-49bc-92e6-44b98d81e81b",
		# 	    "200a6bca-b27c-4f4d-ac67-60acc0eea6ab"
		# 	    ],
		# 	    "categories": [
		# 	    "ca63a0e3-4c12-42d4-b9f6-4754aa0eede4"
		# 	    ]
		# 	},
		# 	{
		# 	    "id": "b6c4fe55-a9d8-4f51-ae6f-3653554b60bc",
		# 	    "name": "20%",
		# 	    "type": "FIXED",
		# 	    "amount": 1,
		# 	    "rate": 0.5,
		# 	    "locations": [
		# 		"fd78954f-71cb-4b36-b451-0cddeeebcb66",
		# 		"b6c4fe54-a9d9-4f51-ae6f-3653554b60bc"
		# 	    ],
		# 	    "color": "6F7077",
		# 	    "pin_required": false,
		# 	    "after_tax": false,
		# 	    "item_applicable": false,
		# 	    "automatic": false,
		# 	    "start_date": null,
		# 	    "end_date": null,
		# 	    "days": [{"day":"SUNDAY","time":{"start":"08:00","end":"18:00"}},{"day":"WEDNESDAY","time":{"start":"08:00","end":"18:00"}},{"day":"FRIDAY","time":{"start":"08:00","end":"18:00"}}],
		# 	    "items": [],
		# 	     "categories": ["d9fd3a96-36f9-4165-93c1-0fa7e7af92d5","42e53332-896c-473a-91c9-774347aa1f1c"]
		# 	},
		# 	{
		# 	    "id": "b6c7fe55-a9d8-4f51-ae6f-3653554b60bc",
		# 	    "name": "30%",
		# 	    "type": "FIXED",
		# 	    "amount":2,
		# 	    "rate": 0.1,
		# 	    "locations": [
		# 	    "b93b750c-80f4-4957-83ac-1886418232da",
		# 	    "e101e528-355a-4394-a647-5a9ce5c376a0"
		# 	    ],
		# 	    "color": "6F7077",
		# 	    "pin_required": false,
		# 	    "after_tax": false,
		# 	    "item_applicable": false,
		# 	    "automatic": false,
		# 	    "start_date": "2020-10-02 02:00:00",
		# 	    "end_date": "2020-12-22 02:00:00",
		# 	    "days": [],
		# 	    "items": [],
		# 	    "categories": []
		# 	},
		# 	{
		# 	    "id": "b2c4fe55-a9d8-4f51-ae6f-3653554b60bc",
		# 	    "name": "50%",
		# 	    "type": "PERCENTAGE",
		# 	    "amount": 0,
		# 	    "rate": 0.1,
		# 	    "locations": [
		# 		"fd78954f-71cb-4b36-b451-0cddeeebcb66",
		# 		"b6c4fe54-a9d9-4f51-ae6f-3653554b60bc"
		# 	    ],
		# 	    "color": "00ff00",
		# 	    "pin_required": true,
		# 	    "after_tax": true,
		# 	    "item_applicable": true,
		# 	    "automatic": true,
		# 	    "start_date": null,
		# 	    "end_date": null,
		# 	    "days": [{"day":"SUNDAY","time":{"start":"08:00","end":"18:00"}},{"day":"WEDNESDAY","time":{"start":"08:00","end":"18:00"}},{"day":"FRIDAY","time":{"start":"08:00","end":"18:00"}}],
		# 	    "items": [
		# 	    "ca63a0e3-4c12-42d4-b9f6-4754aa0eede4",
		# 	    "a6a6dcb9-86d4-49bc-92e6-44b98d81e81b",
		# 	    "200a6bca-b27c-4f4d-ac67-60acc0eea6ab"
		# 	    ],
		# 	    "categories": ["d9fd3a96-36f9-4165-93c1-0fa7e7af92d5","42e53332-896c-473a-91c9-774347aa1f1c"]
		# 	}
        # 	]}'''


        # response = json.loads(response)
        pagination = Pagination(response, self.model_cls)
        return pagination

    def get_detail(self, pk, **kwargs):
        url = self.get_service_url()
        response = self.get(f"{url}/{pk}")
        return self.model_cls(**response)

    def get_with_filter(self, query_string, **kwargs):
        url = self.get_service_url()
        response = self.get(f"{url}?{query_string}")
        if 'count' in response and response['count']:
            if 'data' in response and response['data']:
                return self.model_cls(**response['data'][0])
        return None
