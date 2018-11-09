# POSRocket Python SDK

Docs: https://posrocket-python-sdk.readthedocs.io/

quick start:

1. install pos python sdk using:
    `pip install git+git://github.com/posrocket/posrocket-python-sdk.git`

2. import pos module in your python script:
    `from posrocket import LaunchPadClient`

3. create client object:
    `pos_client = LaunchPadClient(<your_oauth_client_id>,<your_oauth_client_secret>)`

4. generate authorization url:
    `auth_url = pos_client.get_authorization_url(<your_redirect_url>)`

5. After the user authorize the app on Lunchpad we will redirect him back to the return url.

6. retrieve the access_token from the return url by using the following function:
    `token = pos_client.get_token(<full_return_url_with_queryparams>,<your_redirect_url>)`

7. now you can call any API endpoint by calling the corresponding service
    `business_info = pos_client.business_service.get_business_info()`
