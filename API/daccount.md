---  
nav_order: 10
parent: API Reference  
title: "daccount"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
內期帳務
提供保證金.未平倉.即時部位查詢

<a id="daccount.DAccount"></a>

## DAccount Objects

```python
class DAccount()
```

<a id="daccount.DAccount.on_error"></a>

#### on\_error

錯誤事件

<a id="daccount.DAccount.on_connected"></a>

#### on\_connected

連線成功事件

<a id="daccount.DAccount.on_disconnected"></a>

#### on\_disconnected

斷線事件

<a id="daccount.DAccount.get_current_server"></a>

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

<a id="daccount.DAccount.get_server_list"></a>

#### get\_server\_list

```python
def get_server_list()
```

透過可連結主機
##### 回傳值 dict[Server]: 

| 型別 | 說明 |
| ------ | ------------- |
| key | str | servername |
| value | Server | 主機物件 |

範例
```python
server_list = unitrade.daccount.get_server_list()
for servername, server in server_list.items():
    print(f'主機名稱: {servername})
```

<a id="daccount.DAccount.set_sever_by_name"></a>

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

<a id="daccount.DAccount.get_margin"></a>

#### get\_margin

```python
def get_margin(actno, currency) -> DMarginResponse
```

查詢保證金
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |     
| actno | str | 帳號 |
| currency | str | 幣別 |

##### 回傳值 MarginResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True 成功 /False 失敗 |
| str | 錯誤訊息 |
| List[DMargin] | 保證金物件 |

##### 範例
```python       
margin_response = unitrade.daccount.get_margin("1234567", "TWD")
# DMarginResponse(ok=True, error='', data=
# DMargin(total_count=1, current_count=1, network_id='A00009z103', company='F008000', actno='1234567', account_date='20250619', currency='NTT', exrate=1.0, lctdab=216432431.0, ltdab=212177921.0, dwamt=0.0, osprtlos=0.0, prtlos=4254510.0, optosprtlos=0.0, optprtlos=14741150.0, tpremium=0.0, orignfee=0.0, ctaxamt=0.0, ordpremium=0.0, ctdab=216432431.0, ordiamt=0.0, iamt=19357150.0, mamt=15208800.0, ordcexcess=197075281.0, bpremium=25055200.0, spremium=1819050.0, optequity=239668581.0, inirate=1118.1007, matrate=1423.0737, liquidation_ratio=1238.1398, twdoptequity=239668581.0, twdinirate='1118.1', twdordexcess=197075281.0, securities_payment_amount=0.0, tmp1prices=0.0, optrate=562.69, update_date='20250619', update_time='094552', securities_valuation='0', excerciseprice=0.0, transaction_total_quota=500000.0, excess_margin=0.0, data_source_type='RT', night_session_closing_ctdab=225141351.0, night_session_optrate=628.4, night_session_optequity=248414576.0, night_session_iamt=19332950.0, night_session_mamt=15184600.0))
```

<a id="daccount.DAccount.get_position"></a>

#### get\_position

```python
def get_position(actno, groupid='', trader='') -> DPositionResponse
```

查詢即時部位
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| actno | str | 帳號 |

##### 回傳值 DPositionResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True 成功 <br/>False 失敗 |
| str | 錯誤訊息 |
| List[DPosition] | 即時部位集合物件 |

##### 範例
```python
position_response = unitrade.daccount.get_position("1234567")
# DPositionResponse(ok=True, error='', data=[
#  DPosition(total_count=32, current_count=1, network_id='A00009z107', company='F008000', actno='1234567', currency='NTT', product='NY1', month='202507', call_put='', strike_price=0.0, ot_qty_b=0, ot_qty_s=39, noworder_qty_b=0, noworder_qty_s=0, nowmatch_qty_b=0, nowmatch_qty_s=0, today_close_position=0, current_buy_open_position=0, current_sell_open_position=39, combined_buy_balance=0.0, combined_sell_balance=0.0, open_buy_position_average_cost=0.0, open_sell_position_average_cost=48.4425, buyer_IAMT=0.0, seller_IAMT=6123000.0, buyer_MAMT=0.0, seller_MAMT=4719000.0, product_base_number=40000, reference_realPrice=43.82, close_position_pnl=0.0, product_name='元大台50 107', buy_spread_points=0.0, sell_spread_points=4.6225, floating_pnl=7211100.0, data_source_type='RT', productkind='1', productid='NY1G5'),
#  DPosition(total_count=32, current_count=2, network_id='A00009z107', company='F008000', actno='1234567', currency='NTT', product='NYF', month='202507', call_put='', strike_price=0.0, ot_qty_b=0, ot_qty_s=42, noworder_qty_b=0, noworder_qty_s=0, nowmatch_qty_b=0, nowmatch_qty_s=0, today_close_position=0, current_buy_open_position=0, current_sell_open_position=42, combined_buy_balance=0.0, combined_sell_balance=0.0, open_buy_position_average_cost=0.0, open_sell_position_average_cost=41.4404, buyer_IAMT=0.0, seller_IAMT=1680000.0, buyer_MAMT=0.0, seller_MAMT=1302000.0, product_base_number=10000, reference_realPrice=43.82, close_position_pnl=0.0, product_name='元大台灣5007', buy_spread_points=0.0, sell_spread_points=-2.3796, floating_pnl=-999432.0, data_source_type='RT', productkind='1', productid='NYFG5')
#  ...])
```

<a id="daccount.DAccount.get_unliquidation"></a>

#### get\_unliquidation

```python
def get_unliquidation(actno,
                      currency='',
                      action='3',
                      sort='') -> DUnliquidationResponse
```

查詢未平倉彙總
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| actno | str | 帳號 |
| currency | str | 幣別 |

##### 回傳值 DUnliquidationResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True: 成功<br/>False: 失敗 |
| str | 錯誤訊息 |
| List[DUnliquidation] | 未平倉彙總集合物件 |

##### 範例
```python
unliquidation_response = unitrade.daccount.get_unliquidation("1234567")
# DUnliquidationResponse(ok=True, error='', data=[
# DUnliquidation(total_count=32, current_count=1, network_id='A00009z100', company='F008000',actno='1234567', productid='NY1G5', bs='S', totalotqty=39, avgmatchprice=48.4426, realprice=43.82, reftotalpl=6619200.0, ctaxamt=1507.0, commission_fee=681.0, net_profit_loss=6617012.0, leg1_product_category='F', leg1_product_date='202507', leg1_strike_price='0', leg1_call_put='', leg1_buy_sell='S', leg1_average_price=48.4426, leg2_product_category='', leg2_product_date='', leg2_strike_price='0', leg2_call_put='', leg2_buy_sell='', leg2_average_price=0.0, product_name='元大台50 107', leg1_productid='NY1', leg2_productid='', multiname='', data_source_type='RT'), 
# DUnliquidation(total_count=32, current_count=2, network_id='A00009z100', company='F008000', actno='1234567', productid='NYFG5', bs='S', totalotqty=42, avgmatchprice=41.4405, realprice=43.82, reftotalpl=-1127400.0, ctaxamt=336.0, commission_fee=759.0, net_profit_loss=-1128495.0, leg1_product_category='F', leg1_product_date='202507', leg1_strike_price='0', leg1_call_put='', leg1_buy_sell='S', leg1_average_price=41.4405, leg2_product_category='', leg2_product_date='', leg2_strike_price='0', leg2_call_put='', leg2_buy_sell='', leg2_average_price=0.0, product_name='元大台灣5007', leg1_productid='NYF', leg2_productid='', multiname='', data_source_type='RT'),
# ...
# ])
```

<a id="daccount.DAccount.get_combine"></a>

#### get\_combine

```python
def get_combine(type, actno, comno1, comym1, strikeprice1, callput1, bs1, qty1,
                comno2, comym2, strikeprice2, callput2, bs2, qty2) -> Response
```

申請組拆功能
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| type | str | 1:拆解 <br> 2:全部拆解 <br> 3:組合 |
| actno | str | 帳號 |
| comno1 | str | 商品代碼1 |
| comym1 | str | 年月1 預設年月(格式YYYYMM) 但股票週選會放年月日(格式YYMMDD) |
| strikeprice1 | str | 履約價1 |
| callput1 | str | Call/Put1 <br> C:Call <br> P:Put |
| bs1 | str |  買賣別1<br> B:買<br> S:賣 |
| qty1  | str |口數1 |
| comno2 | str | 商品代碼2 |
| comym2 | str | 年月2 預設年月(格式YYYYMM) 但股票週選會放年月日(格式YYMMDD) |
| strikeprice2 | float | 履約價2 |
| callput2 | str | Call/Put2 <br> C:Call <br> P:Put |
| bs2 | str |  買賣別2<br> B:買<br> S:賣 |
| qty2  | str |口數2 | 

##### 回傳值 Response 

| 型別 | 說明 |
| ------ | ------------- |
| bool | True 成功<br>False 失敗 |
| str | 錯誤訊息 |

##### 範例
```python
response = daccount.get_combine("3","帳號7碼","TXO","202507","21000","C","S",1,"TXO","202507","21000","P","S",1)
# 組合成功範例:
# Response(ok=True, error='')
# 組合失敗範例
# Response(ok=False, error='無此組合商品')
```

<a id="daccount.DAccount.get_net"></a>

#### get\_net

```python
def get_net(actno) -> Response
```

申請買賣並存沖銷
##### 參數  

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| actno | str | 帳號 |

##### 回傳值 Response

| 型別 | 說明 |
| ------ | ------------- |
| bool |  True: 成功<br> False: 失敗   |
| str  |   錯誤訊息   |

##### 範例
```python
response = daccount.get_net("帳號7碼")
# 申請成功範例:
# Response(ok=True, error='') 
# 申請失敗範例
# Response(ok=False, error='全組或全拆筆數為零')
```

<a id="daccount.DAccount.close"></a>

#### close

```python
def close()
```

關閉物件

