import hashlib
import hmac
import json
import logging

logger = logging.getLogger("django")


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
        hashing = hmac.new(bytes(self.pos_client.client_secret, "utf-8"),
                           bytes(json.dumps(payload), "utf-8"), hashlib.sha1)
        logger.info(hashing.hexdigest())
        logger.info(sig)
        return hashing.hexdigest() == sig

    def handle(self, payload, headers):
        assert self.verify_signature(payload, headers['HTTP_X_HOOK_SIGNATURE']), "invalid signature"
        return self.events[payload['event']](payload, headers) if self.events[payload['event']] else None
