"""Block Python model

"""
__author__ = "Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro"
__email__ = "r.amro@posrocket.com"
__status__ = "Beta"


class BlockModel:
    """ mapper class for Block object from Json Dict

    """
    id: str
    en: str
    ar: str

    def __init__(self,
                 id=None,
                 en=None,
                 ar=None,
                 **kwargs
                 ):
        """ map a dict to Block object

        :param kwargs: Block json dict
        """
        self.id = id
        self.en = en
        self.ar = ar

    def __str__(self) -> str:
        """ String representation for the Block model

        :return: Block name
        """
        return f'{self.en}'
