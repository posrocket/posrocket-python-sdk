"""Area Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class AreaModel:
    """ mapper class for Area object from Json Dict

    """
    id: str
    name: str

    def __init__(self,
                 id=None,
                 name=None
                 ):
        """ map a dict to Area object

        :param kwargs: Area json dict
        """
        self.id = id
        self.name = name

    def __str__(self) -> str:
        """ String representation for the Area model

        :return: Area name
        """
        return f'{self.name}'
