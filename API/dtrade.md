---  
nav_order: 6
parent: API Reference  
title: "dtrade"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
內期交易
    負責下單,改單,回報接收,回報查詢

<a id="dtrade.DTrade"></a>

## DTrade Objects

```python
class DTrade()
```

<a id="dtrade.DTrade.on_error"></a>

#### on\_error

錯誤事件

<a id="dtrade.DTrade.on_connected"></a>

#### on\_connected

連線成功事件

<a id="dtrade.DTrade.on_disonnected"></a>

#### on\_disonnected

斷線事件

<a id="dtrade.DTrade.on_reply"></a>

#### on\_reply

回報接收事件..傳入物件:DOrderReply

<a id="dtrade.DTrade.on_match"></a>

#### on\_match

成回接收事件..傳入物件:DOrderReply

<a id="dtrade.DTrade.get_current_server"></a>

#### get\_current\_server

```python
def get_current_server()
```

目前連結主機
##### 回傳值 str 
##### 範例
```python
server = unitrade.dtrade.get_current_server()
print(server)  # 輸出目前連結的主機 
```

<a id="dtrade.DTrade.get_server_list"></a>

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
server_list = unitrade.dtrade.get_server_list()
for servername, server in server_list.items():
    print(f'主機名稱: {servername})
```

<a id="dtrade.DTrade.set_sever_by_name"></a>

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
success = unitrade.dtrade.set_sever_by_name("xxx")
if success:
    print("連線成功")
else:
    print("連線失敗")
```

<a id="dtrade.DTrade.order"></a>

#### order

```python
def order(obj: DOrderObject) -> DOrderResponse
```

下單
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| obj | DOrderObject | 下單物件 |

##### 回傳值 DOrderResponse

| 型別 | 說明 |
| ------ | ------------- |
| issend | bool | 是否送出 |
| errorcode |str | 錯誤代碼 |
| errormsg | str | 錯誤訊息 |     
| note | str | 傳入的備註 |
| seq | str | 下單序號 |

##### 範例
```python
# DOrderObject(actno='1234567', subactno='', productid='TXFF5', bs='B', ordertype='M', price=0, orderqty=5, ordercondition='R', opencloseflag='', dtrade='N', note='ordertest')
orderresponse=unitrade.dtrade.order(DOrderObject)
# DOrderResponse(issend=True, errorcode='', errormsg='', note='ordertest', seq='0002')
```

<a id="dtrade.DTrade.replace_order"></a>

#### replace\_order

```python
def replace_order(obj: DReplaceObject) -> DOrderResponse
```

改單
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| obj | DReplaceObject | 下單物件 |

##### 回傳值 DOrderResponse

| 型別 | 說明 |
| ------ | ------------- |
| issend | bool | 是否送出 |
| errorcode |str | 錯誤代碼 |
| errormsg | str | 錯誤訊息 |     
| note | str | 傳入的備註 |
| seq | str | 下單序號 |

##### 範例
```python
# DReplaceObject(replacetype='5', orderno='A0001', orderqty=1, actno='1234567', note='ordertest')
response=unitrade.dtrade.replace_order(DReplaceObject)
# DOrderResponse(issend=True, errorcode='', errormsg='', note='ordertest', seq='0002')
```

<a id="dtrade.DTrade.query_reply"></a>

#### query\_reply

```python
def query_reply(actno, num_of_query, network_id_start, network_id_end,
                begin_order_time, end_order_time) -> DQueryReplyResponse
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

##### 回傳值 QueryReplyResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | True 成功 /False 失敗 |
| error | str | 錯誤訊息 |
| data | List[OrderReply] | 回報集合 |

##### 範例
```python
response = unitrade.dtrade.query_reply('1234567', 10, '', '', '', '')
# DQueryReplyResponse(ok=True, error='', data=[
#  DOrderReply(brokerid='F008000', investoracno='1234567', networkid='2500000001', ordertime='100439030', orderno='aa001', subact='', productkind='1', productid='TMFG5', bs='B', ordertype='L', price='21730.0000', orderqty='1', nomatchqty='0', matchqty='0', delqty='0', ordercondition='R', opencloseflag='', ae='', odrsrc='Y', odrmedia='', order_src='M', tradedate='20250619', note='', op='', aeflag=None, loginid=None, mdate='2025/06/19 10:04:39', orderstatus='TTO0002:尚未開始接收委託或者不接受此種委託', statuscode='9902', seq='19        ', rawstatus=None),            
# ..])
```

<a id="dtrade.DTrade.query_match"></a>

#### query\_match

```python
def query_match(actno, num_of_query, network_id_start, network_id_end,
                begin_match_time, end_match_time) -> DQueryMatchResponse
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

##### 回傳值 QueryReplyResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok|bool | True 成功 /False 失敗 |
| error | str | 錯誤訊息 |
| data | List[MatchReply] | 成回集合 |

##### 範例
```python
response = unitrade.dtrade.query_match('1234567', 10, '', '', '', '')
# DQueryMatchResponse(ok=True, error='', data=[
#  DMatchReply(brokerid='F008000', investoracno='1234567', networkid='2500000001', matchtime='100439030', orderno='aa001', subact='', productkind='1', productid='TMFG5', bs='B', matchprice='21730.0000', matchqty='1', matchseq='', matchpricefoot1='', matchpricefoot2='', note=''),
# ..])
```

<a id="dtrade.DTrade.close"></a>

#### close

```python
def close()
```

關閉物件

