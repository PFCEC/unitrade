---  
nav_order: 14
parent: API Reference  
title: "dquote"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
內期行情
註冊接收即時和查詢

<a id="dquote.DQuote"></a>

## DQuote Objects

```python
class DQuote()
```

<a id="dquote.DQuote.on_error"></a>

#### on\_error

錯誤事件

<a id="dquote.DQuote.on_connected"></a>

#### on\_connected

連線成功事件

<a id="dquote.DQuote.on_disonnected"></a>

#### on\_disonnected

斷線事件

<a id="dquote.DQuote.on_tick_data_trade"></a>

#### on\_tick\_data\_trade

成交價事件..傳入物件:DTickDataTrade

<a id="dquote.DQuote.on_tick_data_high_low"></a>

#### on\_tick\_data\_high\_low

最高最低價事件..傳入物件:DTickDataHighLow

<a id="dquote.DQuote.on_index_data"></a>

#### on\_index\_data

現貨價事件..傳入物件:DIndexData

<a id="dquote.DQuote.on_tick_data_bid_offer"></a>

#### on\_tick\_data\_bid\_offer

五檔事件..傳入物件:DTickDataBidOffer

<a id="dquote.DQuote.on_tick_data_before_trade"></a>

#### on\_tick\_data\_before\_trade

試撮成交價事件..傳入物件:DTickDataBeforeTrade

<a id="dquote.DQuote.on_tick_data_before_bid_offer"></a>

#### on\_tick\_data\_before\_bid\_offer

試撮五檔事件..傳入物件:DTickDataBeforeBidOffer

<a id="dquote.DQuote.on_tick_data_open"></a>

#### on\_tick\_data\_open

開盤價事件..傳入物件:DTickDataOpen

<a id="dquote.DQuote.get_current_server"></a>

#### get\_current\_server

```python
def get_current_server()
```

目前連結主機
##### 回傳值 str 
##### 範例
```python
server = unitrade.dquote.get_current_server()
print(server)  # 輸出目前連結的主機 
```

<a id="dquote.DQuote.get_server_list"></a>

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
server_list = unitrade.dquote.get_server_list()
for servername, server in server_list.items():
    print(f'主機名稱: {servername})
```

<a id="dquote.DQuote.set_sever_by_name"></a>

#### set\_sever\_by\_name

```python
def set_sever_by_name(servername) -> Tuple[bool, str]
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
success = unitrade.dquote.set_sever_by_name("xxx")
if success:
    print("連線成功")
else:
    print("連線失敗")
```

<a id="dquote.DQuote.get_subscribe_trade_bid_offer"></a>

#### get\_subscribe\_trade\_bid\_offer

```python
def get_subscribe_trade_bid_offer()
```

查詢已註冊成交.賣賣價量 商品
##### 回傳值 list[str]

| 型別 | 說明 |
| ------ | ------------- |
| list[str] | 註冊的商品代碼列表 |

##### 範例
```python
subscribed_products = unitrade.dquote.get_subscribe_trade_bid_offer()
print(subscribed_products)  # 輸出已註冊的商品代碼列表
```

<a id="dquote.DQuote.get_subscribe_highlow"></a>

#### get\_subscribe\_highlow

```python
def get_subscribe_highlow()
```

查詢已註冊最高最低價商品代碼列表
##### 回傳值 list[str]

| 型別 | 說明 |
| ------ | ------------- |
| list[str] | 已註冊最高最低價商品代碼列表 |

##### 範例
```python
subscribed_highlow_products = unitrade.dquote.get_subscribe_highlow()
print(subscribed_highlow_products)
# 輸出已註冊的最高最低價商品代碼列表
```

<a id="dquote.DQuote.get_subscribe_index_data"></a>

#### get\_subscribe\_index\_data

```python
def get_subscribe_index_data()
```

查詢已註冊現貨 商品
##### 回傳值 list[str]  

| 型別 | 說明 |
| ------ | ------------- |
| list[str] | 註冊的現貨商品代碼列表 |

##### 範例
```python
subscribed_index_products = unitrade.dquote.get_subscribe_index_data()
print(subscribed_index_products)  # 輸出已註冊的現貨商品代碼列表
```

<a id="dquote.DQuote.get_subscribe_open"></a>

#### get\_subscribe\_open

```python
def get_subscribe_open()
```

查詢已註冊開盤價 商品
##### 回傳值 list[str]  

| 型別 | 說明 |
| ------ | ------------- |
| list[str] | 註冊的開盤價商品代碼列表 |

##### 範例
```python
subscribed_open_products = unitrade.dquote.get_subscribe_open()
print(subscribed_open_products)
```

<a id="dquote.DQuote.query_tick_data_trade"></a>

#### query\_tick\_data\_trade

```python
def query_tick_data_trade(productid) -> DTickDataTradeResponse
```

查詢最後成交價量
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |

##### 回傳值 DTickDataTradeResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | DTickDataTrade | 成交價量資料 |

##### 範例
```python
response = unitrade.dquote.query_tick_data_trade("TXFF5")
# DTickDataTradeResponse(ok=True, error='', data=DTickDataTrade(commodityid='TXFG5', infotime='132333276000', matchprice=21699.0, matchquantity=2, matchtotalqty=45901, matchbuycnt=31986, matchsellcnt=30551, matchtime='132333178000', matchpricedata=[], matchqtydata=[]))
```

<a id="dquote.DQuote.query_tick_data_high_low"></a>

#### query\_tick\_data\_high\_low

```python
def query_tick_data_high_low(productid) -> DTickDataHighLowResponse
```

查詢最高(低)價
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |

##### 回傳值 DTickDataHighLowResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | DTickDataHighLow | 最高(低)價資料 |

##### 範例
```python 
response = unitrade.dquote.query_tick_data_high_low("TXFG5")
# DTickDataHighLowResponse(ok=True, error='', data=DTickDataHighLow(commodityid='TXFG5', showtime='105141451000', dayhighprice=21857.0, daylowprice=21675.0))
```

<a id="dquote.DQuote.query_tick_data_before_trade"></a>

#### query\_tick\_data\_before\_trade

```python
def query_tick_data_before_trade(productid) -> DTickDataBeforeTradeResponse
```

查詢最後盤前成交價量
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |

##### 回傳值 DTickDataBeforeTradeResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | DTickDataBeforeTrade | 盤前成交價量  |

##### 範例
```python 
response = unitrade.dquote.query_tick_data_before_trade("TXFG5")
# DTickDataBeforeTradeResponse(ok=True, error='', data=DTickDataBeforeTrade(commodityid='TXFG5', infotime='084455000000', matchprice=21810.0, matchquantity=125, matchtotalqty=0, matchbuycnt=0, matchsellcnt=0, matchtime='084455000000'))
```

<a id="dquote.DQuote.query_tick_data_open"></a>

#### query\_tick\_data\_open

```python
def query_tick_data_open(productid) -> DTickDataOpenResponse
```

查詢開盤價
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |

##### 回傳值 DTickDataOpenResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | DTickDataOpen | 開盤價  |

##### 範例
```python         
response = unitrade.dquote.query_tick_data_open("TXFG5")
# DTickDataOpenResponse(ok=True, error='', data=DTickDataOpen(commodityid='TXFG5', opentime='084500060000', openprice=21820.0, openquantity=159))
```

<a id="dquote.DQuote.query_index_data"></a>

#### query\_index\_data

```python
def query_index_data(productid) -> DIndexDataResponse
```

查詢現貨成交價
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |

##### 回傳值 DIndexDataResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | DIndexData | 現貨成交價  |

##### 範例
```python 
response = unitrade.dquote.query_index_data("TXF")
# DIndexDataResponse(ok=True, error='', data=DIndexData(index_kind='TXF', index_time='133325000000', index_value=22003.5))
```

<a id="dquote.DQuote.query_tick_data_bid_offer"></a>

#### query\_tick\_data\_bid\_offer

```python
def query_tick_data_bid_offer(productid) -> DTickDataBidOfferResponse
```

查詢最後五檔
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |

##### 回傳值 DTickDataBidOfferResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | DTickDataBidOffer | 最後五檔  |

##### 範例
```python 
response = unitrade.dquote.query_tick_data_bid_offer("TXFG5")
# DTickDataBidOfferResponse(ok=True, error='', data=DTickDataBidOffer(commodityid='TXFG5', bp1=21704.0, bp2=21703.0, bp3=21702.0, bp4=21701.0, bp5=21700.0, bq1=5, bq2=3, bq3=7, bq4=3, bq5=5, sp1=21706.0, sp2=21708.0, sp3=21709.0, sp4=21710.0, sp5=21711.0, sq1=4, sq2=1, sq3=3, sq4=12, sq5=16))
```

<a id="dquote.DQuote.query_tick_data_before_bid_offer"></a>

#### query\_tick\_data\_before\_bid\_offer

```python
def query_tick_data_before_bid_offer(
        productid) -> DTickDataBeforeBidOfferResponse
```

查詢最後盤前五檔
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |

##### 回傳值 DTickDataBeforeBidOfferResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | DTickDataBeforeBidOffer | 最後盤前五檔  |

##### 範例
```python
response = unitrade.dquote.query_tick_data_before_bid_offer("TXFG5")
# DTickDataBeforeBidOfferResponse(ok=True, error='', data=DTickDataBeforeBidOffer(commodityid='TXFG5', bp1=21810.0, bp2=21809.0, bp3=21808.0, bp4=21807.0, bp5=21805.0, bq1=1, bq2=5, bq3=2, bq4=3, bq5=3, sp1=21811.0, sp2=21815.0, sp3=21816.0, sp4=21819.0, sp5=21821.0, sq1=1, sq2=10, sq3=1, sq4=1, sq5=1))
```

<a id="dquote.DQuote.subscribe_trade_bid_offer"></a>

#### subscribe\_trade\_bid\_offer

```python
def subscribe_trade_bid_offer(productid) -> Tuple[bool, str]
```

註冊成交.賣賣價量
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |  

##### Returns 

| Type | Description |
| ------ | ------------- |
| bool | 是否成功 |    
| str | 錯誤訊息 |

<a id="dquote.DQuote.unsubscribe_trade_bid_offer"></a>

#### unsubscribe\_trade\_bid\_offer

```python
def unsubscribe_trade_bid_offer(productid) -> Tuple[bool, str]
```

反註冊成交.賣賣價量
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |  

##### Returns 

| Type | Description |
| ------ | ------------- |
| bool | 是否成功 |    
| str | 錯誤訊息 |

<a id="dquote.DQuote.subscribe_high_low"></a>

#### subscribe\_high\_low

```python
def subscribe_high_low(productid) -> Tuple[bool, str]
```

註冊最高最低價
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |  

##### Returns 

| Type | Description |
| ------ | ------------- |
| bool | 是否成功 |    
| str | 錯誤訊息 |

<a id="dquote.DQuote.unsubscribe_high_low"></a>

#### unsubscribe\_high\_low

```python
def unsubscribe_high_low(productid) -> Tuple[bool, str]
```

反註冊最高最低價
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 | 

##### Returns 

| Type | Description |
| ------ | ------------- |
| bool | 是否成功 |    
| str | 錯誤訊息 |

<a id="dquote.DQuote.subscribe_open"></a>

#### subscribe\_open

```python
def subscribe_open(productid) -> Tuple[bool, str]
```

註冊開盤價
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |  

##### Returns 

| Type | Description |
| ------ | ------------- |
| bool | 是否成功 |    
| str | 錯誤訊息 |

<a id="dquote.DQuote.unsubscribe_open"></a>

#### unsubscribe\_open

```python
def unsubscribe_open(productid) -> Tuple[bool, str]
```

反註冊開盤價
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| productid | str | 商品代碼 |  

##### Returns 

| Type | Description |
| ------ | ------------- |
| bool | 是否成功 |    
| str | 錯誤訊息 |

<a id="dquote.DQuote.subscribe_index_data"></a>

#### subscribe\_index\_data

```python
def subscribe_index_data(kind, index) -> Tuple[bool, str]
```

註冊現貨價
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| index | str | 商品代碼 |    

##### Returns 

| Type | Description |
| ------ | ------------- |
| bool | 是否成功 |    
| str | 錯誤訊息 |

<a id="dquote.DQuote.unsubscribe_index_data"></a>

#### unsubscribe\_index\_data

```python
def unsubscribe_index_data(kind, index) -> Tuple[bool, str]
```

反註冊現貨價
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| index | str | 商品代碼 |    

##### Returns 

| Type | Description |
| ------ | ------------- |
| bool | 是否成功 |    
| str | 錯誤訊息 |

<a id="dquote.DQuote.close"></a>

#### close

```python
def close()
```

關閉物件

<a id="dquote.Format"></a>

## Format Objects

```python
class Format()
```

<a id="dquote.Format.I020_HEAD"></a>

#### I020\_HEAD

成交價揭示

<a id="dquote.Format.I021_HEAD"></a>

#### I021\_HEAD

最高最低價揭示

<a id="dquote.Format.I022_HEAD"></a>

#### I022\_HEAD

盤前揭示成交價揭示

<a id="dquote.Format.I023_HEAD"></a>

#### I023\_HEAD

定時開盤價量揭示

<a id="dquote.Format.I060_HEAD"></a>

#### I060\_HEAD

現貨價

<a id="dquote.Format.I080_HEAD"></a>

#### I080\_HEAD

委託簿揭示

<a id="dquote.Format.I082_HEAD"></a>

#### I082\_HEAD

盤前委託簿揭示

<a id="dquote.Format.I020"></a>

#### I020

成交價揭示

<a id="dquote.Format.I021"></a>

#### I021

最高最低價揭示

<a id="dquote.Format.I022"></a>

#### I022

盤前揭示成交價揭示

<a id="dquote.Format.I023"></a>

#### I023

定時開盤價量揭示

<a id="dquote.Format.I060"></a>

#### I060

現貨價

<a id="dquote.Format.I080"></a>

#### I080

委託簿揭示

<a id="dquote.Format.I082"></a>

#### I082

盤前委託簿揭示

<a id="dquote.Format.X010"></a>

#### X010

商品基本資料訊息

<a id="dquote.Format.X020"></a>

#### X020

成交價量揭示訊息

<a id="dquote.Format.X021"></a>

#### X021

盤中最高低價揭示訊息

<a id="dquote.Format.X060"></a>

#### X060

現貨標的資訊

<a id="dquote.Format.X080"></a>

#### X080

委託簿揭示訊息

