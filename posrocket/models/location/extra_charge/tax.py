"""Location Extra Charge Tax Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationExtraChargeTaxModel:
    """ mapper class for Location Extra Charge Tax object from Json Dict

    """
    id: str
    name: str
    inclusion_type: str
    rate: float

    def __init__(self,
                 id=None,
                 name=None,
                 inclusion_type=None,
                 rate=None,
                 **kwargs
                 ):
        """ map a dict to Location Extra Charge Tax object

        :param kwargs: Location Extra Charge Tax json dict
        """
        self.id = id
        self.name = name
        self.inclusion_type = inclusion_type
        self.rate = rate

    def __str__(self) -> str:
        """ String representation for the Location Extra Charge tax model

        :return: Directory Location Extra Charge tax name
        """
        return f'{self.name}'
