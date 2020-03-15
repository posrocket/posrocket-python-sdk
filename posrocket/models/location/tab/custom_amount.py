"""Location Tab Item Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabCustomAmountModel:
    """ mapper class for Location Tab Item object from Json Dict

    """
    name: str
    price: int

    def __init__(self,
                 name=None,
                 price=None,
                 **kwargs
                 ):
        """ map a dict to Location Tab Item object

        :param kwargs: Location Tab json Item dict
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """ String representation for the Location Tab Item model

        :return: Directory Location Tab Item name
        """
        return f'{self.name}'
