"""Avenue Python model

"""
__author__ = "Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro"
__email__ = "r.amro@posrocket.com"
__status__ = "Beta"


class AvenueModel:
    """ mapper class for Avenue object from Json Dict

    """
    id: str
    name: str

    def __init__(self,
                 id=None,
                 name=None,
                 **kwargs
                 ):
        """ map a dict to Avenue object

        :param kwargs: Avenue json dict
        """
        self.id = id
        self.name = name

    def __str__(self) -> str:
        """ String representation for the Avenue model

        :return: Avenue name
        """
        return f'{self.name}'
