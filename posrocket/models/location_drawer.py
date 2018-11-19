"""Location Drawer Python model

"""
import datetime
from typing import List

from posrocket.models.location_drawer_creator import LocationDrawerCreatorModel
from posrocket.models.location_drawer_payment import LocationDrawerPaymentModel
from posrocket.models.location_drawer_payment_method import LocationDrawerPaymentMethodModel
from posrocket.models.location_initial_money import LocationInitialMoneyModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationDrawerModel:
    """ mapper class for Location Drawer object from Json Dict

    """
    id: str
    reference: str
    serial: str
    description: str
    start_time: datetime
    end_time: datetime
    _initial_money: LocationInitialMoneyModel
    _card_sales_money: LocationInitialMoneyModel
    _card_refunds_money: LocationInitialMoneyModel
    _other_sales_money: LocationInitialMoneyModel
    _other_refunds_money: LocationInitialMoneyModel
    _sales_money: LocationInitialMoneyModel
    _refunds_money: LocationInitialMoneyModel
    _paid_in_out_money: LocationInitialMoneyModel
    _expected_money: LocationInitialMoneyModel
    _actual_money: LocationInitialMoneyModel
    _difference_money: LocationInitialMoneyModel
    _creator: LocationDrawerCreatorModel
    _payments: List[LocationDrawerPaymentModel]
    _payment_methods: List[LocationDrawerPaymentMethodModel]

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Drawer object

        :param kwargs: Location Drawer json dict
        """
        self.id = None
        self.reference = None
        self.serial = None
        self.description = None
        self.start_time = None
        self.end_time = None
        self._initial_money = None
        self._card_sales_money = None
        self._card_refunds_money = None
        self._other_sales_money = None
        self._other_refunds_money = None
        self._sales_money = None
        self._refunds_money = None
        self._paid_in_out_money = None
        self._expected_money = None
        self._actual_money = None
        self._difference_money = None
        self._creator = None
        self._payments = None
        self._payment_methods = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Drawer model

        :return: Directory Location Drawer reference
        """
        return f'{self.reference}'

    @property
    def initial_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer Initial Money
        :return: Drawer Initial Money object
        """
        return self._initial_money

    @initial_money.setter
    def initial_money(self, json_initial_money: dict):
        """setter for Drawer Initial Money

        :param json_initial_money: json dict for Initial Money
        :return: None
        """
        self._initial_money = LocationInitialMoneyModel(**json_initial_money)

    @property
    def card_sales_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer card sales Money
        :return: Drawer card sales Money object
        """
        return self._card_sales_money

    @card_sales_money.setter
    def card_sales_money(self, json_card_sales_money: dict):
        """setter for Drawer card sales Money

        :param json_card_sales_money: json dict for  card sales Money
        :return: None
        """
        self._card_sales_money = LocationInitialMoneyModel(**json_card_sales_money)

    @property
    def card_refunds_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer card refunds Money
        :return: Drawer card refunds Money object
        """
        return self._card_refunds_money

    @card_refunds_money.setter
    def card_refunds_money(self, json_card_refunds_money: dict):
        """setter for Drawer card refunds Money

        :param json_card_refunds_money: json dict for  card refunds Money
        :return: None
        """
        self._card_refunds_money = LocationInitialMoneyModel(**json_card_refunds_money)

    @property
    def other_sales_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer other sales Money
        :return: Drawer other sales Money object
        """
        return self._other_sales_money

    @other_sales_money.setter
    def other_sales_money(self, json_other_sales_money: dict):
        """setter for Drawer other sales Money

        :param json_card_refunds_money: json dict for other sales Money
        :return: None
        """
        self._other_sales_money = LocationInitialMoneyModel(**json_other_sales_money)

    @property
    def other_refunds_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer other refunds Money
        :return: Drawer other refunds Money object
        """
        return self._other_refunds_money

    @other_refunds_money.setter
    def other_refunds_money(self, json_other_refunds_money: dict):
        """setter for Drawer other refunds Money

        :param json_other_refunds_money: json dict for other refunds Money
        :return: None
        """
        self._other_refunds_money = LocationInitialMoneyModel(**json_other_refunds_money)

    @property
    def sales_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer sales Money
        :return: Drawer sales Money object
        """
        return self._sales_money

    @sales_money.setter
    def sales_money(self, json_sales_money: dict):
        """setter for Drawer sales Money

        :param json_sales_money: json dict for sales Money
        :return: None
        """
        self._sales_money = LocationInitialMoneyModel(**json_sales_money)

    @property
    def refunds_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer refunds Money
        :return: Drawer refunds Money object
        """
        return self._refunds_money

    @refunds_money.setter
    def refunds_money(self, json_refunds_money: dict):
        """setter for Drawer refunds Money

        :param json_refunds_money: json dict for refunds Money
        :return: None
        """
        self._refunds_money = LocationInitialMoneyModel(**json_refunds_money)

    @property
    def paid_in_out_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer paid in out Money
        :return: Drawer paid in out Money object
        """
        return self._paid_in_out_money

    @paid_in_out_money.setter
    def paid_in_out_money(self, json_paid_in_out_money: dict):
        """setter for Drawer paid in out Money

        :param json_paid_in_out_money: json dict for paid in out Money
        :return: None
        """
        self._paid_in_out_money = LocationInitialMoneyModel(**json_paid_in_out_money)

    @property
    def expected_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer expected Money
        :return: Drawer expected Money object
        """
        return self._expected_money

    @expected_money.setter
    def expected_money(self, json_expected_money: dict):
        """setter for Drawer expected Money

        :param json_expected_money: json dict for expected Money
        :return: None
        """
        self._expected_money = LocationInitialMoneyModel(**json_expected_money)

    @property
    def actual_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer actual Money
        :return: Drawer actual Money object
        """
        return self._actual_money

    @actual_money.setter
    def actual_money(self, json_actual_money: dict):
        """setter for Drawer actual Money

        :param json_actual_money: json dict for actual Money
        :return: None
        """
        self._actual_money = LocationInitialMoneyModel(**json_actual_money)

    @property
    def difference_money(self) -> LocationInitialMoneyModel:
        """
        getter for Drawer difference Money
        :return: Drawer difference Money object
        """
        return self._difference_money

    @difference_money.setter
    def difference_money(self, json_difference_money: dict):
        """setter for Drawer difference Money

        :param json_difference_money: json dict for difference Money
        :return: None
        """
        self._difference_money = LocationInitialMoneyModel(**json_difference_money)

    @property
    def creator(self) -> LocationDrawerCreatorModel:
        """
        getter for Drawer creator
        :return: Drawer creator object
        """
        return self._creator

    @creator.setter
    def creator(self, json_creator: dict):
        """setter for Drawer creator

        :param json_creator: json dict for creator
        :return: None
        """
        self._creator = LocationDrawerCreatorModel(**json_creator)

    @property
    def payments(self) -> List[LocationDrawerPaymentModel]:
        """getter for Drawer payments

        :return: list of payments for the Drawer
        """
        return self._payments

    @payments.setter
    def payments(self, json_payments: List[dict]):
        """setter for Drawer payments

        :param json_payments:json list of payment dicts
        :return: None
        """
        self._payments = []
        for json_payment in json_payments:
            self._payments.append(LocationDrawerPaymentModel(**json_payment))

    @property
    def payment_methods(self) -> List[LocationDrawerPaymentMethodModel]:
        """getter for Drawer payment methods

        :return: list of payment methods for the Drawer
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, json_payment_methods: List[dict]):
        """setter for Drawer payment methods

        :param json_payment_methods:json list of payment method dicts
        :return: None
        """
        self._payment_methods = []
        for json_payment_method in json_payment_methods:
            self._payment_methods.append(LocationDrawerPaymentMethodModel(**json_payment_method))
