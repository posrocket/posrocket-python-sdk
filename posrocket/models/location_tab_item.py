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
    id: str = None
    name: str = None
    quantity: int = None
    notes: str = None
    _variation: LocationTabItemVariationModel = None
    _discounts: List[LocationTabItemDiscountModel] = []
    _modifiers: List[LocationTabItemModifierModel] = []

    def __init__(self, **kwargs):
        """ map a dict to Location Tab Item object

        :param kwargs: Location Tab json Item dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Tab Item model

        :return: Directory Location Tab Item name
        """
        return f'{self.name}'

    @property
    def variation(self):
        return self._variation

    @variation.setter
    def variation(self, variation_dict):
        self._variation = LocationTabItemVariationModel(**variation_dict)

    @property
    def discounts(self):
        return self._discounts

    @discounts.setter
    def discounts(self, discounts_list):
        self._discounts = []
        for discount in discounts_list:
            self._discounts.append(LocationTabItemDiscountModel(**discount))

    @property
    def modifiers(self):
        return self._modifiers

    @modifiers.setter
    def modifiers(self, modifiers_list):
        self._modifiers = []
        for modifier in modifiers_list:
            self._modifiers.append(LocationTabItemModifierModel(**modifier))

    def add_variation(self, variation: CatalogVariationModel, location_id: str):
        self._variation = LocationTabItemVariationModel(id=variation.id, name=variation.name,
                                                        type=variation.pricing_type,
                                                        price=variation.get_price_for_location(location_id))

    def add_modifier(self, modifier: CatalogModifierModel, quantity: int, location_id: str):
        self._modifiers.append(LocationTabItemModifierModel(id=modifier.id, name=modifier.name, quantity=quantity,
                                                            price=modifier.get_price_for_location(location_id)))
