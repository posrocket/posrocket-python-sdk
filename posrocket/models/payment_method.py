"""Catalog Category Python model

"""

__author__ = "Lujain Battikhi"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Lujain Battikhi"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class PaymentMethodModel:
    """mapper class for Catalog Category object from Json Dict

    """
    id: str
    name: str
    label: str
    type: str
    icon: str

    def __init__(self, id=None, name=None, label=None, type=None, icon=None, **kwargs):
        """map a dict to Payment Method object

        :param kwargs: Payment Method json dict
        """
        self.id = id
        self.name = name
        self.label = label
        self.type = type
        self.icon = icon

    def __str__(self) -> str:
        """ String representation for the Payment Method model

        :return: Payment Method name
        """
        return f'{self.name}'
