"""Location Tab Item Discount Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabItemDiscountModel:
    """ mapper class for Location Tab Item Discount object from Json Dict

    """
    id: str
    name: str
    type: str
    rate: float
    amount: float
    value: float

    def __init__(self,
                 id=None,
                 name=None,
                 type=None,
                 rate=None,
                 amount=None,
                 value=None
                 ):
        """ map a dict to Location Tab Item Discount object

        :param kwargs: Location Tab Item Discount json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.rate = rate
        self.amount = amount
        self.value = value

    def __str__(self) -> str:
        """ String representation for the Location Tab Item Discount model

        :return: Directory Location Tab Item Discount name
        """
        return f'{self.name}'
