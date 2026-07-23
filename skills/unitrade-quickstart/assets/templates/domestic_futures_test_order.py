import os
import time
from unitrade.unitrade import *


CONFIRM_SEND_ORDER = False


def env(name, default=""):
    return os.getenv(name, default)


api = Unitrade()
api.on_error = lambda err: print(f"[Unitrade error] {err}")


def on_reply(orderreply):
    print("[reply]", orderreply)


def on_match(matchreply):
    print("[match]", matchreply)


api.dtrade.on_reply = on_reply
api.dtrade.on_match = on_match

try:
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

    accounts = api.get_accounts()
    if not accounts:
        raise SystemExit("No trading accounts returned by api.get_accounts()")

    actno = env("UNITRADE_ACTNO", accounts[0])

    order = DOrderObject()
    order.actno = actno
    order.note = "test"
    order.subactno = ""
    order.productid = env("UNITRADE_DOMESTIC_PRODUCT", "TXFF5")
    order.bs = env("UNITRADE_BS", "B")
    order.ordertype = env("UNITRADE_ORDER_TYPE", "M")
    order.price = float(env("UNITRADE_PRICE", "0"))
    order.orderqty = int(env("UNITRADE_QTY", "1"))
    order.ordercondition = env("UNITRADE_ORDER_CONDITION", "R")
    order.opencloseflag = env("UNITRADE_OPEN_CLOSE", "")
    order.dtrade = env("UNITRADE_DAY_TRADE", "N")

    print("prepared order:", order)

    if not CONFIRM_SEND_ORDER:
        raise SystemExit(
            "Order was not sent. Set CONFIRM_SEND_ORDER = True only after confirming test environment, account, product, side, quantity, and price."
        )

    order_response = api.dtrade.order(order)
    print("order response:", order_response)

    time.sleep(3)
finally:
    if getattr(api, "login_status_flag", False):
        api.logout()
