Authentication Service
==============================
In this part we will talk in-depth about the OAuth2 flow we use in our platform.

In order to start working on the LaunchPad and connect with our APIs,
you need an account on `LaunchPad`_ and an App connected to that account for the Authentication flow (OAuth2).

The OAuth flow through our SDK requires the following credentials:

* Client ID:
    LaunchPad Oauth Client ID
* Client Secret:
    LaunchPad OAuth Client Secret
* Redirect URL:
    Redirect URL you registered as callback in the LaunchPad app settings
* Authorization Response URL:
    Authorization response URL, the callback URL of the request back to you

OAuth2 Process
----------------------

Please check the following example on how to use the SDKs LaunchPad client class to authenticate:
    - Import the posrocket LaunchPad client in your python script:

    .. sourcecode:: python

        from posrocket import LaunchPadClient


    - Create a LaunchPad object:

    .. sourcecode:: python

        launch_pad = LaunchPadClient(<your_oauth_client_id>,<your_oauth_client_secret>)

    - Generate authorization url:

    .. sourcecode:: python

        auth_url = launch_pad.get_authorization_url(<your_redirect_url>)

    - After the user authorizes the app on LaunchPad we will redirect him back to the return url (Redirect URL) to catch the code from your side.


    - Retrieve the access_token from the return url by using the following function:

    .. sourcecode:: python

        token = launch_pad.get_token(<full_return_url_with_query_params>,<your_redirect_url>)

    .. important::
        The function also saves the token as an attribute in the object instance (LaunchPad Client) to be used,
        no need to keep using the function to get the token

Refresh Expired Token
----------------------
In the case of token expiration:
    - Use the following function to refresh your token, using the expired token:

    .. sourcecode:: python

        new_token = launch_pad.refresh_token(<your_expired_token>)

    .. warning::
        The token expires after 10 hours of being generated


This covers the authentication process, you will be using the LaunchPadClient to access the APIs in the SDK.


.. _LaunchPad: https://developer.posrocket.com