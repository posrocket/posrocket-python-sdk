"""Location Tab Item Variation Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabItemVariationModel:
    """ mapper class for Location Tab Item Variation object from Json Dict

    """
    id: str
    name: str
    type: str
    price: float

    def __init__(self,
                 id=None,
                 name=None,
                 type=None,
                 price=None,
                 **kwargs
                 ):
        """ map a dict to Location Tab Item Variation object

        :param kwargs: Location Tab Item Variation json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.price = price

    def __str__(self) -> str:
        """ String representation for the Location Tab Item Variation model

        :return: Directory Location Tab Item Variation name
        """
        return f'{self.name}'
