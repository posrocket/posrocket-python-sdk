"""Location Drawer Payment Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationDrawerPaymentModel:
    """ mapper class for Location Drawer Payment object from Json Dict

    """
    id: str = None
    type: str = None
    amount: float = None
    description: str = None
    time: str = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Drawer Payment object

        :param kwargs: Location Drawer Payment json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Drawer Payment model

        :return: Directory Location Drawer Payment type
        """
        return f'{self.type}'
