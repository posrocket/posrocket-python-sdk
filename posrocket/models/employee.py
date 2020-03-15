"""Employee Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class EmployeeModel:
    """mapper class for Employee object from Json Dict

    """

    id: str
    first_name: str
    last_name: str
    email: str
    is_deleted: str

    def __init__(self,
                 id=None,
                 first_name=None,
                 last_name=None,
                 email=None,
                 is_deleted=None,
                 **kwargs
                 ):
        """map a dict to Employee object

        :param kwargs: Employee json dict
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_deleted = is_deleted
