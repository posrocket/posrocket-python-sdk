from posrocket.models import LocationInitialMoneyModel, LocationTabCreatorModel, DirectoryCustomerModel, \
    LocationTabModel, SalesTransactionTenderModel, SalesTransactionTaxModel, SalesTransactionItemizationModel


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
        return f'{self.id}'

    @property
    def discount_money(self):
        return self._discount_money

    @discount_money.setter
    def discount_money(self, discount_money_dict):
        self._discount_money = LocationInitialMoneyModel(**discount_money_dict)

    @property
    def refunded_money(self):
        return self._refunded_money

    @refunded_money.setter
    def refunded_money(self, refunded_money_dict):
        self._refunded_money = LocationInitialMoneyModel(**refunded_money_dict)

    @property
    def additive_tax_money(self):
        return self._additive_tax_money

    @additive_tax_money.setter
    def additive_tax_money(self, additive_tax_money_dict):
        self._additive_tax_money = LocationInitialMoneyModel(**additive_tax_money_dict)

    @property
    def inclusive_tax_money(self):
        return self._inclusive_tax_money

    @inclusive_tax_money.setter
    def inclusive_tax_money(self, inclusive_tax_money_dict):
        self._inclusive_tax_money = LocationInitialMoneyModel(**inclusive_tax_money_dict)

    @property
    def tax_money(self):
        return self._tax_money

    @tax_money.setter
    def tax_money(self, tax_money_dict):
        self._tax_money = LocationInitialMoneyModel(**tax_money_dict)

    @property
    def tip_money(self):
        return self._tip_money

    @tip_money.setter
    def tip_money(self, tip_money_dict):
        self._tip_money = LocationInitialMoneyModel(**tip_money_dict)

    @property
    def received_money(self):
        return self._received_money

    @received_money.setter
    def received_money(self, received_money_dict):
        self._received_money = LocationInitialMoneyModel(**received_money_dict)

    @property
    def total_collected_money(self):
        return self._total_collected_money

    @total_collected_money.setter
    def total_collected_money(self, total_collected_money_dict):
        self._total_collected_money = LocationInitialMoneyModel(**total_collected_money_dict)

    @property
    def extra_charges_money(self):
        return self._extra_charges_money

    @extra_charges_money.setter
    def extra_charges_money(self, extra_charges_money_dict):
        self._extra_charges_money = LocationInitialMoneyModel(**extra_charges_money_dict)

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, creator_dict):
        self._creator = LocationTabCreatorModel(**creator_dict)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer_dict):
        self._customer = DirectoryCustomerModel(**customer_dict)

    @property
    def tab(self):
        return self._tab

    @tab.setter
    def tab(self, customer_dict):
        self._tab = LocationTabModel(**customer_dict)

    @property
    def tenders(self):
        return self._tenders

    @tenders.setter
    def tenders(self, tenders_dict):
        self._tenders = SalesTransactionTenderModel(**tenders_dict)

    @property
    def extra_charges(self):
        return self._extra_charges

    @extra_charges.setter
    def extra_charges(self, extra_charges_list):
        self._extra_charges = []
        for extra_charge in extra_charges_list:
            self._extra_charges.append(SalesTransactionTenderModel(**extra_charge))

    @property
    def itemization(self):
        return self._itemization

    @itemization.setter
    def itemization(self, itemization_list):
        self._itemization = []
        for itemization in itemization_list:
            self._itemization.append(SalesTransactionItemizationModel(**itemization))

    @property
    def taxes(self):
        return self._taxes

    @taxes.setter
    def taxes(self, taxes_list):
        self._taxes = []
        for tax in taxes_list:
            self._taxes.append(SalesTransactionTaxModel(**tax))

    @property
    def refunds(self):
        return self._refunds

    @refunds.setter
    def refunds(self, refunds_list):
        self._refunds = []
        for refund in refunds_list:
            self._refunds.append(SalesTransactionTaxModel(**refund))

