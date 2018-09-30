"""
POS Rocket Oauth client Module
"""
from requests_oauthlib import OAuth2Session

from posrocket.utils import Singleton


class POSRocketOAuthClient(object):
    __metaclass__ = Singleton

    """
    Oauth class connect to POSRocket oauth server
    """

    def __init__(self, client_id, client_secret, scopes, redirect_uri):
        """

        :param client_id: POSRocket oauth app client id
        :type client_id: str
        :param client_secret:POSRocket oauth app client secret
        :type client_secret: str
        :param scopes:POSRocket Required scopes
        :type scopes: list
        :param redirect_uri:The url that POSRocket will redirect the user to *should be set in the App settings*
        :type redirect_uri: str
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = scopes
        self.redirect_uri = redirect_uri
        self._state = None
        self.oauth_client = OAuth2Session(client_id=self.client_id,
                                          scope=self.scopes,
                                          redirect_uri=self.redirect_uri)

    @property
    def state(self):
        assert self._state is not None, "cant get state before calling get_authorization_url"
        return self._state

    def get_authorization_url(self):
        """

        :return: return the authorization url where the user will start the oauth flow
        :rtype: list
        """
        authorization_url, state = self.oauth_client.authorization_url(
            'http://localhost:8200/oauth/authorize/',
            access_type="offline"
        )
        self._state = state
        return authorization_url

    def get_token(self, authorization_response_url):
        """

        :param authorization_response_url: full url for the redirect url after the user came back from the oauth flow.
        :type authorization_response_url: str
        :return: A token dict
        :rtype: dict
        """
        token = self.oauth_client.fetch_token(
            'http://host.docker.internal:8200/oauth/token/',
            authorization_response=authorization_response_url,
            client_secret=self.client_secret
        )
        return token
