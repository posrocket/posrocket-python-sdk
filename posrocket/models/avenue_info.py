"""Avenue Info Python model

"""
__author__ = "Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro"
__email__ = "r.amro@posrocket.com"
__status__ = "Beta"


class AvenueInfoModel:
    """ mapper class for Avenue Info object from Json Dict

    """
    avenue_id = str
    name_en = str

    def __init__(self,
                 area_id=None,
                 name_en=None,
                 **kwargs
                 ):
        """ map a dict to Avenue Info object

        :param kwargs: Avenue Info json dict
        """
        self.area_id = area_id
        self.name_en = name_en

    def __str__(self) -> str:
        """ String representation for the Avenue Info model

        :return: Avenue name
        """
        return f'{self.name_en}'
