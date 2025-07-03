---  
nav_order: 16
parent: API Reference  
title: "fquote"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
外期行情
註冊接收即時和查詢

<a id="fquote.FQuote"></a>

## FQuote Objects

```python
class FQuote()
```

<a id="fquote.FQuote.on_error"></a>

#### on\_error

錯誤事件

<a id="fquote.FQuote.on_connected"></a>

#### on\_connected

連線成功事件

<a id="fquote.FQuote.on_disonnected"></a>

#### on\_disonnected

斷線事件

<a id="fquote.FQuote.on_tick_data_trade"></a>

#### on\_tick\_data\_trade

成交價事件..傳入物件:FTickDataTrade

<a id="fquote.FQuote.on_tick_data_bid"></a>

#### on\_tick\_data\_bid

最佳買價量事件..傳入物件:FTickDataBid

<a id="fquote.FQuote.on_tick_data_offer"></a>

#### on\_tick\_data\_offer

最佳賣價量事件..傳入物件:FTickDataOffer

<a id="fquote.FQuote.on_tick_data_implied"></a>

#### on\_tick\_data\_implied

隱含價事件..傳入物件:FTickDataImplied

<a id="fquote.FQuote.on_tick_data_high_low"></a>

#### on\_tick\_data\_high\_low

最高最低價事件..傳入物件:FTickDataHighLow

<a id="fquote.FQuote.on_tick_data_open_close"></a>

#### on\_tick\_data\_open\_close

開盤價事件..傳入物件:FTickDataOpenclose

<a id="fquote.FQuote.on_tick_data_settle"></a>

#### on\_tick\_data\_settle

結算價事件..傳入物件:FTickDataOpen

<a id="fquote.FQuote.get_current_server"></a>

#### get\_current\_server

```python
def get_current_server()
```

目前連結主機
##### 回傳值 str 
##### 範例
```python
server = unitrade.fquote.get_current_server()
print(server)  # 輸出目前連結的主機 
```

<a id="fquote.FQuote.get_server_list"></a>

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
server_list = unitrade.fquote.get_server_list()
for servername, server in server_list.items():
    print(f'主機名稱: {servername})
```

<a id="fquote.FQuote.set_sever_by_name"></a>

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
success = unitrade.fquote.set_sever_by_name("xxx")
if success:
    print("連線成功")
else:
    print("連線失敗")
```

<a id="fquote.FQuote.get_subscribe"></a>

#### get\_subscribe

```python
def get_subscribe()
```

查詢已註冊商品
##### 回傳值 list[str]

| 型別 | 說明 |
| ------ | ------------- |
| list | 註冊商品清單 |

##### 範例
```python
subscribes = unitrade.fquote.get_subscribe()
```

<a id="fquote.FQuote.query_tick_data_trade"></a>

#### query\_tick\_data\_trade

```python
def query_tick_data_trade(exchange, symbol, ym, strike,
                          cp) -> FTickDataTradeResponse
```

查詢最後成交價量
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| exchange | str | 交易所 |
| symbol | str | 商品代號 |
| ym | str | 年月 |
| cp | str | CP |
| strike | str | 履約價 |

##### 回傳值 FTickDataTradeResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | FTickDataTrade | 成交價量資料 |

##### 範例
```python
response = unitrade.fquote.query_tick_data_trade("CME", "NQ", "202509", "", "F"))
# FTickDataTradeResponse(ok=True, error='', data=FTickDataTrade(exchage='CME', symbol='NQ', ym='202509', cp='F', strike='', display_denominator=1.0, display_multiply=1.0, total=33017, lastprice=21857.75, lastvolume=1, time='141835084'))
```

<a id="fquote.FQuote.query_tick_data_bid"></a>

#### query\_tick\_data\_bid

```python
def query_tick_data_bid(exchange, symbol, ym, strike,
                        cp) -> FTickDataBidResponse
```

查詢最佳買進報價
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| exchange | str | 交易所 |
| symbol | str | 商品代號 |    
| ym | str | 年月 |
| cp | str | CP |  
| strike | str | 履約價 |

##### 回傳值 FTickDataBidResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | FTickDataBid | 最佳買進報價 |

##### 範例
```python
response = unitrade.fquote.query_tick_data_bid("CME", "NQ", "202509", "", "F")  
# FTickDataBidResponse(ok=True, error='', data=FTickDataBid(exchage='CME', symbol='NQ', ym='202509', cp='F', strike='', display_denominator=1.0, display_multiply=1.0, BidDOM1Price=21846.5, BidDOM1Volume=1, BidDOM2Price=21846.25, BidDOM2Volume=3, BidDOM3Price=21846.0, BidDOM3Volume=4, BidDOM4Price=21845.75, BidDOM4Volume=1, BidDOM5Price=21845.5, BidDOM5Volume=2, BidDOM6Price=21845.25, BidDOM6Volume=2, BidDOM7Price=21845.0, BidDOM7Volume=5, BidDOM8Price=21844.75, BidDOM8Volume=4, BidDOM9Price=21844.25, BidDOM9Volume=5, BidDOM10Price=21844.0, BidDOM10Volume=5))  
```

<a id="fquote.FQuote.query_tick_data_offer"></a>

#### query\_tick\_data\_offer

```python
def query_tick_data_offer(exchange, symbol, ym, strike,
                          cp) -> FTickDataOfferResponse
```

最佳賣出報價
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| exchange | str | 交易所 |
| symbol | str | 商品代號 |
| ym | str | 年月 |
| cp | str | CP |
| strike | str | 履約價 |

##### 回傳值 FTickDataOfferResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | FTickDataOffer | 最佳賣出報價 |

##### 範例
```python        
response = unitrade.fquote.query_tick_data_offer("CME", "NQ", "202509", "", "F")
# FTickDataOfferResponse(ok=True, error='', data=FTickDataOffer(exchage='CME', symbol='NQ', ym='202509', cp='F', strike='', display_denominator=1.0, display_multiply=1.0, OfferDOM1Price=21844.0, OfferDOM1Volume=1, OfferDOM2Price=21844.25, OfferDOM2Volume=2, OfferDOM3Price=21844.5, OfferDOM3Volume=3, OfferDOM4Price=21844.75, OfferDOM4Volume=2, OfferDOM5Price=21845.0, OfferDOM5Volume=1, OfferDOM6Price=21845.25, OfferDOM6Volume=1, OfferDOM7Price=21845.5, OfferDOM7Volume=4, OfferDOM8Price=21845.75, OfferDOM8Volume=1, OfferDOM9Price=21846.0, OfferDOM9Volume=4, OfferDOM10Price=21846.25, OfferDOM10Volume=3))
```

<a id="fquote.FQuote.query_tick_data_implied"></a>

#### query\_tick\_data\_implied

```python
def query_tick_data_implied(exchange, symbol, ym, strike,
                            cp) -> FTickDataImpliedResponse
```

隱含買賣價量
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |  
| exchange | str | 交易所 |
| symbol | str | 商品代號 |    
| ym | str | 年月 |
| cp | str | CP |  
| strike | str | 履約價 |

##### 回傳值 FTickDataImpliedResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | FTickDataImplied | 隱含買賣價量 |

##### 範例
```python        
response = unitrade.fquote.query_tick_data_implied("CME", "NQ", "202509", "", "F")
# FTickDataImpliedResponse(ok=True, error='', data=FTickDataImplied(exchage='CME', symbol='NQ', ym='202509', cp='F', strike='', display_denominator=1.0, display_multiply=1.0, ImpliedBidPrice=0.0, ImpliedBidVolume=0, ImpliedOfferPrice=0.0, ImpliedOfferVolume=0))
```

<a id="fquote.FQuote.query_tick_data_open_close"></a>

#### query\_tick\_data\_open\_close

```python
def query_tick_data_open_close(exchange, symbol, ym, strike,
                               cp) -> FTickDataOpencloseResponse
```

查詢開收盤價
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| exchange | str | 交易所 |
| symbol | str | 商品代號 |
| ym | str | 年月 |
| cp | str | CP |
| strike | str | 履約價 |

##### 回傳值 FTickDataOpencloseResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | FTickDataOpenclose | 開收盤價 |

##### 範例
```python  
response = unitrade.fquote.query_tick_data_open_close("CME", "NQ", "202509", "", "F")
# FTickDataOpencloseResponse(ok=True, error='', data=FTickDataOpenclose(exchage='CME', symbol='NQ', ym='202509', cp='F', strike='', display_denominator=1.0, display_multiply=1.0, Opening=21956.75, Closing=21842.75))
```

<a id="fquote.FQuote.query_tick_data_high_low"></a>

#### query\_tick\_data\_high\_low

```python
def query_tick_data_high_low(exchange, symbol, ym, strike,
                             cp) -> FTickDataHighLowResponse
```

查詢最高最低價
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| exchange | str | 交易所 |
| symbol | str | 商品代號 |
| ym | str | 年月 |
| cp | str | CP |
| strike | str | 履約價 |

##### 回傳值 FTickDataHighLowResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | FTickDataHighLow | 開收盤價 |

##### 範例
```python  
response = unitrade.fquote.query_tick_data_high_low("CME", "NQ", "202509", "", "F")
# FTickDataHighLowResponse(ok=True, error='', data=FTickDataHighLow(exchage='CME', symbol='NQ', ym='202509', cp='F', strike='', display_denominator=1.0, display_multiply=1.0, High=21970.75, Low=21790.0))
```

<a id="fquote.FQuote.query_tick_data_settle"></a>

#### query\_tick\_data\_settle

```python
def query_tick_data_settle(exchange, symbol, ym, strike,
                           cp) -> FTickDataSettleResponse
```

查詢結算價
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| exchange | str | 交易所 |
| symbol | str | 商品代號 |
| ym | str | 年月 |
| cp | str | CP |
| strike | str | 履約價 |

##### 回傳值 FTickDataSettleResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | FTickDataSettle | 結算價 |

##### 範例
```python  
response = unitrade.fquote.query_tick_data_settle("CME", "NQ", "202509", "", "F")
# FTickDataSettleResponse(ok=True, error='', data=FTickDataSettle(exchage='CME', symbol='NQ', ym='202509', cp='F', strike='', display_denominator=1.0, display_multiply=1.0, CurrStl=21945.25, NewStl=21945.25))
```

<a id="fquote.FQuote.subscribe"></a>

#### subscribe

```python
def subscribe(exchange: str, symbol: str, ym: str, cp: str,
              strike: str) -> Tuple[bool, str]
```

註冊
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |   
| exchange | str | 交易所 |
| symbol | str | 商品代號 |
| ym | str | 年月 |
| cp | str | CP |
| strike | str | 履約價 |

##### 回傳值 Tuple[bool, str] 

| 型別 | 說明 |
| ------ | ------------- |
|bool|是否成功|
|str|錯誤訊息|

<a id="fquote.FQuote.unsubscribe"></a>

#### unsubscribe

```python
def unsubscribe(exchange: str, symbol: str, ym: str, cp: str,
                strike: str) -> Tuple[bool, str]
```

反註冊
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |        
| exchange | str | 交易所 |
| symbol | str | 商品代號 |
| ym | str | 年月 |
| cp | str | CP |
| strike | str | 履約價 |

##### 回傳值 Tuple[bool, str]

| 型別 | 說明 |
| ------ | ------------- |
|bool|是否成功|
|str|錯誤訊息|

<a id="fquote.FQuote.close"></a>

#### close

```python
def close()
```

關閉物件

<a id="fquote.Format"></a>

## Format Objects

```python
class Format()
```

<a id="fquote.Format.I020_HEAD"></a>

#### I020\_HEAD

成交價揭示

<a id="fquote.Format.I021_HEAD"></a>

#### I021\_HEAD

最高最低價揭示

<a id="fquote.Format.I022_HEAD"></a>

#### I022\_HEAD

盤前揭示成交價揭示

<a id="fquote.Format.I060_HEAD"></a>

#### I060\_HEAD

現貨價

<a id="fquote.Format.I080_HEAD"></a>

#### I080\_HEAD

委託簿揭示

<a id="fquote.Format.I082_HEAD"></a>

#### I082\_HEAD

盤前委託簿揭示

<a id="fquote.Format.TICKDATATRADE"></a>

#### TICKDATATRADE

即時成交價量

<a id="fquote.Format.TICKDATABID"></a>

#### TICKDATABID

即時最佳買進報價

<a id="fquote.Format.TICKDATAOFFER"></a>

#### TICKDATAOFFER

即時最佳賣出報價

<a id="fquote.Format.TICKDATAIMPLIED"></a>

#### TICKDATAIMPLIED

即時隱含買賣價量

<a id="fquote.Format.TICKDATAHIGHLOW"></a>

#### TICKDATAHIGHLOW

即時最高最低價

<a id="fquote.Format.TICKDATAOPENCLOSE"></a>

#### TICKDATAOPENCLOSE

即時開收盤價

<a id="fquote.Format.TICKDATASETTLE"></a>

#### TICKDATASETTLE

即時結算價

