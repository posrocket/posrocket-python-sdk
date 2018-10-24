"""
POS Rocket Oauth client Module
"""

from posrocket.services import LocationService


class LocationClient(object):
    """
    Oauth class connect to POSRocket oauth server
    """
    _tab_service = None
    _discount_service = None
    _drawer_service = None
    _extra_charge_service = None
    _order_option_service = None

    def __init__(self, location_id, pos_client):
        """

        :param client_id: POSRocket oauth app client id
        :type client_id: str
        :param client_secret:POSRocket oauth app client secret
        :type client_secret: str
        :param scopes:POSRocket Required scopes
        :type scopes: list
        """
        self.location_id = location_id
        self.pos_client = pos_client

    @property
    def tab_service(self):
        assert self.pos_client.token, "User Token Not Set"
        if not self._tab_service:
            self._tab_service = LocationService(self.pos_client.token, self.location_id)
        return self._tab_service

    @property
    def discount_service(self):
        assert self.pos_client.token, "User Token Not Set"
        if not self._discount_service:
            self._discount_service = LocationService(self.pos_client.token, self.location_id)
        return self._discount_service

    @property
    def drawer_service(self):
        assert self.pos_client.token, "User Token Not Set"
        if not self._drawer_service:
            self._drawer_service = LocationService(self.pos_client.token, self.location_id)
        return self._drawer_service

    @property
    def extra_charge_service(self):
        assert self.pos_client.token, "User Token Not Set"
        if not self._extra_charge_service:
            self._extra_charge_service = LocationService(self.pos_client.token, self.location_id)
        return self._extra_charge_service

    @property
    def order_option_service(self):
        assert self.pos_client.token, "User Token Not Set"
        if not self._order_option_service:
            self._order_option_service = LocationService(self.pos_client.token, self.location_id)
        return self._order_option_service
