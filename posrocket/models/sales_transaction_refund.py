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
    id: str
    transaction_id: str
    type: str
    reason: str
    notes: str
    serial_number: str
    creation_time: str
    _customer: DirectoryCustomerModel
    _tender: SalesTransactionTenderModel
    _creator: SalesTransactionRefundCreatorModel
    _extra_charges: List[SalesTransactionExtraChargeModel]
    _itemization: List[SalesTransactionItemizationModel]

    def __init__(self, **kwargs: dict):
        """ map a dict to Sales Transaction Refund object

        :param kwargs: Sales Transaction Refund json dict
        """
        self.id = None
        self.transaction_id = None
        self.type = None
        self.reason = None
        self.notes = None
        self.serial_number = None
        self.creation_time = None
        self._customer = None
        self._tender = None
        self._creator = None
        self._extra_charges = None
        self._itemization = None

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
        if customer_dict:
            self._customer = DirectoryCustomerModel(**customer_dict)
        else:
            self._customer = None

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
        if tender_dict:
            self._tender = SalesTransactionTenderModel(**tender_dict)
        else:
            self._tender = None

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
        if creator_dict:
            self._creator = SalesTransactionRefundCreatorModel(**creator_dict)
        else:
            self._creator = None

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
