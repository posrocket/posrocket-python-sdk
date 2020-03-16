"""Location Drawer Payment method Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
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

    def __init__(self, id=None, name=None, label=None, type=None, sales=None, refunds=None, **kwargs):
        """ map a dict to Location Drawer Payment method object

        :param kwargs: Location Drawer Payment method json dict
        """
        self.id = id
        self.name = name
        self.label = label
        self.type = type
        self.sales = sales
        self.refunds = refunds

    def __str__(self) -> str:
        """ String representation for the Location Drawer Payment method model

        :return: Directory Location Drawer Payment method type
        """
        return f'{self.type}'
