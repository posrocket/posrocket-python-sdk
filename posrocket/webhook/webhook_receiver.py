"""
Webhook Reciever
"""
import hashlib
import hmac
import json
import logging

__author__ = "Ahmad Bazadough"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class WebhookReceiver:
    events = {}

    def __init__(self,
                 pos_client,
                 tab_create=None,
                 tab_update=None,
                 item_create=None,
                 item_update=None,
                 item_delete=None,
                 sale_create=None,
                 refund_create=None,
                 customer_create=None,
                 customer_update=None,
                 customer_delete=None,
                 ):
        """
        create web callback for the apps to deliver the data immediately when specific events occurs
            :param self:
            :param pos_client:  the event name that will trigger the callback when client data get modified
            :param tab_create= None:  the event name that will trigger the callback when a tab get created
            :param tab_update= None:  the event name that will trigger the callback when a tab get updated
            :param item_create= None:  the event name that will trigger the callback when an item get created
            :param item_update= None:  the event name that will trigger the callback when an item get updated
            :param item_delete= None:  the event name that will trigger the callback when an item get deleted
            :param sale_create= None:  the event name that will trigger the callback when a transaction get created
            :param refund_create= None:  the event name that will trigger the callback when a refund get created
            :param customer_create= None:  the event name that will trigger the callback when a customer get created
            :param customer_update= None:  the event name that will trigger the callback when a customer get updated
            :param customer_delete= None:  the event name that will trigger the callback when a customer get deleted
        """
        self.pos_client = pos_client
        self.events["tab.create"] = tab_create
        self.events["tab.update"] = tab_update
        self.events["item.create"] = item_create
        self.events["item.update"] = item_update
        self.events["item.delete"] = item_delete
        self.events["sale.create"] = sale_create
        self.events["refund.create"] = refund_create
        self.events["customer.create"] = customer_create
        self.events["customer.update"] = customer_update
        self.events["customer.delete"] = customer_delete

    def verify_signature(self, payload, sig):
        """
        verfiy if the client secret still truthful or not.
            :param self:
            :param payload: request data
            :param sig:  the request signiture

        Return true if the request signiture matched the pos client signiture
        """
        hashing = hmac.new(bytes(self.pos_client.client_secret, "utf-8"),
                           bytes(json.dumps(payload), "utf-8"), hashlib.sha1)
        return hashing.hexdigest() == sig

    def handle(self, payload, headers):
        """
        verify that the signiture is truthful then handle the web callback when a an event triggered
            :param self:
            :param payload:  request data
            :param headers:  request header

        Throw an error if the signiture is not truth and prevent the code execution from proceeding or
        Return the execution of the web callback if the app is subscribed to the triggred event
        """
        assert self.verify_signature(payload, headers['HTTP_X_HOOK_SIGNATURE']), "invalid signature"
        return self.events[payload['event']](payload, headers) if self.events[payload['event']] else None
