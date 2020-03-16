"""Location Drawer Payment Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationDrawerPaymentModel:
    """ mapper class for Location Drawer Payment object from Json Dict

    """
    id: str
    type: str
    amount: float
    description: str
    time: str

    def __init__(self, id=None, type=None, amount=None, description=None, time=None, **kwargs):
        """ map a dict to Location Drawer Payment object

        :param kwargs: Location Drawer Payment json dict
        """
        self.id = id
        self.type = type
        self.amount = amount
        self.description = description
        self.time = time

    def __str__(self) -> str:
        """ String representation for the Location Drawer Payment model

        :return: Directory Location Drawer Payment type
        """
        return f'{self.type}'
