"""
Launchpad Location Client
"""
from posrocket.services import TabService
from posrocket.services.location.discount import LocationDiscountService
from posrocket.services.location.drawer import LocationDrawerService
from posrocket.services.location.extra_charge import LocationExtraChargeService
from posrocket.services.location.order_option import LocationOrderOptionService
from posrocket.services.location.sales import LocationSaleService

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
    _sale_service: LocationSaleService = None

    def __init__(self, location_id: str, launch_pad_client: 'posrocket.LaunchPadClient'):
        """create a location client to allow access to location related services

        :param location_id: POSRocket location id to get services for
        :param launch_pad_client: LaunchPadClient object to access tokens and auth related info
        """
        self.location_id = location_id
        self.launch_pad_client = launch_pad_client

    @property
    def tab_service(self) -> TabService:
        """build tab service object to inquire about location tabs

        :return: tab service object
        """
        assert self.launch_pad_client.token, "User Token Not Set"
        if not self._tab_service:
            self._tab_service = TabService(self.launch_pad_client.token, self.location_id)
        return self._tab_service

    @property
    def discount_service(self) -> LocationDiscountService:
        """build discount service object to inquire about location discounts

        :return: discount service object
        """
        assert self.launch_pad_client.token, "User Token Not Set"
        if not self._discount_service:
            self._discount_service = LocationDiscountService(self.launch_pad_client.token, self.location_id)
        return self._discount_service

    @property
    def drawer_service(self) -> LocationDrawerService:
        """build drawer service object to inquire about location drawers

        :return: drawer service object
        """
        assert self.launch_pad_client.token, "User Token Not Set"
        if not self._drawer_service:
            self._drawer_service = LocationDrawerService(self.launch_pad_client.token, self.location_id)
        return self._drawer_service

    @property
    def extra_charge_service(self) -> LocationExtraChargeService:
        """build extra charge service object to inquire about location extra charge

        :return: extra charge service object
        """
        assert self.launch_pad_client.token, "User Token Not Set"
        if not self._extra_charge_service:
            self._extra_charge_service = LocationExtraChargeService(self.launch_pad_client.token, self.location_id)
        return self._extra_charge_service

    @property
    def order_option_service(self) -> LocationOrderOptionService:
        """build order option service object to inquire about location order option

        :return:order option service object
        """
        assert self.launch_pad_client.token, "User Token Not Set"
        if not self._order_option_service:
            self._order_option_service = LocationOrderOptionService(self.launch_pad_client.token, self.location_id)
        return self._order_option_service

    @property
    def sale_service(self) -> LocationSaleService:
        """build country service object to inquire about countries

        :return: country service object
        """
        assert self.token, "User Token Not Set"
        if not self._sale_service:
            self._sale_service = LocationSaleService(self.token)
        return self._sale_service
