Business Service
================

A Business in POSRocket is the parent, Locations are the children, there can be many Locations but only one Business for
them, it contains all the information regarding the business as a whole, not location specific, like Business industry
type / current status in the POSRocket System.


Business Information
--------------------
In order to access the Business service, a LaunchPad client must be created and to have a valid token.

The following function allows to GET Business data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - Initialize your Business Service by calling it through your LaunchPad object instance.

    .. sourcecode:: python

        pos_client.business_service()

    - After it has been initialized you can access the services functions, which returns the
      business json data as a Python object of type `Business`_.

    .. sourcecode:: python

        business = pos_client.business_service.get_business_info()

    - For reference: Business Service `Source Code`_

.. _Authentication: authentication.html
.. _Business: ../posrocket.models.html#module-posrocket.models.business
.. _Source Code: ../posrocket.services.html#module-posrocket.services.business

