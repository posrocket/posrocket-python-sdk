import hashlib
import hmac
import json


class WebhookReceiver:
    events = {}

    def __init__(self,
                 pos_client,
                 tab_create=lambda payload, headers: None,
                 tab_update=lambda payload, headers: None,
                 item_create=lambda payload, headers: None,
                 item_update=lambda payload, headers: None,
                 item_delete=lambda payload, headers: None,
                 sale_create=lambda payload, headers: None,
                 refund_create=lambda payload, headers: None,
                 customer_create=lambda payload, headers: None,
                 customer_update=lambda payload, headers: None,
                 customer_delete=lambda payload, headers: None,
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
        self.events["customer. update"] = customer_update
        self.events["customer. delete"] = customer_delete

    def verify_signature(self, payload, sig):
        hashing = hmac.new(self.pos_client.client_secret, json.dumps(payload), hashlib.sha1)
        return hashing == sig

    def handle(self, payload, headers):
        assert self.verify_signature(payload, headers['X-Hook-Signature']), "invalid signature"
        return self.events[headers['X-Hook-Event']](payload, headers)
