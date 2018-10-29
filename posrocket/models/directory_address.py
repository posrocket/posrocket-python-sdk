"""Directory Address Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

from posrocket.models.area import AreaModel
from posrocket.models.city import CityModel


class DirectoryAddressModel:
    """ mapper class for Directory Address object from Json Dict

    """
    id: str = None
    label: str = None
    residence: str = None
    street: str = None
    building: str = None
    floor: str = None
    apartment: str = None
    extras: str = None
    is_primary: bool = None
    _city: CityModel = None
    _area: AreaModel = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Directory Address object

        :param kwargs: Directory Address json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Directory Address model

        :return: Directory Address label
        """
        return f'{self.label}'

    @property
    def city(self) -> CityModel:
        """
        getter for Address City
        :return: Address City object
        """
        return self._city

    @city.setter
    def city(self, json_city: dict):
        """setter for Address City

        :param json_city: json dict for City
        :return: None
        """
        self._city = CityModel(**json_city)

    @property
    def area(self) -> AreaModel:
        """
        getter for Address Area
        :return: Address Area object
        """
        return self._area

    @area.setter
    def area(self, json_area: dict):
        """setter for Address Area

        :param json_city: json dict for Area
        :return: None
        """
        self._area = AreaModel(**json_area)
