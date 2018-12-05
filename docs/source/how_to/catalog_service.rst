Catalog Service
================

The Catalog service allows access to the POSRocket merchant catalog.

In order to access the Catalog service, a LaunchPad client must be created and to have a valid token.

.. note:: if you already have a valid token you can directly initiate a client like below:

    .. sourcecode:: python

        token = launch_pad.get_token(<full_return_url_with_query_params>,<your_redirect_url>,<token_dict>)

Item Service
^^^^^^^^^^^^
The following function allows to GET Item data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Item json data as a Python object of type `CatalogItemModel`_.

    - Each Service has 2 Getter functions which are:
        * Get item by ID:
            get a specific `CatalogItemModel`_. by id
        .. sourcecode:: python

            item = launch_pad.catalog_item_service.get_item_by_id(<item_id>)

        * Get all items:
            get all current business `CatalogItemModel`_. you can filter by category_id, tag_id,
            tax_id, name and you can also select the page by passing any of those variables to
            the get_items function.

        .. sourcecode:: python

            items = launch_pad.catalog_item_service.get_items()


    - Once you have the item object, you can use the built-in functions:
        * Get item variation by ID:
            If the variation is included in the items variations:
        .. sourcecode:: python

            variation = item.get_variation_by_id(<variation_id>)


        * Get item modifier by ID:
            If the modifier is included in the items list of modifiers:
        .. sourcecode:: python

            modifier = item.get_modifier_by_id(<modifier_id>)


    - For More information about `CatalogItemModel`_ specific functions, please check the models source code.

Category Service
^^^^^^^^^^^^^^^^
The following function allows to GET Category data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Category json data as a Python object of type `CatalogCategoryModel`_.

    - Each Service has 2 Getter functions which are:
        * Get category by ID:
            get a specific `CatalogCategoryModel`_. by id

        .. sourcecode:: python

            category = launch_pad.catalog_category_service.get_category_by_id(<category_id>)

        * Get all categories:
            get all current business `CatalogCategoryModel`_. you can select the page by passing the page variables to
            the get_categories function.

        .. sourcecode:: python

            categories = launch_pad.catalog_category_service.get_categories()


Tag Service
^^^^^^^^^^^
The following function allows to GET Tag data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Tag json data as a Python object of type `CatalogTagModel`_.

    - Each Service has 2 Getter functions which are:
        * Get tag by ID:
            get a specific `CatalogTagModel`_. by id

        .. sourcecode:: python

            tag = launch_pad.catalog_tag_service.get_tag_by_id(<tag_id>)

        * Get all tags:
            get all current business `CatalogTagModel`_. you can filter by name and you can also select the page by
            passing any of those variables to the get_tags function.

        .. sourcecode:: python

            tags = launch_pad.catalog_tag_service.get_tags()


Tax Service
^^^^^^^^^^^
The following function allows to GET Tax data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Tax json data as a Python object of type `CatalogTaxModel`_.

    - Each Service has 2 Getter functions which are:
        * Get tax by ID:
            get a specific `CatalogTaxModel`_. by id

        .. sourcecode:: python

            tax = launch_pad.catalog_tax_service.get_tax_by_id(<tax_id>)

        * Get all taxes:
            get all current business `CatalogTaxModel`_. you can filter by name and you can also select the page by
            passing any of those variables to the get_taxes function.

        .. sourcecode:: python

            taxes = launch_pad.catalog_tax_service.get_taxes()


Modifier Lists Service
^^^^^^^^^^^^^^^^^^^^^^
The following function allows to GET Tax data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Modifier List json data as a Python object of type `CatalogModifierListModel`_.

    - Each Service has 2 Getter functions which are:
        * Get tax by ID:
            get a specific `CatalogModifierListModel`_. by id

        .. sourcecode:: python

            modifier_list = launch_pad.catalog_modifier_list_service.get_modifiers_list_by_id(<modifier_list_id>)

        * Get all taxes:
            get all current business `CatalogModifierListModel`_. you can filter by name and you can also select the page by
            passing any of those variables to the get_modifiers_lists function.

        .. sourcecode:: python

            modifier_lists = launch_pad.catalog_modifier_list_service.get_modifiers_lists()

.. _Authentication: authentication.html
.. _CatalogItemModel: ../posrocket.models.html#module-posrocket.models.catalog_item
.. _CatalogTaxModel: ../posrocket.models.html#module-posrocket.models.catalog_tax
.. _CatalogTagModel: ../posrocket.models.html#module-posrocket.models.catalog_tag
.. _CatalogCategoryModel: ../posrocket.models.html#module-posrocket.models.catalog_category
.. _CatalogModifierListModel: ../posrocket.models.html#module-posrocket.models.catalog_modifier_list


