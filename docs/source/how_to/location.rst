Location Service
================

A Location in POSRocket is one of the children of a `Business`_, in other words it is a branch of a Business, each
location has its own set of services that can be accessed through this service.

In order to access the Location service, a LaunchPad client must be created and to have a valid token.

The following function allows to GET location data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - Initialize your Location Service by calling it through your LaunchPad object instance.

    .. sourcecode:: python

        pos_client.location_service()

    - There are 5 location services that can be accessed through the following:
        - Tab Service
        - Discount Service
        - Drawer Service
        - Extra Charge Service
        - Order option Service

    .. sourcecode:: python

        pos_client.location_service.tab_service()
        pos_client.location_service.discount_service()
        pos_client.location_service.drawer_service()
        pos_client.location_service.extra_charge_service()
        pos_client.location_service.order_option_service()

    - For reference: Location Service `Source Code`_

.. _Authentication: authentication.html
.. _Location: ../posrocket.models.html#module-posrocket.models.location
.. _Business: ../posrocket.models.html#module-posrocket.models.business
.. _Source Code: ../posrocket.services.location.html

