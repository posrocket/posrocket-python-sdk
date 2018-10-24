from posrocket.models import LocationDrawerCreatorModel, LocationDrawerPaymentMethodModel, LocationDrawerPaymentModel, \
    LocationInitialMoneyModel


class SalesTransactionModel:
    id = None
    receipt_id = None
    serial_number = None
    dining_option = None
    creation_time = None
    _discount_money = None
    _refunded_money = None
    _additive_tax_money = None
    _inclusive_tax_money = None
    _tax_money = None
    _tip_money = None
    _received_money = None
    _total_collected_money = None
    _extra_charges_money = None
    _creator = None
    _customer = None
    _tab = None
    _tenders = None
    _taxes = None
    _extra_charges = None
    _itemization = None
    _refunds = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.reference}'

    @property
    def initial_money(self):
        return self._initial_money

    @initial_money.setter
    def initial_money(self, json_initial_money):
        self._initial_money = LocationInitialMoneyModel(**json_initial_money)

    @property
    def card_sales_money(self):
        return self._card_sales_money

    @card_sales_money.setter
    def card_sales_money(self, json_card_sales_money):
        self._card_sales_money = LocationInitialMoneyModel(**json_card_sales_money)

    @property
    def card_refunds_money(self):
        return self._card_refunds_money

    @card_refunds_money.setter
    def card_refunds_money(self, json_card_refunds_money):
        self._card_refunds_money = LocationInitialMoneyModel(**json_card_refunds_money)

    @property
    def other_sales_money(self):
        return self._other_sales_money

    @other_sales_money.setter
    def other_sales_money(self, json_other_sales_money):
        self._other_sales_money = LocationInitialMoneyModel(**json_other_sales_money)

    @property
    def other_refunds_money(self):
        return self._other_refunds_money

    @other_refunds_money.setter
    def other_refunds_money(self, json_other_refunds_money):
        self._other_refunds_money = LocationInitialMoneyModel(**json_other_refunds_money)

    @property
    def sales_money(self):
        return self._sales_money

    @sales_money.setter
    def sales_money(self, json_sales_money):
        self._sales_money = LocationInitialMoneyModel(**json_sales_money)

    @property
    def refunds_money(self):
        return self._refunds_money

    @refunds_money.setter
    def refunds_money(self, json_refunds_money):
        self._refunds_money = LocationInitialMoneyModel(**json_refunds_money)

    @property
    def paid_in_out_money(self):
        return self._paid_in_out_money

    @paid_in_out_money.setter
    def paid_in_out_money(self, json_paid_in_out_money):
        self._paid_in_out_money = LocationInitialMoneyModel(**json_paid_in_out_money)

    @property
    def expected_money(self):
        return self._expected_money

    @expected_money.setter
    def expected_money(self, json_expected_money):
        self._expected_money = LocationInitialMoneyModel(**json_expected_money)

    @property
    def actual_money(self):
        return self._actual_money

    @actual_money.setter
    def actual_money(self, json_actual_money):
        self._actual_money = LocationInitialMoneyModel(**json_actual_money)

    @property
    def difference_money(self):
        return self._difference_money

    @difference_money.setter
    def difference_money(self, json_difference_money):
        self._difference_money = LocationInitialMoneyModel(**json_difference_money)

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, json_creator):
        self._creator = LocationDrawerCreatorModel(**json_creator)

    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, json_payments):
        self._payments = []
        for json_payment in json_payments:
            self._payments.append(LocationDrawerPaymentModel(**json_payment))

    @property
    def payment_methods(self):
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, json_payment_methods):
        self._payment_methods = []
        for json_payment_method in json_payment_methods:
            self._payment_methods.append(LocationDrawerPaymentMethodModel(**json_payment_method))
