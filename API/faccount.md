---  
nav_order: 12
parent: API Reference  
title: "faccount"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
外期帳務
提供保證金.未平倉.即時部位查詢

<a id="faccount.FAccount"></a>

## FAccount Objects

```python
class FAccount()
```

<a id="faccount.FAccount.on_error"></a>

#### on\_error

錯誤事件

<a id="faccount.FAccount.on_connected"></a>

#### on\_connected

連線成功事件

<a id="faccount.FAccount.on_disconnected"></a>

#### on\_disconnected

斷線事件

<a id="faccount.FAccount.get_current_server"></a>

#### get\_current\_server

```python
def get_current_server()
```

目前連結主機
##### 回傳值 str 
##### 範例
```python
server = daccount.get_current_server()
print(server)  # 輸出目前連結的主機 
```

<a id="faccount.FAccount.get_server_list"></a>

#### get\_server\_list

```python
def get_server_list()
```

透過可連結主機
##### 回傳值 dict[Server]

| 型別 | 說明 |
| ------ | ------------- |
| key | str | servername |
| value | Server | 主機物件 |

##### 範例
```python
server_list = unitrade.daccount.get_server_list()
for servername, server in server_list.items():
    print(f'主機名稱: {servername})
```

<a id="faccount.FAccount.set_sever_by_name"></a>

#### set\_sever\_by\_name

```python
def set_sever_by_name(servername)
```

透過主機名稱切換連結主機
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |      
| servername | str | 主機名稱 |

##### 回傳值 bool

| 型別 | 說明 |
| ------ | ------------- |
| True | 切換連線成功 |
| False | 切換連線失敗 |

##### 範例
```python
success = unitrade.daccount.set_sever_by_name("xxx")
if success:
    print("連線成功")
else:
    print("連線失敗")
```

<a id="faccount.FAccount.get_margin"></a>

#### get\_margin

```python
def get_margin(actno)
```

查詢保證金
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| actno | str | 帳號 |

##### 回傳值 FMarginResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True 成功 /False 失敗 |
| str | 錯誤訊息 |
| List[FMargin] | 保證金集合物件 |

##### 範例
```python        
margin_response = unitrade.faccount.get_margin("1234567")
# FMarginResponse(ok=True, error='', data=[
# FMargin(total_count=15, current_count=1, web_code='PF2', web_serial='000041', currency='***', previous_day_balance=295423497.0, commission=1034.0, exchange_rate=1.0, futures_tax=21.0, deposit_withdrawal_amount=0.0, close_pnl=0.0, unrealized_pnl=7575940.0, buy_option_market_value=341151.0, sell_option_market_value=0.0, order_withholding_premium=0.0, today_premium_income_expense=0.0, net_value=302998382.0, original_margin=13218455.0, maintenance_margin=12016777.0, available_balance=281348836.0, order_available_margin=0.0, today_order_margin=855151.0, performance_pnl=0.0, variable_premium=341151.0, marking_time='000000', additional_payment=289779927.0, yesterday_unrealized_pnl=0.0, today_intraday_unrealized_pnl=7575940.0, sell_vertical_spread_market_value=0.0, strike_payment=0.0, today_balance=295422442.0, account_total_market_value=303339533.0, full_original_margin=13218455.0, total_market_value_risk=2237.08, risk_coefficient=2292.24, maintenance_rate=2353.95, company_type='F008000', account='1234567', group='', trader=''),
# ...
# ])
```

<a id="faccount.FAccount.get_position"></a>

#### get\_position

```python
def get_position(actno, groupid='', trader='')
```

查詢即時部位
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| actno | str | 帳號 |

##### 回傳值 FPositionResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True 成功 /False 失敗 |
| str | 錯誤訊息 |
| List[FPosition] | 即時部位集合物件 |

##### 範例
```python       
position_response = unitrade.faccount.get_position("1234567")
# FPositionResponse(ok=True, error='', data=[
# FPosition(total_count=15, current_count=1, web_code='PF2', web_serial='000075', company_type='F008000', client_account='1234567', exchange='CBT', trade_type='0', product_code='C', product_year_month='202507', strike_price=0.0, buy_sell_option='', net_buy=2, net_sell=0, buyer_position=2, seller_position=0, buyer_transaction=0, seller_transaction=0, buyer_order=0, seller_order=0, delivery_date='00000000', currency='USD', average_deal_price=436.1, instant_price=490.1, unrealized_pnl=5400.0, close_volume=0, close_pnl=0.0, group='', trader='', abbreviation='玉米', price_base='4'),
#  FPosition(total_count=15, current_count=2, web_code='PF2', web_serial='000075', company_type='F008000', client_account='1234567', exchange='CBT', trade_type='1', product_code='CO', product_year_month='202507', strike_price=450.0, buy_sell_option='C', net_buy=7, net_sell=0, buyer_position=7, seller_position=0, buyer_transaction=0, seller_transaction=0, 
# ..])
```

<a id="faccount.FAccount.get_unliquidation"></a>

#### get\_unliquidation

```python
def get_unliquidation(actno)
```

查詢未平倉彙總
 ##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| actno | str | 帳號 |
| currency | str | 幣別 |

##### 回傳值 FUnliquidationResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True 成功 /False 失敗  |
| str | 錯誤訊息 |
| List[FUnliquidation] | 未平倉彙總集合物件 |

##### 範例
```python
unliquidation_response = unitrade.faccount.get_unliquidation("1234567")
# FUnliquidationResponse(ok=True, error='', data=[
#  FUnliquidation(total_count=15, current_count=1, company_type='F008000', client_account='1234567', exchange='CME', buy_sell_type_1='B', trade_type_1='0', product_code_1='AD', product_year_month_1='202506', strike_price_1=0.0, buy_sell_option_1='', open_interest_1=41, settlement_price_1=0.0, spot_price_1=0.0, unrealized_pnl_1=-2466635.0, initial_margin_1=99220.0, maintenance_margin_1=90200.0, currency_1='USD', deal_price_1=6016.1829268, broker_code='PHI', unrealized_pnl_ntd_1=-72856655.0, commission_1=635.0, business_tax_1=12.7, net_open_interest_pnl_1=-2467282.7, net_open_interest_pnl_ntd_1=-72875789.0, group='', trader='', abbreviation='澳幣', backend_pricebase='1', display_pricebase='1'),
# ...])
```

<a id="faccount.FAccount.close"></a>

#### close

```python
def close()
```

關閉物件

