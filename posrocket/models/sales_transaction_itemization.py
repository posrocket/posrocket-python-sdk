from posrocket.models import SalesTransactionTaxModel, LocationInitialMoneyModel, CatalogCategoryModel, \
    CatalogVariationModel, SalesTransactionItemizationModifierModel


class SalesTransactionItemizationModel:
    id = None
    name = None
    quantity = None
    notes = None
    _total_money = None#
    _single_quantity_money = None
    _gross_sales_money = None
    _discount_money = None
    _net_sales_money = None
    _category = None
    _variation = None
    _taxes = None
    _modifiers = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'

    @property
    def taxes(self):
        return self._taxes

    @taxes.setter
    def taxes(self, tax_dict):
        self._taxes = SalesTransactionTaxModel(**tax_dict)

    @property
    def total_money(self):
        return self._total_money

    @total_money.setter
    def total_money(self, total_money_dict):
        self._total_money = LocationInitialMoneyModel(**total_money_dict)

    @property
    def single_quantity_money(self):
        return self._single_quantity_money

    @single_quantity_money.setter
    def single_quantity_money(self, single_quantity_money_dict):
        self._single_quantity_money = LocationInitialMoneyModel(**single_quantity_money_dict)

    @property
    def gross_sales_money(self):
        return self._gross_sales_money

    @gross_sales_money.setter
    def gross_sales_money(self, gross_sales_money_dict):
        self._gross_sales_money = LocationInitialMoneyModel(**gross_sales_money_dict)

    @property
    def discount_money(self):
        return self._discount_money

    @discount_money.setter
    def discount_money(self, discount_money_dict):
        self._discount_money = LocationInitialMoneyModel(**discount_money_dict)

    @property
    def net_sales_money(self):
        return self._net_sales_money

    @net_sales_money.setter
    def net_sales_money(self, net_sales_money_dict):
        self._net_sales_money = LocationInitialMoneyModel(**net_sales_money_dict)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category_dict):
        self._category = CatalogCategoryModel(**category_dict)

    @property
    def variation(self):
        return self._variation

    @variation.setter
    def variation(self, variation_dict):
        self._variation = CatalogVariationModel(**variation_dict)

    @property
    def modifiers(self):
        return self._modifiers

    @modifiers.setter
    def modifiers(self, modifiers_list):
        for modifier in modifiers_list:
            self._modifiers.append(SalesTransactionItemizationModifierModel(**modifier))
