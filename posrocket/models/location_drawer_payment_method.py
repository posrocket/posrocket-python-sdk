"""Location Drawer Payment method Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationDrawerPaymentMethodModel:
    """ mapper class for Location Drawer Payment method object from Json Dict

    """
    id: str = None
    name: str = None
    label: str = None
    type: str = None
    sales: float = None
    refunds: float = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Drawer Payment method object

        :param kwargs: Location Drawer Payment method json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Drawer Payment method model

        :return: Directory Location Drawer Payment method type
        """
        return f'{self.type}'
