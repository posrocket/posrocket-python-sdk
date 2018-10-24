from posrocket.models.area import AreaModel
from posrocket.models.city import CityModel


class DirectoryAddressModel:
    id = None
    label = None
    residence = None
    street = None
    building = None
    floor = None
    apartment = None
    extras = None
    is_primary = None
    _city = None
    _area = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.label}'

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, json_city):
        self._city = CityModel(**json_city)

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, json_area):
        self._area = AreaModel(**json_area)
