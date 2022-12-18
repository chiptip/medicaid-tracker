import plaid
from plaid.api import plaid_api
from plaid.api.plaid_api import PlaidApi
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_get_request import LinkTokenGetRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_account_filters import LinkTokenAccountFilters
from plaid.model.depository_filter import DepositoryFilter
from plaid.model.depository_account_subtypes import DepositoryAccountSubtypes
from plaid.model.depository_account_subtype import DepositoryAccountSubtype
from plaid.model.products import Products
from plaid.model.country_code import CountryCode

# initiating API client

CLIENT_ID = '58a9e242bdc6a44288ea1bf3'
SECRET = 'a836d52b1bc3169de6f04cc8cd09c6'


def get_client() -> PlaidApi:
    """
    obtain Plaid client via instantiation of Plaid API Client
    :return: Plaid client
    """
    configuration = plaid.Configuration(
        host=plaid.Environment.Sandbox,
        api_key={
            'clientId': CLIENT_ID,
            'secret': SECRET
        }
    )

    api_client = plaid.ApiClient(configuration)
    return plaid_api.PlaidApi(api_client)


def create_link_token(api_client: PlaidApi) -> str:

    request = LinkTokenCreateRequest(
        client_name='Sonny Test App',
        products=[Products('auth'), Products('transactions')],
        country_codes=[CountryCode('US')],
        redirect_uri='https://sonnykwok.com/oauth-page',
        language='en',
        webhook='https://sample-webhook-uri.com',
        link_customization_name='default',
        account_filters=LinkTokenAccountFilters(
            depository=DepositoryFilter(
                account_subtypes=DepositoryAccountSubtypes(
                    [
                        DepositoryAccountSubtype('checking'),
                        DepositoryAccountSubtype('savings')
                    ]
                )
            )
        ),
        user=LinkTokenCreateRequestUser(
            client_user_id='123-test-user-id'
        )
    )

    response = api_client.link_token_create(request)
    return response['link_token']


def exchange_public_token(api_client: PlaidApi, public_token):
    request = ItemPublicTokenExchangeRequest(public_token=public_token)
    response = api_client.item_public_token_exchange(request)
    access_token = response['access_token']
    item_id = response['item_id']
