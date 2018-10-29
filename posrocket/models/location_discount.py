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
    id = None
    name = None
    type = None
    amount = None
    rate = None
    color = None
    pin_required = None
    after_tax = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Discount object

        :param kwargs: Location Discount json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Discount model

        :return: Location Discount name
        """
        return f'{self.name}'
