"""Location Python model

"""
from posrocket.models.position import PositionModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationModel:
    """ mapper class for Location object from Json Dict

    """
    id: str
    name: str
    tax_number: str
    phone: str
    address: str
    footer: str
    _position: PositionModel

    def __init__(self,
                 id=None,
                 name=None,
                 tax_number=None,
                 phone=None,
                 address=None,
                 footer=None,
                 position=None,
                 **kwargs
                 ):
        """ map a dict to Location object

        :param kwargs: Location json dict
        """
        self.id = id
        self.name = name
        self.tax_number = tax_number
        self.phone = phone
        self.address = address
        self.footer = footer
        self.position = position

    def __str__(self) -> str:
        """ String representation for the Location model

        :return: Location name
        """
        return f'{self.name}'

    @property
    def position(self) -> PositionModel:
        """
        getter for Location position
        :return: Location Position object
        """
        return self._position

    @position.setter
    def position(self, json_position: dict):
        """setter for Location position

        :param json_position: json dict for Location position
        :return: None
        """
        if json_position:
            self._position = PositionModel(**json_position)
        else:
            self._position = None
