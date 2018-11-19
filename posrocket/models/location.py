"""Location Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
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

    def __init__(self, **kwargs: dict):
        """ map a dict to Location object

        :param kwargs: Location json dict
        """
        self.id = None
        self.name = None
        self.tax_number = None
        self.phone = None
        self.address = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location model

        :return: Location name
        """
        return f'{self.name}'
