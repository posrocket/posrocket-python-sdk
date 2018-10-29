"""Catalog Modifier list Python model

"""
from typing import List

from posrocket.models.catalog_modifier import CatalogModifierModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class CatalogModifierListModel:
    """mapper class for Catalog Modifier list object from Json Dict

    """
    id: str = None
    name: str = None
    type: str = None
    quantifiable: bool = None
    order: int = None
    price: float = None
    _modifiers: List[CatalogModifierModel] = []

    def __init__(self, **kwargs):
        """map a dict to Catalog Modifier list object

        :param kwargs: Catalog Modifier list json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Catalog Modifier list model

        :return: Catalog Item name
        """
        return f'{self.name}'

    @property
    def modifiers(self) -> List[CatalogModifierModel]:
        """getter for Modifier list Modifiers

        :return: list of Modifiers for the Modifier list
        """
        return self._modifiers

    @modifiers.setter
    def modifiers(self, json_modifiers: List[dict]):
        """setter for Modifier list Modifiers

        :param json_taxes:json list of Modifier dicts
        :return: None
        """
        self._modifiers = []
        for json_modifier in json_modifiers:
            self._modifiers.append(CatalogModifierModel(**json_modifier))
