from posrocket.models.catalog_modifier import CatalogModifierModel


class CatalogModifierListModel:
    id = None
    name = None
    type = None
    quantifiable = None
    order = None
    price = None
    _modifiers = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'

    @property
    def modifiers(self):
        return self._modifiers

    @modifiers.setter
    def modifiers(self, json_modifiers):
        self._modifiers = []
        for json_modifier in json_modifiers:
            self._modifiers.append(CatalogModifierModel(**json_modifier))
