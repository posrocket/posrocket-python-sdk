"""Location Sales Transaction Python model

"""
import logging
from datetime import date
from typing import List

from posrocket.models import DirectoryCustomerModel, LocationInitialMoneyModel, LocationTabCreatorModel, \
    LocationTabModel
from .extra_charges import SalesTransactionExtraChargeModel
from .itemization.itemization import SalesTransactionItemizationModel
from .refund.refund import SalesTransactionRefundModel
from .tax import SalesTransactionTaxModel
from .tender import SalesTransactionTenderModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"
logger = logging.getLogger("django")

class SalesTransactionModel:
    """ mapper class for Sales Transaction object from Json Dict

    """
    id: str
    receipt_id: str
    serial_number: int
    dining_option: str
    creation_time: date
    _discount_money: LocationInitialMoneyModel
    _refunded_money: LocationInitialMoneyModel
    _additive_tax_money: LocationInitialMoneyModel
    _inclusive_tax_money: LocationInitialMoneyModel
    _tax_money: LocationInitialMoneyModel
    _tip_money: LocationInitialMoneyModel
    _received_money: LocationInitialMoneyModel
    _total_collected_money: LocationInitialMoneyModel
    _extra_charges_money: LocationInitialMoneyModel
    _creator: LocationTabCreatorModel
    _customer: DirectoryCustomerModel
    _tab: LocationTabModel
    _tenders: List[SalesTransactionTenderModel]
    _taxes: List[SalesTransactionTaxModel]
    _extra_charges: List[SalesTransactionExtraChargeModel]
    _itemization: List[SalesTransactionItemizationModel]
    _refunds: List[SalesTransactionRefundModel]

    def __init__(self,
                 id=None,
                 receipt_id=None,
                 serial_number=None,
                 dining_option=None,
                 creation_time=None,
                 discount_money=None,
                 refunded_money=None,
                 additive_tax_money=None,
                 inclusive_tax_money=None,
                 tax_money=None,
                 tip_money=None,
                 received_money=None,
                 total_collected_money=None,
                 extra_charges_money=None,
                 creator=None,
                 customer=None,
                 tab=None,
                 tenders=None,
                 taxes=None,
                 extra_charges=None,
                 itemization=None,
                 refunds=None,
                 **kwargs
                 ):
        """ map a dict to Sales Transaction object

        :param kwargs: Sales Transaction json dict
        """
        self.id = id
        self.receipt_id = receipt_id
        self.serial_number = serial_number
        self.dining_option = dining_option
        self.creation_time = creation_time
        self.discount_money = discount_money
        self.refunded_money = refunded_money
        self.additive_tax_money = additive_tax_money
        self.inclusive_tax_money = inclusive_tax_money
        self.tax_money = tax_money
        self.tip_money = tip_money
        self.received_money = received_money
        self.total_collected_money = total_collected_money
        self.extra_charges_money = extra_charges_money
        self.creator = creator
        self.customer = customer
        self.tab = tab
        self.tenders = tenders
        self.taxes = taxes
        self.extra_charges = extra_charges
        self.itemization = itemization
        self.refunds = refunds

    def __str__(self) -> str:
        """ String representation for the Sales Transaction model

        :return: Directory Sales Transaction name
        """
        return f'{self.id}'

    @property
    def discount_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Discount Money
        :return: Sales Transaction Discount Money object
        """
        return self._discount_money

    @discount_money.setter
    def discount_money(self, discount_money_dict: dict):
        """setter for Sales Transaction Discount Money

        :param discount_money_dict: json dict for discount money
        :return: None
        """
        if discount_money_dict:
            self._discount_money = LocationInitialMoneyModel(**discount_money_dict)
        else:
            self._discount_money = None

    @property
    def refunded_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Refunded Money
        :return: Sales Transaction Refunded Money object
        """
        return self._refunded_money

    @refunded_money.setter
    def refunded_money(self, refunded_money_dict: dict):
        """setter for Sales Transaction Refunded Money

        :param refunded_money_dict: json dict for refunded money
        :return: None
        """
        if refunded_money_dict:
            self._refunded_money = LocationInitialMoneyModel(**refunded_money_dict)
        else:
            self._refunded_money = None

    @property
    def additive_tax_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Additive Tax Money
        :return: Sales Transaction Additive Tax Money object
        """
        return self._additive_tax_money

    @additive_tax_money.setter
    def additive_tax_money(self, additive_tax_money_dict: dict):
        """setter for Sales Transaction Additive Tax Money

        :param additive_tax_money_dict: json dict for additive tax money
        :return: None
        """
        if additive_tax_money_dict:
            self._additive_tax_money = LocationInitialMoneyModel(**additive_tax_money_dict)
        else:
            self._additive_tax_money = None

    @property
    def inclusive_tax_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Inclusive Tax Money
        :return: Sales Transaction Inclusive Tax Money object
        """
        return self._inclusive_tax_money

    @inclusive_tax_money.setter
    def inclusive_tax_money(self, inclusive_tax_money_dict: dict):
        """setter for Sales Transaction Inclusive Tax Money

        :param inclusive_tax_money_dict: json dict for discount money
        :return: None
        """
        if inclusive_tax_money_dict:
            self._inclusive_tax_money = LocationInitialMoneyModel(**inclusive_tax_money_dict)
        else:
            self._inclusive_tax_money = None

    @property
    def tax_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Tax Money
        :return: Sales Transaction Tax Money object
        """
        return self._tax_money

    @tax_money.setter
    def tax_money(self, tax_money_dict: dict):
        """setter for Sales Transaction Tax Money

        :param tax_money_dict: json dict for tax money
        :return: None
        """
        if tax_money_dict:
            self._tax_money = LocationInitialMoneyModel(**tax_money_dict)
        else:
            self._tax_money = None

    @property
    def tip_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Tip Money
        :return: Sales Transaction Tip Money object
        """
        return self._tip_money

    @tip_money.setter
    def tip_money(self, tip_money_dict: dict):
        """setter for Sales Transaction Tip Money

        :param tip_money_dict: json dict for tip money
        :return: None
        """
        if tip_money_dict:
            self._tip_money = LocationInitialMoneyModel(**tip_money_dict)
        else:
            self._tip_money = None

    @property
    def received_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Received Money
        :return: Sales Transaction Received Money object
        """
        return self._received_money

    @received_money.setter
    def received_money(self, received_money_dict: dict):
        """setter for Sales Transaction Received Money

        :param received_money_dict: json dict for received money
        :return: None
        """
        if received_money_dict:
            self._received_money = LocationInitialMoneyModel(**received_money_dict)
        else:
            self._received_money = None

    @property
    def total_collected_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Total Collected Money
        :return: Sales Transaction Total Collected Money object
        """
        return self._total_collected_money

    @total_collected_money.setter
    def total_collected_money(self, total_collected_money_dict: dict):
        """setter for Sales Transaction Total Collected Money

        :param total_collected_money_dict: json dict for total collected money
        :return: None
        """
        if total_collected_money_dict:
            self._total_collected_money = LocationInitialMoneyModel(**total_collected_money_dict)
        else:
            self._total_collected_money = None

    @property
    def extra_charges_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Extra Charges Money
        :return: Sales Transaction Extra Charges Money object
        """
        return self._extra_charges_money

    @extra_charges_money.setter
    def extra_charges_money(self, extra_charges_money_dict: dict):
        """setter for Sales Transaction Extra Charges Money

        :param extra_charges_money_dict: json dict for extra charges money
        :return: None
        """
        if extra_charges_money_dict:
            self._extra_charges_money = LocationInitialMoneyModel(**extra_charges_money_dict)
        else:
            self._extra_charges_money = None

    @property
    def creator(self) -> LocationTabCreatorModel:
        """
        getter for Sales Transaction Creator
        :return: Sales Transaction Creator object
        """
        return self._creator

    @creator.setter
    def creator(self, creator_dict: dict):
        """setter for Sales Transaction Creator

        :param creator_dict: json dict for creator
        :return: None
        """
        if creator_dict:
            self._creator = LocationTabCreatorModel(**creator_dict)
        else:
            self._creator = None

    @property
    def customer(self) -> DirectoryCustomerModel:
        """
        getter for Sales Transaction Customer
        :return: Sales Transaction Customer object
        """
        return self._customer

    @customer.setter
    def customer(self, customer_dict: dict):
        """setter for Sales Transaction Customer

        :param customer_dict: json dict for customer
        :return: None
        """
        if customer_dict:
            self._customer = DirectoryCustomerModel(**customer_dict)
        else:
            self._customer = None

    @property
    def tab(self) -> LocationTabModel:
        """
        getter for Sales Transaction Tab
        :return: Sales Transaction Tab object
        """
        return self._tab

    @tab.setter
    def tab(self, tab_dict: dict):
        """setter for Sales Transaction Tab

        :param customer_dict: json dict for tab
        :return: None
        """
        if tab_dict:
            self._tab = LocationTabModel(**tab_dict)
        else:
            self._tab = None

    @property
    def tenders(self) -> List[SalesTransactionTenderModel]:
        """
        getter for Sales Transaction Tenders Object
        :return: Sales Transaction Tenders object
        """
        return self._tenders

    @tenders.setter
    def tenders(self, tenders_list: dict):
        """setter for Sales Transaction Tenders

        :param tenders_list: json list for tenders
        :return: None
        """
        self._tenders = []
        for tenders in tenders_list or []:
            self._tenders.append(SalesTransactionTenderModel(**tenders))

    @property
    def extra_charges(self) -> List[SalesTransactionExtraChargeModel]:
        """getter for Sales Transaction extra charges

        :return: list of items for the extra charges
        """
        return self._extra_charges

    @extra_charges.setter
    def extra_charges(self, extra_charges_list: List[dict]):
        """setter for Sales Transaction extra charges items

        :param extra_charges_list:json list of item dicts
        :return: None
        """
        self._extra_charges = []
        for extra_charge in extra_charges_list or []:
            logging.info('HAHAHHAHAHHAHA')
            logging.info(extra_charge)
            self._extra_charges.append(SalesTransactionExtraChargeModel(**extra_charge))

    @property
    def itemization(self) -> List[SalesTransactionItemizationModel]:
        """getter for Sales Transaction Itemization

        :return: list of items for the itemization
        """
        return self._itemization

    @itemization.setter
    def itemization(self, itemization_list: List[dict]):
        """setter for Sales Transaction Itemization items

        :param itemization_list:json list of itemization dicts
        :return: None
        """
        self._itemization = []
        for itemization in itemization_list or []:
            self._itemization.append(SalesTransactionItemizationModel(**itemization))

    @property
    def taxes(self) -> List[SalesTransactionTaxModel]:
        """getter for Sales Transaction Taxes items

        :return: list of items for the taxes
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes_list: List[dict]):
        """setter for Sales Transaction Taxes items

        :param taxes_list:json list of taxes dicts
        :return: None
        """
        self._taxes = []
        for tax in taxes_list or []:
            self._taxes.append(SalesTransactionTaxModel(**tax))

    @property
    def refunds(self) -> List[SalesTransactionRefundModel]:
        """getter for Sales Transaction Refunds items

        :return: list of items for the refunds items
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds_list: List[dict]):
        """setter for Sales Transaction Refunds items

        :param refunds_list:json list of refunds dicts
        :return: None
        """
        self._refunds = []
        for refund in refunds_list or []:
            self._refunds.append(SalesTransactionRefundModel(**refund))
