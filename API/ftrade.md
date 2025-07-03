---  
nav_order: 8
parent: API Reference
title: "ftrade"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
外期交易
    負責下單,改單,回報接收,回報查詢

<a id="ftrade.FTrade"></a>

## FTrade Objects

```python
class FTrade()
```

<a id="ftrade.FTrade.on_error"></a>

#### on\_error

錯誤事件

<a id="ftrade.FTrade.on_connected"></a>

#### on\_connected

連線成功事件

<a id="ftrade.FTrade.on_disonnected"></a>

#### on\_disonnected

斷線事件

<a id="ftrade.FTrade.on_reply"></a>

#### on\_reply

回報接收事件..傳入物件:FOrderReply

<a id="ftrade.FTrade.on_match"></a>

#### on\_match

成回接收事件..傳入物件:FOrderReply

<a id="ftrade.FTrade.get_current_server"></a>

#### get\_current\_server

```python
def get_current_server()
```

目前連結主機
##### 回傳值 str 
##### 範例
```python
server = unitrade.ftrade.get_current_server()
print(server)  # 輸出目前連結的主機 
```

<a id="ftrade.FTrade.get_server_list"></a>

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
server_list = unitrade.ftrade.get_server_list()
for servername, server in server_list.items():
    print(f'主機名稱: {servername})
```

<a id="ftrade.FTrade.set_sever_by_name"></a>

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
success = unitrade.ftrade.set_sever_by_name("xxx")
if success:
    print("連線成功")
else:
    print("連線失敗")
```

<a id="ftrade.FTrade.order"></a>

#### order

```python
def order(obj) -> FOrderResponse
```

下單
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| obj | FOrderObject | 下單物件 |

##### 回傳值 FOrderResponse

| 型別 | 說明 |
| ------ | ------------- |
| issend | bool | 是否送出 |
| errorcode |str | 錯誤代碼 |
| errormsg | str | 錯誤訊息 |     
| note | str | 傳入的備註 |
| seq | str | 下單序號 |

##### 範例
```python
# FOrderObject(actno='1234567', subactno='', exchange='CME', symbol='NQ', maturitymonthyear='202406', putorcall='', strikeprice='', symbol2='', maturitymonthyear2='', putorcall2='', strikeprice2='', side1='', side2='', bs='S', ordertype='M', price=0, stopprice=0, orderqty=1, ordercondition='R', opencloseflag='', dtrade='', note='ordertest')
orderresponse=unitrade.ftrade.order(FOrderObject)
# FOrderResponse(issend=True, errorcode='', errormsg='', note='ordertest', seq='AGmb80002')
```

<a id="ftrade.FTrade.replace_order"></a>

#### replace\_order

```python
def replace_order(obj) -> FOrderResponse
```

改單
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| obj | FReplaceObject | 下單物件 |

##### 回傳值 FOrderResponse

| 型別 | 說明 |
| ------ | ------------- |
| issend | bool | 是否送出 |
| errorcode |str | 錯誤代碼 |
| errormsg | str | 錯誤訊息 |     
| note | str | 傳入的備註 |
| seq | str | 下單序號 |

##### 範例        
```python
# FReplaceObject(replacetype='m', actno='1234567', orderno='AGmb80002', ordercondition='R', ordertype='M', price=0, stopprice=0, orderqty=1, note='ordertest')
orderresponse=unitrade.ftrade.replace_order(FReplaceObject)
# FOrderResponse(issend=True, errorcode='', errormsg='', note='ordertest', seq='AGmb80002')
```

<a id="ftrade.FTrade.query_reply"></a>

#### query\_reply

```python
def query_reply(actno, num_of_query, network_id_start, network_id_end,
                begin_order_time, end_order_time) -> FQueryReplyResponse
```

查詢委託回報
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| actno | str | 帳號 |
| networkid_st | str | 網路單號起 |
| networkid_ed | str | 網路單號迄 |
| beginOrderTime | str | 委託時間起 |
| endOrderTime | str | 委託時間迄 |

##### 回傳值 FQueryReplyResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | True 成功 /False 失敗 |
| error | str | 錯誤訊息 |
| data | List[FOrderReply] | 回報集合 |

##### 範例
```python
response = unitrade.ftrade.query_reply('1234567', 10, '', '', '', '')
# FQueryReplyResponse(ok=True, error='', data=[
# FOrderReply(brokerid='F008000', investoracno='1234567', networkid='1J', ordertime='100453124', orderno='C0009', subact='', productkind='1', exchange='CME', symbol='MNQ', maturitymonthyear='202506', putorcall='F', strikeprice='0.0000000', symbol2='', maturitymonthyear2='', putorcall2='', strikeprice2='0.0000000', side1='', side2='', bs='B', ordertype='L', price='21614.7500000', stopprice='0.0000000', orderqty='2', nomatchqty='2', matchqty='0', delqty='0', pricebase='1', ordercondition='R', opencloseflag=' ', ae='F0657', odrsrc='E', odrmedia='', order_src='', tradedate='20250619', note='', op='', aeflag='', loginid='', mdate='06/19/2025 10:04:53', orderstatus='委託成功', statuscode='0000', seq='', rawstatus=None), 
# ..])
```

<a id="ftrade.FTrade.query_match"></a>

#### query\_match

```python
def query_match(actno, num_of_query, network_id_start, network_id_end,
                begin_match_time, end_match_time) -> FQueryMatchResponse
```

查詢成交回報
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| actno | str | 帳號 |
| networkid_st | str | 網路單號起 |
| networkid_ed | str | 網路單號迄 |
| begin_match_time | str | 成交時間起 |
| end_match_time | str | 成交時間迄 |

##### 回傳值 FQueryReplyResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | True 成功 /False 失敗 |
| error | str | 錯誤訊息 |
| data | List[FMatchReply] | 成回集合 |

##### 範例
```python
response = unitrade.ftrade.query_match('1234567', 10, '', '', '', '')
# FQueryMatchResponse(ok=True, error='', data=[
#  FMatchReply(brokerid='F008000', investoracno='1234567', networkid='15N', matchtime='100454169', orderno='C0010', subact='', productkind='', exchange='CME', symbol='MNQ', maturitymonthyear='202506', putorcall='F', strikeprice='0.0000000', symbol2='', maturitymonthyear2='', putorcall2='', strikeprice2='0.0000000', side1='', side2='', bs='B', matchprice='21836.5000000', matchqty='1', matchseq='31iPYtn05f770utMc5NP17', pricebase='1', note='', mdate=''), 
# ..])
```

<a id="ftrade.FTrade.close"></a>

#### close

```python
def close()
```

關閉物件

