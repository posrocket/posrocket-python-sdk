"""Location Tab Creator Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabTemplateModel:
    """ mapper class for Location Tab Creator object from Json Dict

    """
    id: str
    name: str

    def __init__(self,
                 id=None,
                 name=None,
                 **kwargs
                 ):
        """ map a dict to Location Tab creator object

        :param kwargs: Location Tab json creator dict
        """
        self.id = id
        self.name = name

    def __str__(self) -> str:
        """ String representation for the Location Tab creator model

        :return: Location Tab creator name
        """
        return f'{self.name}'
