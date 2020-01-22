"""Location Register Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationRegisterModel:
    """ mapper class for Location Register object from Json Dict

    """
    id: str
    name: str
    type: str
    reference: str
    amount: float
    rate: float
    serial: float
    sale_serial: float
    drawer_serial: float

    def __init__(self, id=None, name=None, type=None, reference=None, amount=None, rate=None, serial=None,
                 sale_serial=None,
                 drawer_serial=None, **kwargs):
        """ map a dict to Location Register object

        :param kwargs: Location Register json dict
        """

        self.id = id
        self.name = name
        self.type = type
        self.reference = reference
        self.amount = amount
        self.rate = rate
        self.serial = serial
        self.sale_serial = sale_serial,
        self.drawer_serial = drawer_serial,

    def __str__(self) -> str:
        """ String representation for the Location Register model

        :return: Directory Location Register name
        """
        return f'{self.name}'
