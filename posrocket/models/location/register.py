"""Location Register Python model

"""
__author__ = "Lujain Battiki, Rawan Amro"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Lujain Battiki, Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lujain Battiki, Rawan Amro"
__email__ = "Lanuchpad@posrocket.com"
__status__ = "Beta"

class LocationRegisterModel:
    """ mapper class for Location Register object from Json Dict

    """
    id: str
    name: str
    type: str
    reference: str
    serial: float
    is_master: bool
    sale_serial: float
    drawer_serial: float

    def __init__(self, id=None, name=None, is_master=None, type=None, reference=None, serial=None,
                 sale_serial=None,
                 drawer_serial=None, **kwargs):
        """ map a dict to Location Register object

        :param kwargs: Location Register json dict
        """

        self.id = id
        self.name = name
        self.type = type
        self.reference = reference
        self.serial = serial
        self.is_master = is_master
        self.sale_serial = sale_serial,
        self.drawer_serial = drawer_serial,

    def __str__(self) -> str:
        """ String representation for the Location Register model

        :return: Directory Location Register name
        """
        return f'{self.name}-{self.is_master}'
