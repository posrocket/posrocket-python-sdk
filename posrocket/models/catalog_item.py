import logging
from uuid import UUID

from posrocket.models.catalog_category import CatalogCategoryModel
from posrocket.models.catalog_modifier_list import CatalogModifierListModel
from posrocket.models.catalog_tag import CatalogTagModel
from posrocket.models.catalog_tax import CatalogTaxModel
from posrocket.models.catalog_variation import CatalogVariationModel

logger = logging.getLogger("django")


class CatalogItemModel:
    id: UUID = None
    name: str = None
    color: str = None
    description: str = None
    image: str = None
    _category: CatalogCategoryModel = None
    _variations: list = []
    _modifier_lists: list = []
    _taxes: list = None
    _tags: list = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, json_category):
        self._category = CatalogCategoryModel(**json_category)

    @property
    def variations(self):
        return self._variations

    @variations.setter
    def variations(self, json_variations):
        self._variations = []
        for json_variation in json_variations:
            self._variations.append(CatalogVariationModel(**json_variation))

    @property
    def modifier_lists(self):
        return self._modifier_lists

    @modifier_lists.setter
    def modifier_lists(self, json_modifier_lists):
        self._modifier_lists = []
        for json_modifier_list in json_modifier_lists:
            self._modifier_lists.append(CatalogModifierListModel(**json_modifier_list))

    @property
    def modifier_lists(self):
        return self._modifier_lists

    @modifier_lists.setter
    def modifier_lists(self, json_modifier_lists):
        self._modifier_lists = []
        for json_modifier_list in json_modifier_lists:
            self._modifier_lists.append(CatalogModifierListModel(**json_modifier_list))

    @property
    def taxes(self):
        return self._taxes

    @taxes.setter
    def taxes(self, json_taxes):
        self._taxes = []
        for json_tax in json_taxes:
            self._taxes.append(CatalogTaxModel(**json_tax))

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, json_tags):
        self._tags = []
        for json_tag in json_tags:
            self._tags.append(CatalogTagModel(**json_tag))
