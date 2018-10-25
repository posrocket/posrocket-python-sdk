"""
POS Rocket Oauth client Module
"""
import requests
from requests_oauthlib import OAuth2Session

from posrocket.location_client import LocationClient
from posrocket.services import BusinessService, LocationService, TabService
from posrocket.services.catalog import CatalogItemService


class POSRocketClient(object):
    """
    Oauth class connect to POSRocket oauth server
    """
    _location_service = None
    _catalog_item_service = None
    _business_service = None
    _tab_service = None

    def __init__(self, client_id, client_secret, token=None):
        """

        :param client_id: POSRocket oauth app client id
        :type client_id: str
        :param client_secret:POSRocket oauth app client secret
        :type client_secret: str
        :param token:POSRocket Required scopes
        :type token: list
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self._state = None
        self.token = token
        self.oauth_client = OAuth2Session(client_id=self.client_id)

    @property
    def state(self):
        assert self._state is not None, "cant get state before calling get_authorization_url"
        return self._state

    def get_authorization_url(self, redirect_uri):
        """

        :return: return the authorization url where the user will start the oauth flow
        :rtype: list
        """
        self.oauth_client.redirect_uri = redirect_uri
        authorization_url, state = self.oauth_client.authorization_url(
            'http://localhost:8200/oauth/authorize/',
            access_type="offline"
        )
        self._state = state
        return authorization_url

    def get_token(self, authorization_response_url, redirect_uri):
        """

        :param authorization_response_url: full url where the user will start the oauth flow.
        :type authorization_response_url: str
        :param redirect_uri: full url for the redirect url after the user came back from the oauth flow.
        :type redirect_uri: str
        :return: A token dict
        :rtype: dict
        """
        self.oauth_client.redirect_uri = redirect_uri
        token = self.oauth_client.fetch_token(
            'http://host.docker.internal:8200/oauth/token/',
            authorization_response=authorization_response_url,
            client_secret=self.client_secret
        )
        self.token = token
        return token

    def refresh_token(self, refresh_token):
        """

        :param refresh_token: User refresh token.
        :type refresh_token: str
        :return: A token dict
        :rtype: dict
        """

        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        token = self.oauth_client.refresh_token(
            token_url='http://host.docker.internal:8200/oauth/token/',
            refresh_token=refresh_token,
            auth=auth
        )
        return token

    def location(self, location_id):
        return LocationClient(location_id, self)

    @property
    def location_service(self):
        assert self.token, "User Token Not Set"
        if not self._location_service:
            self._location_service = LocationService(self.token)
        return self._location_service

    @property
    def catalog_item_service(self):
        assert self.token, "User Token Not Set"
        if not self._catalog_item_service:
            self._catalog_item_service = CatalogItemService(self.token)
        return self._catalog_item_service

    @property
    def business_service(self):
        assert self.token, "User Token Not Set"
        if not self._business_service:
            self._business_service = BusinessService(self.token)
        return self._business_service

    @property
    def tab_service(self):
        assert self.token, "User Token Not Set"
        if not self._tab_service:
            self._tab_service = TabService(self.token)
        return self._tab_service
