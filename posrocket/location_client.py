"""
Launchpad Location Client
"""
from posrocket.services import TabService
from posrocket.services.location.discount import LocationDiscountService
from posrocket.services.location.drawer import LocationDrawerService
from posrocket.services.location.extra_charge import LocationExtraChargeService
from posrocket.services.location.order_option import LocationOrderOptionService

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationClient(object):
    """Location Client class to allow retrieving data for a specific location
    """
    _tab_service: TabService = None
    _discount_service: LocationDiscountService = None
    _drawer_service: LocationDrawerService = None
    _extra_charge_service: LocationExtraChargeService = None
    _order_option_service: LocationOrderOptionService = None

    def __init__(self, location_id: str, lunch_pad_client: 'posrocket.LunchPadClient'):
        """create a location client to allow access to location related services

        :param location_id: POSRocket location id to get services for
        :param lunch_pad_client: LunchPadClient object to access tokens and auth related info
        """
        self.location_id = location_id
        self.lunch_pad_client = lunch_pad_client

    @property
    def tab_service(self) -> TabService:
        """build tab service object to inquire about location tabs

        :return: tab service object
        """
        assert self.lunch_pad_client.token, "User Token Not Set"
        if not self._tab_service:
            self._tab_service = TabService(self.lunch_pad_client.token, self.location_id)
        return self._tab_service

    @property
    def discount_service(self) -> LocationDiscountService:
        """build discount service object to inquire about location discounts

        :return: discount service object
        """
        assert self.lunch_pad_client.token, "User Token Not Set"
        if not self._discount_service:
            self._discount_service = LocationDiscountService(self.lunch_pad_client.token, self.location_id)
        return self._discount_service

    @property
    def drawer_service(self) -> LocationDrawerService:
        """build drawer service object to inquire about location drawers

        :return: drawer service object
        """
        assert self.lunch_pad_client.token, "User Token Not Set"
        if not self._drawer_service:
            self._drawer_service = LocationDrawerService(self.lunch_pad_client.token, self.location_id)
        return self._drawer_service

    @property
    def extra_charge_service(self) -> LocationExtraChargeService:
        """build extra charge service object to inquire about location extra charge

        :return: extra charge service object
        """
        assert self.lunch_pad_client.token, "User Token Not Set"
        if not self._extra_charge_service:
            self._extra_charge_service = LocationExtraChargeService(self.lunch_pad_client.token, self.location_id)
        return self._extra_charge_service

    @property
    def order_option_service(self) -> LocationOrderOptionService:
        """build order option service object to inquire about location order option

        :return:order option service object
        """
        assert self.lunch_pad_client.token, "User Token Not Set"
        if not self._order_option_service:
            self._order_option_service = LocationOrderOptionService(self.lunch_pad_client.token, self.location_id)
        return self._order_option_service
