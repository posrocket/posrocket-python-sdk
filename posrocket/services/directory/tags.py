"""
Directory Tags Service
"""
import logging

from posrocket.models.directory.tag import DirectoryTagModel
from posrocket.utils.requests import Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class DirectoryTagService(Requests):
    """Tags service class to allow retrieving customer related data
    """
    service_url = "/directory/tags"
    model_cls = DirectoryTagModel

    def get_tags(self, **kwargs):
        return self.get_list(**kwargs)

    def get_tag_by_id(self, pk):
        return self.get_detail(pk)
