"""Catalog Tax Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class CatalogTaxModel:
    """mapper class for Catalog Tax object from Json Dict

    """
    id: str
    name: str
    rate: float
    inclusion_type: str

    def __init__(self, id=None, name=None, rate=None, inclusion_type=None, **kwargs):
        """map a dict to Catalog Tax object

        :param kwargs: Catalog Tax json dict
        """
        self.id = id
        self.name = name
        self.rate = rate
        self.inclusion_type = inclusion_type

    def __str__(self) -> str:
        """ String representation for the Catalog Tax model

        :return: Catalog Tax name
        """
        return f'{self.name}'
