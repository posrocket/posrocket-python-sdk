"""Catalog Category Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class CatalogCategoryModel:
    """mapper class for Catalog Category object from Json Dict

    """
    id: str
    name: str
    local_name: str

    def __init__(self, id=None, name=None, local_name=None, **kwargs):
        """map a dict to Catalog Category object

        :param kwargs: Catalog Category json dict
        """
        self.id = id
        self.name = name
        self.local_name = local_name

    def __str__(self) -> str:
        """ String representation for the Catalog Category model

        :return: Catalog Category name
        """
        return f'{self.name}'
