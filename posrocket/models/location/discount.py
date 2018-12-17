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

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Discount object

        :param kwargs: Location Discount json dict
        """
        self.id = None
        self.name = None
        self.type = None
        self.amount = None
        self.rate = None
        self.color = None
        self.pin_required = None
        self.after_tax = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Discount model

        :return: Location Discount name
        """
        return f'{self.name}'
