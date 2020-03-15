"""Report Summary Python model

"""

import logging

__author__ = "Lujain Battiki, Rawan Amro"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Lujain Battiki, Rawan Amro"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Lujain Battiki, Rawan Amro"
__email__ = "Lanuchpad@posrocket.com"
__status__ = "Beta"

from posrocket.models.report import SummaryDetailsModel

LOGGER = logging.getLogger("posrocket")


class ReportSummaryModel:
    """mapper class for Report Summary object from Json Dict

    """
    _sales: SummaryDetailsModel
    _refunds: SummaryDetailsModel
    _net: SummaryDetailsModel

    def __init__(self,
                 sales=None,
                 refunds=None, net=None,
                 **kwargs):
        """map a dict to Report Summary object

        :param kwargs: Report Summary json dict
        """

        self.sales = sales
        self.refunds = refunds
        self.net = net

    def __str__(self) -> str:
        """ String representation for the Report Summary model

        :return: Report Summary name
        """
        return f'{self.sales}'

    @property
    def sales(self) -> SummaryDetailsModel:
        """
        getter for Report Summary sales
        :return: Report Summary sales object
        """
        return self._sales

    @sales.setter
    def sales(self, json_sales: dict):
        """setter for report summary sales

        :param json_sales: json dict for sales
        :return: None
        """
        if json_sales:
            self._sales = SummaryDetailsModel(**json_sales)
        else:
            self._sales = None

    @property
    def refunds(self) -> SummaryDetailsModel:
        """
        getter for Report Summary refunds
        :return: report summary refunds object
        """
        return self._refunds

    @refunds.setter
    def refunds(self, json_refunds: dict):
        """setter for report summary refunds

        :param json_refunds: json dict for refunds
        :return: None
        """
        if json_refunds:
            self._refunds = SummaryDetailsModel(**json_refunds)
        else:
            self._refunds = None

    @property
    def net(self) -> SummaryDetailsModel:
        """
        getter for Report Summary net
        :return: report summary net object
        """
        return self._net

    @net.setter
    def net(self, json_net: dict):
        """setter for report summary net

        :param json_net: json dict for net
        :return: None
        """
        if json_net:
            self._net = SummaryDetailsModel(**json_net)
        else:
            self._net = None
