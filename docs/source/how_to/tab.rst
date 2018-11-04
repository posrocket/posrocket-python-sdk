Tab Service
================

A Tab in POSRocket is Location specific and is used as an order representation in the system.

Assign Pickup
--------------------
In order to assign a pickup for a `Tab`_, a LaunchPad client must be created and to have a valid token.

The following function allows to Assign a pickup object to a Tab:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - Initialize your Tab Service by calling it through your LaunchPad object instance (Location must be initialized
      as well).

    .. sourcecode:: python

        pos_client.location_service.tab_service()

    - After it has been initialized you can access the services functions, and use 'assign_pickup' function which
      returns the updated tab json data as a Python object of type `Tab`_ with the sent pickup object.

    .. sourcecode:: python

        result = pos_client.location_service.tab_service.assign_pickup(<tab_id>, <your_pickup_object_here>)

    - For reference: `Tab`_ Service source code


.. _Authentication: authentication.html
.. _Tab: ../posrocket.models.html#module-posrocket.models.location_tab