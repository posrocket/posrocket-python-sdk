"""Catalog Tag Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class CatalogTagModel:
    """mapper class for Catalog Tag object from Json Dict

    """
    id: str
    name: str

    def __init__(self, **kwargs):
        """map a dict to Catalog Tag object

        :param kwargs: Catalog Tag json dict
        """
        self.id = None
        self.name = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Catalog Tag model

        :return: Catalog Tag name
        """
        return f'{self.name}'
