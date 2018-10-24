from posrocket.models import LocationTabItemVariationModel, LocationTabItemDiscountModel, LocationTabItemModifierModel


class LocationTabItemModel:
    id = None
    name = None
    quantity = None
    notes = None
    _variation = None
    _discounts = []
    _modifiers = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
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
