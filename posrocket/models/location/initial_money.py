"""Location Initial Money Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationInitialMoneyModel:
    """ mapper class for Location Initial Money object from Json Dict

    """
    amount: float
    currency: str

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Initial Money object

        :param kwargs: Location Initial Money json dict
        """
        self.amount = None
        self.currency = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Initial Money model

        :return: Directory Location Initial Money name
        """
        return f'{self.amount}{self.currency}'
