Catalog Service
================

The Catalog service allows access to the POSRocket catalog directory.

In order to access the Catalog service, a LaunchPad client must be created and to have a valid token.

Item Service
^^^^^^^^^^^^^^^
The following function allows to GET Item data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Item json data as a Python object of type `CatalogItemModel`_.

    - Each Service has 2 Getter functions which are:
        * Get item by ID:

        .. sourcecode:: python

            item = launch_pad.catalog_item_service.get_item_by_id(<item_id>)

        * Get all items:

        .. sourcecode:: python

            items = launch_pad.catalog_item_service.get_items()


    - For More information about `CatalogItemModel`_ specific functions, please check the models source code.

Category Service
^^^^^^^^^^^^^^^
The following function allows to GET Category data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Category json data as a Python object of type `CatalogCategoryModel`_.

    - Each Service has 2 Getter functions which are:
        * Get category by ID:

        .. sourcecode:: python

            category = launch_pad.catalog_category_service.get_category_by_id(<category_id>)

        * Get all categories:

        .. sourcecode:: python

            categories = launch_pad.catalog_category_service.get_categories()


Tag Service
^^^^^^^^^^^^^^^
The following function allows to GET Tag data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Tag json data as a Python object of type `CatalogTagModel`_.

    - Each Service has 2 Getter functions which are:
        * Get tag by ID:

        .. sourcecode:: python

            tag = launch_pad.catalog_tag_service.get_tag_by_id(<tag_id>)

        * Get all tags:

        .. sourcecode:: python

            tags = launch_pad.catalog_tag_service.get_tags()


Tax Service
^^^^^^^^^^^^^^^
The following function allows to GET Tax data:

    - Check the `Authentication`_ section for information regarding how to setup your LaunchPad object.

    - After the LaunchPad object has been setup you can access the getter functions, which return the
      Tax json data as a Python object of type `CatalogTaxModel`_.

    - Each Service has 2 Getter functions which are:
        * Get tax by ID:

        .. sourcecode:: python

            tax = launch_pad.catalog_tax_service.get_tax_by_id(<tax_id>)

        * Get all taxes:

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

        .. sourcecode:: python

            modifier_list = launch_pad.catalog_modifier_list_service.get_modifiers_list_by_id(<modifier_list_id>)

        * Get all taxes:

        .. sourcecode:: python

            modifier_lists = launch_pad.catalog_modifier_list_service.get_modifiers_lists()

.. _Authentication: authentication.html
.. _CatalogItemModel: ../posrocket.models.html#module-posrocket.models.catalog_item
.. _CatalogTaxModel: ../posrocket.models.html#module-posrocket.models.catalog_tax
.. _CatalogTagModel: ../posrocket.models.html#module-posrocket.models.catalog_tag
.. _CatalogCategoryModel: ../posrocket.models.html#module-posrocket.models.catalog_category
.. _CatalogModifierListModel: ../posrocket.models.html#module-posrocket.models.catalog_modifier_list


