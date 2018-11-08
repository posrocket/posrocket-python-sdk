Customer Service
================

The Customer service allows access to the POSRocket customer directory, the service allows creating a customer along
with getters.

In order to access the Business service, a LaunchPad client must be created and to have a valid token.

Basic Functions
^^^^^^^^^^^^^^^
The following function allows to GET Business data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Customer json data as a Python object of type `DirectoryCustomerModel`_.

    - Each Service has 2 Getter functions which are:
        * Get customer by ID:

        .. sourcecode:: python

            user = launch_pad.directory_customers_service.get_customer_by_id(<customer_id>)

        * Get all customers:

        .. sourcecode:: python

            users = launch_pad.directory_customers_service.get_customers()

    - You can also filter by name:

        .. sourcecode:: python

            users = launch_pad.directory_customers_service.filter_customers_by_name(name="<customer_name>")

Creating a new Customer
^^^^^^^^^^^^^^^^^^^^^^^
The following function allows to POST a new customer to the POSRocket Directory:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the 'create' function, which takes
      an object of type `DirectoryCustomerModel`_ as its parameter.

    - To create a Customer Object of type (DirectoryCustomerModel), 2 other objects must be created:
        * `DirectoryAddressModel`_: The Customers address information

        .. sourcecode:: python

            from posrocket.models import DirectoryAddressModel
            address = DirectoryAddressModel(label="<address_label>", residence="<residence_type>", is_primary=True,
                                            is_verified=True)

        * `DirectoryPhoneModel`_: The Customers phone information

        .. sourcecode:: python

            from posrocket.models import DirectoryAddressModel
            phone = DirectoryPhoneModel(number="<customer_phone_number>", is_primary=True, is_verified=True)


    - Now that we have the 2 objects ready, it is time to create the DirectoryCustomerModel:

        .. sourcecode:: python


            customer = DirectoryCustomerModel(first_name="<first_name>", last_name="<last_name>", gender="<gender>",
                                              country="<country_code>", addresses=[address], phone_numbers=[phone])

    - And finally pushing it to the POSRocket Directory:

        .. sourcecode:: python

            customer = launch_pad.directory_customers_service.create(customer)


.. _Authentication: authentication.html
.. _DirectoryCustomerModel: ../posrocket.models.html#module-posrocket.models.directory_customer
.. _DirectoryPhoneModel: ../posrocket.models.html#module-posrocket.models.directory_customer
.. _DirectoryAddressModel: ../posrocket.models.html#module-posrocket.models.directory_customer


