"""
Launchpad Location Client
"""
from posrocket.services.location.discount import LocationDiscountService
from posrocket.services.location.drawer import LocationDrawerService
from posrocket.services.location.extra_charge import LocationExtraChargeService
from posrocket.services.location.order_option import LocationOrderOptionService
from posrocket.services.location.register import LocationRegisterService
from posrocket.services.location.sales import LocationSaleService
from posrocket.services.location.summary_report import SummaryReportService
from posrocket.services.location.tabs import TabService
from posrocket.utils.assert_value import assert_value

__author__ = "Lujain Battikhi, Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Lujain Battikhi", "Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lujain Battikhi, Rawan Amro"
__email__ = "launchpad@posrocket.com"
__status__ = "Beta"


class LocationClient(object):
    """Location Client class to allow retrieving data for a specific location
    """

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
        assert_value(self.launch_pad_client.token)
        return TabService(self.launch_pad_client.token, self.location_id, prod=self.launch_pad_client.prod)

    @property
    def discount_service(self) -> LocationDiscountService:
        """build discount service object to inquire about location discounts

        :return: discount service object
        """
        assert_value(self.launch_pad_client.token)
        return LocationDiscountService(self.launch_pad_client.token, self.location_id, prod=self.launch_pad_client.prod)

    @property
    def drawer_service(self) -> LocationDrawerService:
        """build drawer service object to inquire about location drawers

        :return: drawer service object
        """
        assert_value(self.launch_pad_client.token)
        return LocationDrawerService(self.launch_pad_client.token, self.location_id, prod=self.launch_pad_client.prod)

    @property
    def extra_charge_service(self) -> LocationExtraChargeService:
        """build extra charge service object to inquire about location extra charge

        :return: extra charge service object
        """
        assert_value(self.launch_pad_client.token)
        return LocationExtraChargeService(self.launch_pad_client.token, self.location_id,
                                          prod=self.launch_pad_client.prod)

    @property
    def register_service(self) -> LocationRegisterService:
        """build register service object to inquire about location register

        :return: register service object
        """
        assert_value(self.launch_pad_client.token)
        return LocationRegisterService(self.launch_pad_client.token, self.location_id,
                                       prod=self.launch_pad_client.prod)

    @property
    def order_option_service(self) -> LocationOrderOptionService:
        """build order option service object to inquire about location order option

        :return:order option service object
        """
        assert_value(self.launch_pad_client.token)
        return LocationOrderOptionService(self.launch_pad_client.token, self.location_id,
                                          prod=self.launch_pad_client.prod)

    @property
    def sale_service(self) -> LocationSaleService:
        """build country service object to inquire about countries

        :return: country service object
        """
        assert_value(self.launch_pad_client.token)
        return LocationSaleService(self.launch_pad_client.token, self.location_id, prod=self.launch_pad_client.prod)

    @property
    def summary_report_service(self) -> SummaryReportService:
        """build summary report service object to inquire about report

        :return: summary report service object
        """
        assert_value(self.launch_pad_client.token)
        return SummaryReportService(self.launch_pad_client.token, self.location_id, prod=self.launch_pad_client.prod)
