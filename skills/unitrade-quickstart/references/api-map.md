# Unitrade API Map

Use this when choosing a component, method, callback, or return object.

## Core Setup

```python
import unitrade
from unitrade.unitrade import *

api = Unitrade()
api.on_error = lambda err: print(f"API Error: {err}")

login_response = api.login(url, userid, password, ca_path, ca_password)
```

Check `login_response.ok` and `api.login_status_flag`. On success, call `api.get_accounts()` before account-bound operations.

## Component Map

| Need | Component | Notes |
| --- | --- | --- |
| Login, logout, accounts | `api` | `login`, `logout`, `get_accounts` |
| Domestic products/contracts | `api` | `get_domestic_products`, `get_domestic_contracts(symbol, type)` |
| Foreign exchanges/products/contracts | `api` | `get_exchanges`, `get_foreign_products`, `get_foreign_contracts(exchange, symbol, type)` |
| Domestic futures/options quote | `api.dquote` | Snapshot, subscription, history bars |
| Domestic futures/options order | `api.dtrade` | Order, replace, query reply/match |
| Foreign futures/options order | `api.ftrade` | Order, replace, query reply/match |
| Domestic futures account | `api.daccount` | Margin, position, unliquidated, combine, net |
| Foreign futures account | `api.faccount` | Margin, position, unliquidated |

## Naming Caveats

- API docs use `set_sever_by_name(servername)` in component references. Some tutorial text shows `set_server_by_name`; if one spelling fails, try the other and mention the docs mismatch.
- Some API files spell disconnected callbacks as `on_disonnected` for quote/trade/stock components, while tutorials may show `on_disconnected`. For account components, API files show `on_disconnected`.
- Query responses usually expose `ok`, `error`, and `data`. Order responses expose `issend`, `errorcode`, `errormsg`, `note`, and `seq`.

## Core API Methods

```python
api.login(url, userid, password, ca_path, ca_password) -> LoginResponse
api.logout()
api.get_domestic_products()
api.get_foreign_products()
api.get_exchanges()
api.get_domestic_contracts(symbol, type) -> DomesticContractResponse
api.get_foreign_contracts(exchange, symbol, type) -> ForeignContractResponse
api.get_accounts() -> list[str]
```

Contract `type` uses `"F"` for futures and `"O"` for options.

## Shared Component Methods

Most quote/trade/account components provide:

```python
component.on_error = callback
component.on_connected = callback
component.get_current_server()
component.get_server_list()
component.set_sever_by_name(servername)
component.close()
```

## Domestic Trade: `api.dtrade`

Callbacks:

```python
api.dtrade.on_reply = on_reply      # DOrderReply
api.dtrade.on_match = on_match      # DMatchReply
```

Methods:

```python
api.dtrade.order(obj: DOrderObject) -> DOrderResponse
api.dtrade.replace_order(obj: DReplaceObject) -> DOrderResponse
api.dtrade.query_reply(actno, num_of_query, network_id_start, network_id_end, order_time_start, order_time_end)
api.dtrade.query_match(actno, num_of_query, network_id_start, network_id_end, match_time_start, match_time_end)
```

`DOrderObject` fields commonly used:

```python
actno, subactno, productid, bs, ordertype, price, orderqty,
ordercondition, opencloseflag, dtrade, note
```

Order flags:

- `bs`: `"B"` buy, `"S"` sell.
- `ordertype`: `"M"` market, `"L"` limit, `"P"` range market in domestic examples.
- `ordercondition`: `"I"` IOC, `"R"` ROD, `"F"` FOK.
- `opencloseflag`: `"0"` open, `"1"` close, blank for auto/unspecified in examples.
- `dtrade`: `"Y"` day trade, `"N"` non-day-trade.
- `DReplaceObject.replacetype`: `"4"` cancel, `"5"` decrease quantity, `"m"` modify price.

## Foreign Trade: `api.ftrade`

Callbacks:

```python
api.ftrade.on_reply = on_reply      # FOrderReply
api.ftrade.on_match = on_match      # FMatchReply
```

Methods:

```python
api.ftrade.order(obj: FOrderObject) -> FOrderResponse
api.ftrade.replace_order(obj: FReplaceObject) -> FOrderResponse
api.ftrade.query_reply(actno, num_of_query, network_id_start, network_id_end, order_time_start, order_time_end)
api.ftrade.query_match(actno, num_of_query, network_id_start, network_id_end, match_time_start, match_time_end)
```

`FOrderObject` fields commonly used:

```python
actno, subactno, exchange, symbol, maturitymonthyear, putorcall,
strikeprice, bs, ordertype, price, stopprice, orderqty,
ordercondition, opencloseflag, dtrade, note
```

Foreign order flags:

- `putorcall`: `"F"` futures, `"C"` call, `"P"` put.
- `ordertype`: `"M"` market, `"L"` limit, `"3"` stop market, `"4"` stop limit.
- `ordercondition`: `"I"` IOC, `"R"` ROD, `"F"` FOK.
- `FReplaceObject.replacetype`: `"4"` cancel, `"5"` decrease quantity, `"m"` modify price.

## Domestic Quote: `api.dquote`

Callbacks:

```python
api.dquote.on_tick_data_trade = on_tick_data_trade
api.dquote.on_tick_data_bid_offer = on_tick_data_bid_offer
api.dquote.on_tick_data_high_low = on_tick_data_high_low
api.dquote.on_tick_data_open = on_tick_data_open
api.dquote.on_index_data = on_index_data
api.dquote.on_tick_data_settle = on_tick_data_settle
```

Snapshot methods:

```python
api.dquote.query_tick_data_trade(productid)
api.dquote.query_tick_data_bid_offer(productid)
api.dquote.query_tick_data_high_low(productid)
api.dquote.query_tick_data_before_trade(productid)
api.dquote.query_tick_data_before_bid_offer(productid)
api.dquote.query_tick_data_open(productid)
api.dquote.query_index_data(productid)
api.dquote.query_tick_data_settle(productid)
```

Subscription methods:

```python
api.dquote.subscribe_trade_bid_offer(productid)
api.dquote.unsubscribe_trade_bid_offer(productid)
api.dquote.subscribe_high_low(productid)
api.dquote.unsubscribe_high_low(productid)
api.dquote.subscribe_open(productid)
api.dquote.unsubscribe_open(productid)
api.dquote.subscribe_index_data(kind, index)
api.dquote.unsubscribe_index_data(kind, index)
api.dquote.subscribe_settle(productid)
api.dquote.unsubscribe_settle(productid)
```

History:

```python
api.dquote.get_history_bardata(interval, startdate, enddate, productkind, productid, count)
```

## Account Components

Domestic account:

```python
api.daccount.get_margin(actno, currency) -> DMarginResponse
api.daccount.get_unliquidation(actno, currency) -> DUnliquidationResponse
api.daccount.get_position(actno, groupid="", trader="") -> DPositionResponse
api.daccount.get_combine(type, actno, comno1, comym1, strikeprice1, callput1, bs1, qty1, comno2, comym2, strikeprice2, callput2, bs2, qty2)
api.daccount.get_net(actno) -> Response
```

Foreign account:

```python
api.faccount.get_margin(actno) -> FMarginResponse
api.faccount.get_unliquidation(actno) -> FUnliquidationResponse
api.faccount.get_position(actno, groupid="", trader="") -> FPositionResponse
```

## Product Codes

- Domestic futures product code pattern: product + contract type + month code + year digit, e.g. `TXFH9`.
- Domestic futures month codes: January to December are `A B C D E F G H I J K L`.
- Domestic options use product + contract type + five-digit strike + month/year code. Call months use `A-L`; Put months use `M-X`.
- Foreign product lookup should use `api.get_exchanges()`, `api.get_foreign_products()`, and `api.get_foreign_contracts(exchange, symbol, type)` because contract lists change.
