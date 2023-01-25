from degiro_connector.trading.api import API as TradingAPI
from degiro_connector.trading.models.trading_pb2 import Credentials

credentials = Credentials(
    int_account=None,
    username="username",
    password=r'password',
    totp_secret_key=None,
    one_time_password=000000,
)

# SETUP TRADING API
trading_api = TradingAPI(credentials=credentials)

# CONNECT
trading_api.connect()

# FETCH CONFIG TABLE
# client_details_table = trading_api.get_client_details()

# DISPLAY DATA
print("*** connected!***")
# print("Here is the rest your details :", client_details_table)
            