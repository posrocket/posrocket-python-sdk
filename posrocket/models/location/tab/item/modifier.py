"""Location Tab Item Modifier Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabItemModifierModel:
    """ mapper class for Location Tab Item Modifier object from Json Dict

    """
    id: str
    name: str
    quantity: int
    price: float
    order: int

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Tab Item Modifier object

        :param kwargs: Location Tab Item Modifier json dict
        """
        self.id = None
        self.name = None
        self.quantity = None
        self.price = None
        self.order = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Tab Item Modifier model

        :return: Directory Location Tab Item Modifier name
        """
        return f'{self.name}'
