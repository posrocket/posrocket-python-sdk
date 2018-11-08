Location Service
================

A Location in POSRocket is one of the children of a `Business`_, in other words it is a branch of a Business.

The Location Service is a service created to access Location specific functions, which are listed below.

Service Functions
^^^^^^^^^^^^^^^^^
In order to access the Location Service, a LaunchPad client must be created and to have a valid token.

The following functions allow to GET location data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    -  After the LaunchPad object has been setup you can access the service and functions, you can save
       your Location Service it in a variable by calling it through your LaunchPad object instance or keep calling it
       through your LaunchPad object.

    .. sourcecode:: python

        location_client = launch_pad.location

    - There are 2 functions:
        * Get Locations (get_locations)

            .. sourcecode:: python

                result = location_client.get_locations()

        * Get Location by ID (get_location_by_id)

            .. sourcecode:: python

                result = location_client.get_location_by_id(<your_location_id>)
                    OR
                result = location_client(<your_location_id>)

    - For reference: `Location Service`_ source code

Location Client
^^^^^^^^^^^^^^^
    - There are 5 services that are accessed through LocationService:
        - `Tab Service`_
        - Discount Service
        - Drawer Service
        - Extra Charge Service
        - Order option Service

    .. sourcecode:: python

        launch_pad.location(<your_location_id>).tab_service
        launch_pad.location(<your_location_id>).discount_service
        launch_pad.location(<your_location_id>).drawer_service
        launch_pad.location(<your_location_id>).extra_charge_service
        launch_pad.location(<your_location_id>).order_option_service

    - Each Service has 2 Getter functions which are:
        * Get by ID:

        .. sourcecode:: python

            result = launch_pad.location(<your_location_id>).tab_service.get_tab_by_id(<tab_id>)

        * Get all objects:

        .. sourcecode:: python

            results = launch_pad.location(<your_location_id>).tab_service.get_tabs()

Tab Service
^^^^^^^^^^^

A Tab in POSRocket is Location specific and is used as an order representation in the system.

Create Tab
^^^^^^^^^^^^^
To create a `Tab`_ on the POSRocket system, a LaunchPad client must be created and to have a valid token.

The following function allows to Assign a pickup object to a Tab:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the TabService and functions, the service can be called
      through the following.

    .. sourcecode:: python

        launch_pad.location(<your_location_id>).tab_service

    - For assigning a pickup for a Tab Order, use the 'create' function which
      returns the created Tab json data as a Python object of type `Tab`_.

    .. sourcecode:: python

        result = launch_pad.location(<your_location_id>).tab_service.create(<your_tab_object_here>)


Assign Pickup
^^^^^^^^^^^^^
In order to assign a pickup for a `Tab`_, a LaunchPad client must be created and to have a valid token.

The following function allows to Assign a pickup object to a Tab:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the TabService and functions, the service can be called
      through the following.

    .. sourcecode:: python

        launch_pad.location(<your_location_id>).tab_service

    - For assigning a pickup for a Tab Order, use the 'assign_pickup' function which
      returns the updated Tab json data as a Python object of type `Tab`_ with the sent pickup object.

    .. sourcecode:: python

        result = launch_pad.location(<your_location_id>).tab_service.assign_pickup(<tab_id>, <your_pickup_object_here>)


    - The pickup object JSON example:
        * ETA:
            Estimated Time of Arrival to the Location for the pickup
        * Driver Name:
            Full name of the driver
        * Driver Number:
            The Drivers phone number

    .. sourcecode:: python

        pickup_object = {
            "eta": "DateTimeString",
            "driver_name": "Full Name",
            "driver_phone": "000000000"
        }

    - For reference: `Tab`_ Service source code

.. _Authentication: authentication.html
.. _Tab: ../posrocket.models.html#module-posrocket.models.location_tab
.. _Location Service: ../posrocket.models.html#posrocket.posrocket_client.LaunchPadClient.location_service
.. _Business: ../posrocket.models.html#module-posrocket.models.business
.. _Tab Service: #tab-service