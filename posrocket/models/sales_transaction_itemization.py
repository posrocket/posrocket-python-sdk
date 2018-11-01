"""Location Sales Transaction Itemization Python model

"""
from typing import List
from posrocket.models.catalog_category import CatalogCategoryModel
from posrocket.models.catalog_variation import CatalogVariationModel
from posrocket.models.location_initial_money import LocationInitialMoneyModel
from posrocket.models.sales_transaction_itemization_modifier import SalesTransactionItemizationModifierModel
from posrocket.models.sales_transaction_tax import SalesTransactionTaxModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class SalesTransactionItemizationModel:
    """ mapper class for Sales Transaction Itemization object from Json Dict

    """
    id: int = None
    name: str = None
    quantity: int = None
    notes: str = None
    _total_money: LocationInitialMoneyModel = None
    _single_quantity_money: LocationInitialMoneyModel = None
    _gross_sales_money: LocationInitialMoneyModel = None
    _discount_money: LocationInitialMoneyModel = None
    _net_sales_money: LocationInitialMoneyModel = None
    _category: CatalogCategoryModel = None
    _variation: CatalogVariationModel = None
    _taxes: SalesTransactionTaxModel = None
    _modifiers: List[SalesTransactionItemizationModifierModel] = []

    def __init__(self, **kwargs: dict):
        """ map a dict to Sales Transaction Itemization object

        :param kwargs: Sales Transaction Itemization json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Sales Transaction Itemization model

        :return: Directory Sales Transaction Itemization name
        """
        return f'{self.name}'

    @property
    def taxes(self) -> SalesTransactionTaxModel:
        """
        getter for Sales Transaction Itemization Taxes
        :return: Sales Transaction Itemization Taxes object
        """
        return self._taxes

    @taxes.setter
    def taxes(self, tax_dict):
        """setter for Sales Transaction Itemization Discount Money

        :param tax_dict: json dict for discount money
        :return: None
        """
        self._taxes = SalesTransactionTaxModel(**tax_dict)

    @property
    def total_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Itemization Total Money
        :return: Sales Transaction Itemization Total Money object
        """
        return self._total_money

    @total_money.setter
    def total_money(self, total_money_dict: dict):
        """setter for Sales Transaction Itemization Total Money

        :param total_money_dict: json dict for total money
        :return: None
        """
        self._total_money = LocationInitialMoneyModel(**total_money_dict)

    @property
    def single_quantity_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Itemization Single Quantity Money
        :return: Sales Transaction Itemization Single Quantity Money object
        """
        return self._single_quantity_money

    @single_quantity_money.setter
    def single_quantity_money(self, single_quantity_money_dict: dict):
        """setter for Sales Transaction Itemization Single Quantity Money

        :param single_quantity_money_dict: json dict for discount money
        :return: None
        """
        self._single_quantity_money = LocationInitialMoneyModel(**single_quantity_money_dict)

    @property
    def gross_sales_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Itemization Gross Sales Money
        :return: Sales Transaction Itemization Gross Sales Money object
        """
        return self._gross_sales_money

    @gross_sales_money.setter
    def gross_sales_money(self, gross_sales_money_dict: dict):
        """setter for Sales Transaction Itemization Gross Sales Money

        :param gross_sales_money_dict: json dict for gross sales money
        :return: None
        """
        self._gross_sales_money = LocationInitialMoneyModel(**gross_sales_money_dict)

    @property
    def discount_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Itemization Discount Money
        :return: Sales Transaction Itemization Discount Money object
        """
        return self._discount_money

    @discount_money.setter
    def discount_money(self, discount_money_dict: dict):
        """setter for Sales Transaction Discount Money

        :param discount_money_dict: json dict for discount money
        :return: None
        """
        self._discount_money = LocationInitialMoneyModel(**discount_money_dict)

    @property
    def net_sales_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Itemization Net Sales Money
        :return: Sales Transaction Itemization Net Sales Money object
        """
        return self._net_sales_money

    @net_sales_money.setter
    def net_sales_money(self, net_sales_money_dict: dict):
        """setter for Sales Transaction Itemization Net Sales Money

        :param net_sales_money_dict: json dict for net sales money
        :return: None
        """
        self._net_sales_money = LocationInitialMoneyModel(**net_sales_money_dict)

    @property
    def category(self) -> CatalogCategoryModel:
        """
        getter for Sales Transaction Itemization Category
        :return: Sales Transaction Itemization Category object
        """
        return self._category

    @category.setter
    def category(self, category_dict: dict):
        """setter for Sales Transaction Itemization Category

        :param category_dict: json dict for category
        :return: None
        """
        self._category = CatalogCategoryModel(**category_dict)

    @property
    def variation(self) -> CatalogVariationModel:
        """
        getter for Sales Transaction Itemization Variation
        :return: Sales Transaction Itemization Variation object
        """
        return self._variation

    @variation.setter
    def variation(self, variation_dict: dict):
        """setter for Sales Transaction Itemization Variation

        :param variation_dict: json dict for variation
        :return: None
        """
        self._variation = CatalogVariationModel(**variation_dict)

    @property
    def modifiers(self) -> List[SalesTransactionItemizationModifierModel]:
        """
        getter for Sales Transaction Itemization Modifiers list
        :return: Sales Transaction Itemization Modifiers object
        """
        return self._modifiers

    @modifiers.setter
    def modifiers(self, modifiers_list: List[dict]):
        """setter for Sales Transaction Itemization Modifiers items

        :param modifiers_list: json list for modifiers dicts
        :return: None
        """
        for modifier in modifiers_list:
            self._modifiers.append(SalesTransactionItemizationModifierModel(**modifier))
