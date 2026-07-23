# Unitrade Tutorial Recipes

Use this when the user wants a complete starter flow or code adapted from the tutorials.

## Login Starter

```python
import unitrade
from unitrade.unitrade import *

api = Unitrade()

def on_error(err):
    print(f"API Error: {err}")

api.on_error = on_error

login_response = api.login(
    "登入url",
    "帳號",
    "密碼",
    "憑證檔名",
    "憑證密碼",
)

if login_response.ok:
    print("登入成功")
    accounts = api.get_accounts()
    print(f"可用帳號: {accounts}")
else:
    print(f"登入失敗: {getattr(login_response, 'errorcode', '')} {getattr(login_response, 'errormsg', login_response)}")
```

## Product And Contract Lookup

```python
domestic_products = api.get_domestic_products()
print(list(domestic_products.items())[:5])

txf_contracts = api.get_domestic_contracts("TXF", "F")
txo_contracts = api.get_domestic_contracts("TXO", "O")

exchanges = api.get_exchanges()
foreign_products = api.get_foreign_products()
nq_contracts = api.get_foreign_contracts("CME", "NQ", "F")
ado_options = api.get_foreign_contracts("CME", "ADO", "O")
```

## Connection Events And Server Switching

```python
def dquote_on_connected():
    print("內期報價連線:", api.dquote.get_current_server())

api.dquote.on_connected = dquote_on_connected

print(api.dquote.get_server_list())

if hasattr(api.dquote, "set_sever_by_name"):
    api.dquote.set_sever_by_name("217")
else:
    api.dquote.set_server_by_name("217")
```

Use this defensive spelling because the docs contain both `set_sever_by_name` and `set_server_by_name`.

## Domestic Quote Snapshot

```python
productid = "TXFG5"

trade_response = api.dquote.query_tick_data_trade(productid)
bid_offer_response = api.dquote.query_tick_data_bid_offer(productid)
open_response = api.dquote.query_tick_data_open(productid)
high_low_response = api.dquote.query_tick_data_high_low(productid)
index_response = api.dquote.query_index_data("TXF")
settle_response = api.dquote.query_tick_data_settle("TXFH5")

for name, response in {
    "trade": trade_response,
    "bid_offer": bid_offer_response,
    "open": open_response,
    "high_low": high_low_response,
    "index": index_response,
    "settle": settle_response,
}.items():
    print(name, response)
```

## Domestic Quote Subscription

```python
def on_tick_data_trade(data):
    print("成交價量:", data)

def on_tick_data_bid_offer(data):
    print("五檔:", data)

api.dquote.on_tick_data_trade = on_tick_data_trade
api.dquote.on_tick_data_bid_offer = on_tick_data_bid_offer

sub_ok, msg = api.dquote.subscribe_trade_bid_offer("TXFG5")
print(f"訂閱結果: {sub_ok} {msg}")

# 完成後:
# api.dquote.unsubscribe_trade_bid_offer("TXFG5")
```

## Foreign Quote Snapshot

```python
exchange = "CME"
symbol = "NQ"
ym = "202509"
strike = ""
cp = "F"

print(api.fquote.query_tick_data_trade(exchange, symbol, ym, strike, cp))
print(api.fquote.query_tick_data_bid(exchange, symbol, ym, strike, cp))
print(api.fquote.query_tick_data_offer(exchange, symbol, ym, strike, cp))
print(api.fquote.query_tick_data_implied(exchange, symbol, ym, strike, cp))
print(api.fquote.query_tick_data_open_close(exchange, symbol, ym, strike, cp))
print(api.fquote.query_tick_data_high_low(exchange, symbol, ym, strike, cp))
print(api.fquote.query_tick_data_settle(exchange, symbol, ym, strike, cp))
```

## Foreign Quote Subscription

```python
def on_tick_data_trade(data):
    print("外期成交:", data)

def on_tick_data_bid(data):
    print("外期買價:", data)

def on_tick_data_offer(data):
    print("外期賣價:", data)

api.fquote.on_tick_data_trade = on_tick_data_trade
api.fquote.on_tick_data_bid = on_tick_data_bid
api.fquote.on_tick_data_offer = on_tick_data_offer

# The API and tutorial pages disagree on whether the last two args are
# (cp, strike) or (strike, cp). Confirm against the installed package.
sub_ok, msg = api.fquote.subscribe("CME", "NQ", "202509", "", "F")
print(f"訂閱結果: {sub_ok} {msg}")

# 完成後:
# api.fquote.unsubscribe("CME", "NQ", "202509", "", "F")
```

## History Bars

```python
from datetime import datetime

response = api.dquote.get_history_bardata(
    "1K",
    datetime(2025, 6, 10),
    datetime(2025, 7, 7),
    "1",
    "MXFG5",
    2,
)

foreign_response = api.fquote.get_history_bardata(
    "1K",
    datetime(2025, 6, 10, 0, 0, 0),
    datetime(2025, 7, 7, 0, 0, 0),
    "1",
    "CMX",
    "GC",
    "202508",
    "F",
    "",
    2,
)
```

## Stock Quote Snapshot

```python
print(api.squote.query_tick_data("2330"))
print(api.squote.query_tick_open_close("2330"))
print(api.squote.query_base_data("2330"))

print(api.squote.query_otc_tick_data("5483"))
print(api.squote.query_otc_tick_open_close("5483"))
print(api.squote.query_otc_base_data("5483"))

print(api.squote.query_index_data("IX0001"))
print(api.squote.query_otc_index_data("IX0043"))
```

## Stock Quote Subscription

```python
def on_tick_data(data):
    print("現貨即時行情:", data)

def on_base_data(data):
    print("現貨基本資料:", data)

def on_tick_data_open_close(data):
    print("開收盤:", data)

def on_index_data(data):
    print("指數:", data)

api.squote.on_tick_data = on_tick_data
api.squote.on_base_data = on_base_data
api.squote.on_tick_data_open_close = on_tick_data_open_close
api.squote.on_index_data = on_index_data

print(api.squote.sub_stock("2330"))
print(api.squote.sub_index("IX0001"))

# 完成後:
# api.squote.unsub_stock("2330")
# api.squote.unsub_index("IX0001")
```

## Domestic Order Workflow

Always register callbacks first.

```python
def on_reply(orderreply):
    print(f"委託回報: {orderreply}")

def on_match(matchreply):
    print(f"成交回報: {matchreply}")

api.dtrade.on_reply = on_reply
api.dtrade.on_match = on_match

order = DOrderObject()
order.actno = actno
order.note = "test"
order.subactno = ""
order.productid = "TXFF5"
order.bs = "B"
order.ordertype = "M"
order.price = 0
order.orderqty = 1
order.ordercondition = "R"
order.opencloseflag = ""
order.dtrade = "N"

order_response = api.dtrade.order(order)
print(order_response.issend, order_response.seq, order_response.errorcode, order_response.errormsg)
```

Modify or cancel:

```python
replace = DReplaceObject()
replace.replacetype = "4"   # 4 cancel, 5 decrease, m modify price
replace.actno = actno
replace.orderno = "委託書號"

replace_response = api.dtrade.replace_order(replace)
print(replace_response.issend, replace_response.errormsg)
```

Query:

```python
reply_response = api.dtrade.query_reply(actno, 500, "", "", "", "")
match_response = api.dtrade.query_match(actno, 500, "", "", "", "")
print(reply_response)
print(match_response)
```

## Foreign Order Workflow

Always register callbacks first.

```python
def on_reply(orderreply):
    print(f"外期委託回報: {orderreply.orderno} {orderreply.orderstatus}")

def on_match(matchreply):
    print(f"外期成交回報: {matchreply.orderno} {matchreply.matchprice}")

api.ftrade.on_reply = on_reply
api.ftrade.on_match = on_match

order = FOrderObject()
order.actno = actno
order.subactno = ""
order.note = "ordertest"
order.exchange = "CME"
order.symbol = "AD"
order.maturitymonthyear = "202409"
order.putorcall = "F"
order.strikeprice = ""
order.bs = "B"
order.ordertype = "M"
order.price = 0
order.stopprice = 0
order.orderqty = 1
order.ordercondition = "R"
order.opencloseflag = "0"
order.dtrade = "N"

order_response = api.ftrade.order(order)
print(order_response.issend, order_response.seq, order_response.errorcode, order_response.errormsg)
```

Query:

```python
reply_response = api.ftrade.query_reply(actno, 500, "", "", "", "")
match_response = api.ftrade.query_match(actno, 500, "", "", "", "")
print(reply_response)
print(match_response)
```

## Account Queries

```python
actno = api.get_accounts()[0]

print(api.daccount.get_margin(actno, "NTT"))
print(api.daccount.get_unliquidation(actno, "NTT"))
print(api.daccount.get_position(actno))

print(api.faccount.get_margin(actno))
print(api.faccount.get_unliquidation(actno))
print(api.faccount.get_position(actno))
```

Domestic account also supports:

```python
api.daccount.get_combine(...)
api.daccount.get_net(actno)
```
