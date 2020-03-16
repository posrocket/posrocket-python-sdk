"""Location Tab Template Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabTemplateModel:
    """ mapper class for Location Tab Template object from Json Dict

    """
    id: str
    name: str
    category_id: str

    def __init__(self,
                 id=None,
                 name=None,
                 category_id=None,
                 **kwargs
                 ):
        """ map a dict to Location Tab template object

        :param kwargs: Location Tab json template dict
        """
        self.id = id
        self.name = name
        self.category_id = category_id

    def __str__(self) -> str:
        """ String representation for the Location Tab template model

        :return: Location Tab template name
        """
        return f'{self.name}'
