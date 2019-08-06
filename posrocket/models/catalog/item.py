"""Catalog Item Python model

"""

import logging
from typing import List

from posrocket.models.catalog.category import CatalogCategoryModel
from posrocket.models.catalog.modifier_list import CatalogModifierListModel
from posrocket.models.catalog.tag import CatalogTagModel
from posrocket.models.catalog.tax import CatalogTaxModel
from posrocket.models.catalog.variation import CatalogVariationModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

LOGGER = logging.getLogger("posrocket")


class CatalogItemModel:
    """mapper class for Catalog Item object from Json Dict

    """
    id: str
    name: str
    local_name: str
    color: str
    description: str
    local_description: str
    image: str
    _category: CatalogCategoryModel
    _variations: List[CatalogVariationModel]
    _modifier_lists: List[CatalogModifierListModel]
    _taxes: List[CatalogTaxModel]
    _tags: List[CatalogTagModel]

    def __init__(self,
                 id=None,
                 name=None,
                 local_name=None,
                 color=None,
                 description=None,
                 local_description=None,
                 image=None,
                 category=None,
                 variations=None,
                 modifier_lists=None,
                 taxes=None,
                 tags=None,
                 **kwargs):
        """map a dict to Catalog Item object

        :param kwargs: Catalog Item json dict
        """

        self.id = id
        self.name = name
        self.local_name = local_name
        self.color = color
        self.description = description
        self.local_description = local_description
        self.image = image['256'] if image and '256' in image else None
        self.category = category
        self.variations = variations
        self.modifier_lists = modifier_lists
        self.taxes = taxes
        self.tags = tags

    def __str__(self) -> str:
        """ String representation for the Catalog Item model

        :return: Catalog Item name
        """
        return f'{self.name}'

    @property
    def category(self) -> CatalogCategoryModel:
        """
        getter for Item category
        :return: item category object
        """
        return self._category

    @category.setter
    def category(self, json_category: dict):
        """setter for item category

        :param json_category: json dict for category
        :return: None
        """
        if json_category:
            self._category = CatalogCategoryModel(**json_category)
        else:
            self._category = None

    @property
    def variations(self) -> List[CatalogVariationModel]:
        """
        getter for Item variations
        :return: list of variations for the item
        """
        return self._variations

    @variations.setter
    def variations(self, json_variations: List[dict]):
        """setter for item variations

        :param json_variations: json list of variation dicts
        :return: None
        """
        self._variations = []
        for json_variation in json_variations or []:
            self._variations.append(CatalogVariationModel(**json_variation))

    @property
    def modifier_lists(self) -> List[CatalogModifierListModel]:
        """getter for Item modifiers lists

        :return: list of modifiers lists for the item
        """
        return self._modifier_lists

    @modifier_lists.setter
    def modifier_lists(self, json_modifier_lists: List[dict]):
        """setter for item modifiers lists

        :param json_modifier_lists: json list of modifiers list dicts
        :return: None
        """
        self._modifier_lists = []
        for json_modifier_list in json_modifier_lists or []:
            self._modifier_lists.append(CatalogModifierListModel(**json_modifier_list))

    @property
    def taxes(self) -> List[CatalogTaxModel]:
        """getter for Item taxes

        :return: list of taxes for the item
        """
        return self._taxes

    @taxes.setter
    def taxes(self, json_taxes: List[dict]):
        """setter for item taxes

        :param json_taxes:json list of tax dicts
        :return: None
        """
        self._taxes = []
        for json_tax in json_taxes or []:
            self._taxes.append(CatalogTaxModel(**json_tax))

    @property
    def tags(self) -> List[CatalogTagModel]:
        """getter for Item tags

        :return: list of tags for the item
        """
        return self._tags

    @tags.setter
    def tags(self, json_tags: List[dict]):
        """setter for item tags

        :param json_taxes:json list of tag dicts
        :return: None
        """
        self._tags = []
        for json_tag in json_tags or []:
            self._tags.append(CatalogTagModel(**json_tag))

    def get_variation_by_id(self, variation_id):
        """return the variation by a specific ID

        :param variation_id: variation id to get the variation if its in the variation list of the item
        :return: the variation if it exists
        """
        for variation in self.variations:
            if variation.id == variation_id:
                return variation
        return None

    def get_modifier_by_id(self, modifier_id):
        """return the modifier by a specific ID

        :param modifier_id: modifier id to get the modifier if its in the modifier list of the item
        :return: the modifier if it exists
        """
        for modifier_list in self.modifier_lists or []:
            for modifier in modifier_list.modifiers or []:
                if modifier.id == modifier_id:
                    return modifier
        return None
