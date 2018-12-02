"""Location Tab Item Python model

"""
from typing import List

from posrocket.models.catalog_modifier import CatalogModifierModel
from posrocket.models.catalog_variation import CatalogVariationModel
from posrocket.models.location_tab_item_discount import LocationTabItemDiscountModel
from posrocket.models.location_tab_item_modifier import LocationTabItemModifierModel
from posrocket.models.location_tab_item_variation import LocationTabItemVariationModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabItemModel:
    """ mapper class for Location Tab Item object from Json Dict

    """
    id: str
    name: str
    quantity: int
    notes: str
    _variation: LocationTabItemVariationModel
    _discounts: List[LocationTabItemDiscountModel]
    _modifiers: List[LocationTabItemModifierModel]

    def __init__(self, **kwargs):
        """ map a dict to Location Tab Item object

        :param kwargs: Location Tab json Item dict
        """
        self.id = None
        self.name = None
        self.quantity = None
        self.notes = None
        self._variation = None
        self._discounts = []
        self._modifiers = []
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Tab Item model

        :return: Directory Location Tab Item name
        """
        return f'{self.name}'

    @property
    def variation(self) -> LocationTabItemVariationModel:
        """getter for Tab item variation

        :return: Tab item variation object
        """
        return self._variation

    @variation.setter
    def variation(self, variation_dict: dict):
        """setter for Tab item variation

        :param variation_dict: json dict for Customer
        :return: None
        """
        self._variation = LocationTabItemVariationModel(**variation_dict)

    @property
    def discounts(self) -> List[LocationTabItemDiscountModel]:
        """getter for Tab item discounts

        :return: list of discounts for the Tab item
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts_list: list):
        """setter for Tab item discounts

        :param discounts_list:json list of discount dicts
        :return: None
        """
        self._discounts = []
        for discount in discounts_list:
            self._discounts.append(LocationTabItemDiscountModel(**discount))

    @property
    def modifiers(self) -> List[LocationTabItemModifierModel]:
        """getter for Tab item modifiers

        :return: list of modifiers for the Tab item
        """
        return self._modifiers

    @modifiers.setter
    def modifiers(self, modifiers_list: list):
        """setter for Tab item modifiers

        :param modifiers_list:json list of modifier dicts
        :return: None
        """
        self._modifiers = []
        for modifier in modifiers_list:
            self._modifiers.append(LocationTabItemModifierModel(**modifier))

    def add_variation(self, variation: CatalogVariationModel, location_id: str):
        self._variation = LocationTabItemVariationModel(id=variation.id, name=variation.name,
                                                        type=variation.pricing_type,
                                                        price=variation.get_price_for_location(location_id))

    def add_modifier(self, modifier: CatalogModifierModel, quantity: int, location_id: str, order: int):
        self._modifiers.append(LocationTabItemModifierModel(id=modifier.id, name=modifier.name, quantity=quantity,
                                                            price=modifier.get_price_for_location(location_id)))
