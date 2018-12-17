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
    id: str
    name: str
    label: str
    type: str
    sales: float
    refunds: float

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Drawer Payment method object

        :param kwargs: Location Drawer Payment method json dict
        """
        self.id = None
        self.name = None
        self.label = None
        self.type = None
        self.sales = None
        self.refunds = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Drawer Payment method model

        :return: Directory Location Drawer Payment method type
        """
        return f'{self.type}'
