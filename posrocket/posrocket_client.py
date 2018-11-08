# -*- coding: utf-8 -*-
"""LaunchPad Python SDK.
This is the Official python SDK for POSRocket Developer portal API aka "LaunchPad"
which allow developer to access the resource server with ease.

quick start:
    - install pos python sdk using:
        `pip install pos-python-sdk`
    - import pos module in your python script:
        `from posrocket import LaunchPadClient`
    - create client object:
        `pos_client = LaunchPadClient(<your_oauth_client_id>,<your_oauth_client_secret>)`
    - generate authorization url:
        `auth_url = pos_client.get_authorization_url(<your_redirect_url>)`
    - After the user authorize the app on LaunchPad we will redirect him back to the return url.
    - retrieve the access_token from the return url by using the following function:
        `token = pos_client.get_token(<full_return_url_with_queryparams>,<your_redirect_url>)`
    - now you can call any API endpoint by calling the corresponding service
        `business_info = pos_client.business_service.get_business_info()`



"""
import requests
from posrocket.location_client import LocationClient
from posrocket.services import BusinessService, LocationService
from posrocket.services.catalog import CatalogItemService
from posrocket.services.directory import DirectoryCustomerService
from posrocket.services.geo import CountryService
from requests_oauthlib import OAuth2Session

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LaunchPadClient(object):
    """LaunchPad main client class which is the starting point for integrating with POSRocket
    """
    _location_service = None
    _catalog_item_service = None
    _business_service = None
    _tab_service = None
    _directory_customers_service = None
    _country_service = None

    def __init__(self, client_id: str, client_secret: str, token: str = None):
        """
        define client object for communicating with LaunchPad API
        :param client_id: LaunchPad Oauth Client id
        :param client_secret: LaunchPad OAuth Client Secret
        :param token: optional LaunchPad OAuth Access Token if you already have it stored
        and don't wanna go through the OAuth flow again
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self._state = None
        self.token = token
        self.oauth_client = OAuth2Session(client_id=self.client_id)

    @property
    def state(self) -> str:
        """The state parameter is used to protect against XSRF.
        Your application generates a random string and send it to the authorization server using the state parameter.
        The authorization server send back the state parameter. If both state are the same => OK.
        If state parameters are different, someone else has initiated the request.
        :return: state string
        """
        assert self._state is not None, "cant get state before calling get_authorization_url"
        return self._state

    def get_authorization_url(self, redirect_uri: str) -> str:
        """Form an authorization URL.

        :param redirect_uri: Redirect URI you registered as callback
        :return: authorization_url
        """
        self.oauth_client.redirect_uri = redirect_uri
        authorization_url, state = self.oauth_client.authorization_url(
            'http://52.208.64.108/oauth/authorize/',
            access_type="offline"
        )
        self._state = state
        return authorization_url

    def get_token(self, authorization_response_url: str, redirect_uri: str) -> dict:
        """Method for fetching an access token from the token endpoint.

        :param authorization_response_url: Authorization response URL, the callback
                                           URL of the request back to you.
        :param redirect_uri:Redirect URI you registered as callback
        :return: A token dict
        """
        self.oauth_client.redirect_uri = redirect_uri
        token = self.oauth_client.fetch_token(
            'http://52.208.64.108/oauth/token/',
            authorization_response=authorization_response_url,
            client_secret=self.client_secret
        )
        self.token = token
        return token

    def refresh_token(self, token: dict) -> dict:
        """Fetch a new access token using a refresh token.

        :param token:The token to use.
        :return: A token dict
        """

        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        token = self.oauth_client.refresh_token(
            token_url='http://52.208.64.108/oauth/token/',
            refresh_token=token['refresh_token'],
            auth=auth
        )
        return token

    def location(self, location_id: str) -> LocationClient:
        """ build location client to allow access to that location data

        :param location_id: POSRocket location id
        :return: location client object
        """
        return LocationClient(location_id, self)

    @property
    def location_service(self) -> LocationService:
        """ build location service object to inquire about locations

        :return: location service object
        """
        assert self.token, "User Token Not Set"
        if not self._location_service:
            self._location_service = LocationService(self.token)
        return self._location_service

    @property
    def catalog_item_service(self) -> CatalogItemService:
        """build catalog item service to inquire about catalog item

        :return: catalog item service
        """
        assert self.token, "User Token Not Set"
        if not self._catalog_item_service:
            self._catalog_item_service = CatalogItemService(self.token)
        return self._catalog_item_service

    @property
    def business_service(self) -> BusinessService:
        """build business service object to inquire about current business

        :return: business service object
        """
        assert self.token, "User Token Not Set"
        if not self._business_service:
            self._business_service = BusinessService(self.token)
        return self._business_service

    @property
    def directory_customers_service(self) -> DirectoryCustomerService:
        """build directory customers service object to inquire about customers

        :return: directory customers service object
        """
        assert self.token, "User Token Not Set"
        if not self._directory_customers_service:
            self._directory_customers_service = DirectoryCustomerService(self.token)
        return self._directory_customers_service

    @property
    def country_service(self) -> CountryService:
        """build country service object to inquire about countries

        :return: country service object
        """
        assert self.token, "User Token Not Set"
        if not self._country_service:
            self._country_service = CountryService(self.token)
        return self._country_service
