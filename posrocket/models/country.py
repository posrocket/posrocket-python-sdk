"""Country Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class CountryModel:
    """ mapper class for City object from Json Dict

    """
    country: str

    def __init__(self, **kwargs: dict):
        """ map a dict to Country object

        :param kwargs: Country json dict
        """

        self.country = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Country model

        :return: Country name
        """
        return f'{self.country}'
