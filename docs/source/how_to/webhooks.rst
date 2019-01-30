Webhooks
================

Webhooks allow you to build or set up Apps which subscribe to certain events on the launchpad. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.


Handle webhook
^^^^^^^^^^^^^^
In order to handle a webhook payload all you have to do is to pass a handler method to the hook_receiver method inside
the LaunchPadClient object, below you can find a more details steps:

    - Setup your LaunchPadClient, check the `Getting started`_ section for more details.
    - Write a Callable object (method) this method will receive the payload for the webhook and the headers for the hook
      request.
    - initiate the webhook handler by calling

        .. sourcecode:: python

            launchpad_client.hook_receiver(
                <request_body>,
                <request_headers>,
                tab_update=<tab update method handler>
                tab_create=<tab create method handler>
            )

.. _Getting started: ../getting_started.html

