"""Location Sales Transaction Refund Python model

"""
from typing import List
from posrocket.models.directory_customer import DirectoryCustomerModel
from posrocket.models.sales_transaction_extra_charges import SalesTransactionExtraChargeModel
from posrocket.models.sales_transaction_itemization import SalesTransactionItemizationModel
from posrocket.models.sales_transaction_refund_creator import SalesTransactionRefundCreatorModel
from posrocket.models.sales_transaction_tender import SalesTransactionTenderModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class SalesTransactionRefundModel:
    """ mapper class for Sales Transaction Refund object from Json Dict

    """
    id = None
    transaction_id = None
    type = None
    reason = None
    notes = None
    serial_number = None
    creation_time = None
    _customer: DirectoryCustomerModel = None
    _tender: SalesTransactionTenderModel = None
    _creator: SalesTransactionRefundCreatorModel = None
    _extra_charges: List[SalesTransactionExtraChargeModel] = None
    _itemization: List[SalesTransactionItemizationModel] = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Sales Transaction Refund object

        :param kwargs: Sales Transaction Refund json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Sales Transaction Refund model

        :return: Directory Sales Transaction Refund name
        """
        return f'{self.id}'

    @property
    def customer(self) -> DirectoryCustomerModel:
        """
        getter for Sales Transaction Refund Customer
        :return: Sales Transaction Refund Customer object
        """
        return self._customer

    @customer.setter
    def customer(self, customer_dict):
        """setter for Sales Transaction Refund Customer

        :param customer_dict: json dict for customer
        :return: None
        """
        self._customer = DirectoryCustomerModel(**customer_dict)

    @property
    def tender(self) -> SalesTransactionTenderModel:
        """
        getter for Sales Transaction Refund Tender
        :return: Sales Transaction Refund Tender object
        """
        return self._tender

    @tender.setter
    def tender(self, tender_dict: dict):
        """setter for Sales Transaction Refund Tender

        :param tender_dict: json dict for tender
        :return: None
        """
        self._tender = SalesTransactionTenderModel(**tender_dict)

    @property
    def creator(self) -> SalesTransactionRefundCreatorModel:
        """
        getter for Sales Transaction Refund Creator
        :return: Sales Transaction Refund Creator object
        """
        return self._creator

    @creator.setter
    def creator(self, creator_dict: dict):
        """setter for Sales Transaction Refund Creator

        :param creator_dict: json dict for creator
        :return: None
        """
        self._creator = SalesTransactionRefundCreatorModel(**creator_dict)

    @property
    def extra_charges(self) -> List[SalesTransactionExtraChargeModel]:
        """
        getter for Sales Transaction Refund Extra Charges items
        :return: json list of Sales Transaction Refund Extra Charges dicts
        """
        return self._extra_charges

    @extra_charges.setter
    def extra_charges(self, extra_charges_list: List[dict]):
        """setter for Sales Transaction Refund Extra Charges items

        :param extra_charges_list: json list for extra charges dicts
        :return: None
        """
        self._extra_charges = []
        for extra_charge in extra_charges_list:
            self._extra_charges.append(SalesTransactionExtraChargeModel(**extra_charge))

    @property
    def itemization(self) -> List[SalesTransactionItemizationModel]:
        """
        getter for Sales Transaction Refund Itemization items
        :return: json list of Sales Transaction Refund Itemization dicts
        """
        return self._itemization

    @itemization.setter
    def itemization(self, itemization_list: List[dict]):
        """setter for Sales Transaction Refund Itemization

        :param itemization_list: json list for itemization dicts
        :return: None
        """
        self._itemization = []
        for itemization in itemization_list:
            self._itemization.append(SalesTransactionItemizationModel(**itemization))
