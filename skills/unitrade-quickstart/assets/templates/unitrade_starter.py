import os
from unitrade.unitrade import *


def env(name, default=""):
    value = os.getenv(name, default)
    if value == "":
        print(f"[setup] {name} is empty")
    return value


api = Unitrade()
api.on_error = lambda err: print(f"[Unitrade error] {err}")

login_response = api.login(
    env("UNITRADE_URL", "https://test167.pfctrade.com"),
    env("UNITRADE_USERID"),
    env("UNITRADE_PASSWORD"),
    env("UNITRADE_CA_PATH"),
    env("UNITRADE_CA_PASSWORD"),
)

if not login_response.ok:
    print("login failed:", login_response)
    raise SystemExit(1)

print("login flag:", api.login_status_flag)
accounts = api.get_accounts()
print("accounts:", accounts)

domestic_products = api.get_domestic_products()
print("domestic product sample:", list(domestic_products.keys())[:10])

foreign_exchanges = api.get_exchanges()
print("foreign exchange sample:", list(foreign_exchanges.keys())[:10])

product_id = os.getenv("UNITRADE_DOMESTIC_PRODUCT", "TXFG5")
quote_response = api.dquote.query_tick_data_trade(product_id)
print(f"domestic quote {product_id}:", quote_response)

api.logout()
print("logout flag:", api.login_status_flag)
