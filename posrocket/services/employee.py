"""
Employee Service
"""
from posrocket.models.employee import EmployeeModel
from posrocket.utils.requests import Requests

__author__ = "Lujain Battikhi, Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Lujain Battikhi", "Rawan Amro"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Lujain Battikhi, Rawan Amro"
__email__ = "launchpad@posrocket.com"
__status__ = "Beta"


class EmployeeService(Requests):
    """Employee service class to allow retrieving data for employees
    """
    service_url = "/me/employees"
    model_cls = EmployeeModel

    def get_employees(self, **kwargs):
        return self.get_list(**kwargs)

    def get_employee_by_id(self, pk):
        return self.get_detail(pk)
