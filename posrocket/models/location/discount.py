"""Location Discount Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationDiscountModel:
    """ mapper class for Location Discount object from Json Dict

    """
    id: str
    name: str
    type: str
    amount: float
    rate: float
    color: str
    pin_required: bool
    after_tax: bool

    def __init__(self,
                 id=None,
                 name=None,
                 type=None,
                 amount=None,
                 rate=None,
                 color=None,
                 pin_required=None,
                 after_tax=None,
                 **kwargs
                 ):
        """ map a dict to Location Discount object

        :param kwargs: Location Discount json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.amount = amount
        self.rate = rate
        self.color = color
        self.pin_required = pin_required
        self.after_tax = after_tax

    def __str__(self) -> str:
        """ String representation for the Location Discount model

        :return: Location Discount name
        """
        return f'{self.name}'
