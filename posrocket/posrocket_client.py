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
from requests_oauthlib import OAuth2Session

from posrocket.location_client import LocationClient
from posrocket.services.business import BusinessService
from posrocket.services.catalog import CatalogCategoryService, CatalogItemService, CatalogModifierListService, \
    CatalogTagService, CatalogTaxService
from posrocket.services.directory import DirectoryCustomerService
from posrocket.services.geo import CountryService
from posrocket.services.location import LocationService
from posrocket.services.payment_method import PaymentMethodService
from posrocket.utils.assert_value import assert_value
from posrocket.webhook import WebhookReceiver

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LaunchPadClient(object):
    """LaunchPad main client class which is the starting point for integrating with POSRocket
    """

    def __init__(self, client_id: str, client_secret: str, token: str = None, prod=False):
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
        self.prod = prod
        if prod:
            self.base_url = "https://developer.posrocket.com"
        else:
            self.base_url = "https://launchpad.rocketinfra.com"

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
            f'{self.base_url}/oauth/authorize/',
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
            f'{self.base_url}/oauth/token/',
            authorization_response=authorization_response_url,
            client_secret=self.client_secret
        )
        self.token = token
        return token

    def refresh_token(self, token: dict = None) -> dict:
        """Fetch a new access token using a refresh token.

        :param token:The token to use.
        :return: A token dict
        """
        token = token or self.token
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        self.token = self.oauth_client.refresh_token(
            token_url=f'{self.base_url}/oauth/token/',
            refresh_token=token['refresh_token'],
            auth=auth
        )
        return self.token

    def hook_receiver(self,
                      payload,
                      headers,
                      tab_create=None,
                      tab_update=None,
                      item_create=None,
                      item_update=None,
                      item_delete=None,
                      sale_create=None,
                      refund_create=None,
                      customer_create=None,
                      customer_update=None,
                      customer_delete=None) -> LocationClient:
        hookreciver = WebhookReceiver(self,
                                      tab_create,
                                      tab_update,
                                      item_create,
                                      item_update,
                                      item_delete,
                                      sale_create,
                                      refund_create,
                                      customer_create,
                                      customer_update,
                                      customer_delete)
        return hookreciver.handle(payload, headers)

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
        assert_value(self.token)
        return LocationService(self.token, prod=self.prod)

    @property
    def catalog_item_service(self) -> CatalogItemService:
        """build catalog item service to inquire about catalog item

        :return: catalog item service
        """
        assert_value(self.token)
        return CatalogItemService(self.token, prod=self.prod)

    @property
    def catalog_category_service(self) -> CatalogCategoryService:
        """build catalog item service to inquire about catalog item

        :return: catalog item service
        """
        assert_value(self.token)
        return CatalogCategoryService(self.token, prod=self.prod)

    @property
    def business_service(self) -> BusinessService:
        """build business service object to inquire about current business

        :return: business service object
        """
        assert_value(self.token)
        return BusinessService(self.token, prod=self.prod)

    @property
    def directory_customers_service(self) -> DirectoryCustomerService:
        """build directory customers service object to inquire about customers

        :return: directory customers service object
        """
        assert_value(self.token)
        return DirectoryCustomerService(self.token, prod=self.prod)

    @property
    def country_service(self) -> CountryService:
        """build country service object to inquire about countries

        :return: country service object
        """
        assert_value(self.token)
        return CountryService(self.token, prod=self.prod)

    @property
    def catalog_modifier_list_service(self) -> CatalogModifierListService:
        """build country service object to inquire about countries

        :return: country service object
        """
        assert_value(self.token)
        return CatalogModifierListService(self.token, prod=self.prod)

    @property
    def catalog_tax_service(self) -> CatalogTaxService:
        """build country service object to inquire about countries

        :return: country service object
        """
        assert_value(self.token)
        return CatalogTaxService(self.token, prod=self.prod)

    @property
    def catalog_tag_service(self) -> CatalogTagService:
        """build country service object to inquire about countries

        :return: country service object
        """
        assert_value(self.token)
        return CatalogTagService(self.token, prod=self.prod)

    @property
    def payment_methods_service(self) -> PaymentMethodService:
        """build catalog item service to inquire about catalog item

        :return: catalog item service
        """
        assert_value(self.token)
        return PaymentMethodService(self.token, prod=self.prod)
