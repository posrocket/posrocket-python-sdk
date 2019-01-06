"""Directory Tag Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class DirectoryTagModel:
    """ mapper class for Directory Tag object from Json Dict

    """
    id: str
    name: str

    def __init__(self, id=None, name=None, **kwargs):
        """ map a dict to Directory Tags object

        :param kwargs: Directory Tags json dict
        """
        self.id = id
        self.name = name

    def __str__(self) -> str:
        """ String representation for the Directory Tag model

        :return: Directory Tag name
        """
        return f'{self.name}'
