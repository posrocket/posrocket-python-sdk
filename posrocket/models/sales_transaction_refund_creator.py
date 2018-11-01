"""Location Sales Transaction Refund Creator Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class SalesTransactionRefundCreatorModel:
    """ mapper class for Sales Transaction Refund Creator object from Json Dict

    """
    id: int = None
    name: str = None
    email: str = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Sales Transaction Refund Creator object

        :param kwargs: Sales Transaction Refund Creator json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Sales Transaction Refund Creator model

        :return: Directory Sales Transaction Refund Creator name
        """
        return f'{self.name}'
