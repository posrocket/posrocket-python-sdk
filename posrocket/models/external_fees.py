"""External Fees Python model

"""

__author__ = "Rawan Amro, Lujain Battikhi"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Rawan Amro, Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro, Lujain Battikhi"
__email__ = "Launchpad@posrocket.com"
__status__ = "Beta"


class ExternalFeesModel:
    """ mapper class for External Fees object from Json Dict

    """
    id: str
    name: str
    fees_type: str
    amount: float
    is_locked: bool
    is_disabled: bool
    rate: float
    tax: None

    def __init__(self,
                 id=None,
                 name=None,
                 fees_type=None,
                 amount=None,
                 rate=None,
                 is_locked=None,
                 is_disabled=None,
                 tax=None,
                 **kwargs
                 ):
        """ map a dict to  External Fees object

        :param kwargs: json External Fees dict
        """
        self.id = id
        self.name = name
        self.fees_type = fees_type
        self.amount = amount
        self.is_disabled = is_disabled
        self.is_locked = is_locked
        self.rate = rate
        self.tax = None

    def __str__(self) -> str:
        """ String representation for the  External Fees  model

        :return: Directory  External Fees name
        """
        return f'{self.name}'
