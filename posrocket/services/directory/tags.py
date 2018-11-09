"""
Directory Tags Service
"""
import logging

from posrocket.models.directory_tag import DirectoryTagModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("django")


class DirectoryTagService(Requests):
    """Tags service class to allow retrieving customer related data
    """
    service_url = "/directory/tags"
    model_cls = DirectoryTagModel
    get_tags = BaseServiceFactory.make_list_items_response()
    get_tag_by_id = BaseServiceFactory.make_detail_item_response()
