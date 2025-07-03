---  
nav_order: 18
parent: API Reference  
title: "squote"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
現貨行情
註冊接收即時和查詢

<a id="squote.SQuote"></a>

## SQuote Objects

```python
class SQuote()
```

<a id="squote.SQuote.on_error"></a>

#### on\_error

錯誤事件

<a id="squote.SQuote.on_connected"></a>

#### on\_connected

連線成功事件

<a id="squote.SQuote.on_disonnected"></a>

#### on\_disonnected

斷線事件

<a id="squote.SQuote.on_base_data"></a>

#### on\_base\_data

普通個股基本資料事件..傳入物件:BaseData

<a id="squote.SQuote.on_tick_data"></a>

#### on\_tick\_data

普通股競價交易即時行情資訊事件..傳入物件:TickData

<a id="squote.SQuote.on_tick_data_open_close"></a>

#### on\_tick\_data\_open\_close

普通股競價交易開(收)盤價資料事件..傳入物件:TickDataOpenclose

<a id="squote.SQuote.on_index_data"></a>

#### on\_index\_data

指數資訊事件..傳入物件:IndexData

<a id="squote.SQuote.on_otc_base_data"></a>

#### on\_otc\_base\_data

上櫃個股基本資料事件..傳入物件:BaseData

<a id="squote.SQuote.on_otc_tick_data"></a>

#### on\_otc\_tick\_data

上櫃股競價交易即時行情資訊事件..傳入物件:TickData

<a id="squote.SQuote.on_otc_tick_data_open_close"></a>

#### on\_otc\_tick\_data\_open\_close

上櫃股競價交易開(收)盤價資料事件..傳入物件:TickDataOpenclose

<a id="squote.SQuote.on_otc_index_data"></a>

#### on\_otc\_index\_data

櫃買指數資訊事件..傳入物件:IndexData

<a id="squote.SQuote.get_current_server"></a>

#### get\_current\_server

```python
def get_current_server()
```

目前連結主機
##### 回傳值 str 
##### 範例
```python
server = unitrade.squote.get_current_server()
print(server)  # 輸出目前連結的主機 
```

<a id="squote.SQuote.get_server_list"></a>

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
server_list = unitrade.squote.get_server_list()
for servername, server in server_list.items():
    print(f'主機名稱: {servername})
```

<a id="squote.SQuote.set_sever_by_name"></a>

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
success = unitrade.squote.set_sever_by_name("xxx")
if success:
    print("連線成功")
else:
    print("連線失敗")
```

<a id="squote.SQuote.get_subscribe"></a>

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
subscribes = unitrade.squote.get_subscribe()
```

<a id="squote.SQuote.query_base_data"></a>

#### query\_base\_data

```python
def query_base_data(item) -> BaseDataResponse
```

查詢普通個股基本資料
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 BaseDataResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | BaseData | 基本資料物件 |

##### 範例
```python
response = unitrade.squote.query_base_data("2330")
# BaseDataResponse(ok=True, error='', data=BaseData(stock_code='2330', product_name='台積電          ', industry='24', security_type='  ', stock_abnormal_code='0', reference_price='1055.0000', upper_limit_price='1160.0000', lower_limit_price='950.0000', non_10_denomination=' ', abnormal_recommendation_note=' ', special_abnormal_security_note=' ', day_trading_note='A', exempt_short_selling_note='Y', exempt_borrowing_short_selling_note='Y', matching_cycle_seconds='0', foreign_stock_identifier=' ', trading_unit='1000', trading_currency_code='   '))
```

<a id="squote.SQuote.query_tick_data"></a>

#### query\_tick\_data

```python
def query_tick_data(item) -> TickDataResponse
```

查詢最後普通股競價交易即時行情資訊
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 TickDataResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | TickData | 即時行情資訊 |

##### 範例
```python
response = unitrade.squote.query_tick_data("2330")
# TickDataResponse(ok=True, error='', data=TickData(stock_code='2330', match_time='133000000000', limit_up_down_note='0', status_note='4', cumulative_volume=23904, trade_price=1035.0, trade_volume=2334, best_bid_price_1=1035.0, best_bid_volume_1=107, best_bid_price_2=1030.0, best_bid_volume_2=3831, best_bid_price_3=1025.0, best_bid_volume_3=2908, best_bid_price_4=1020.0, best_bid_volume_4=2494, best_bid_price_5=1015.0, best_bid_volume_5=637, best_ask_price_1=1040.0, best_ask_volume_1=3303, best_ask_price_2=1045.0, best_ask_volume_2=2110, best_ask_price_3=1050.0, best_ask_volume_3=1475, best_ask_price_4=1055.0, best_ask_volume_4=1123, best_ask_price_5=1060.0, best_ask_volume_5=1694))
```

<a id="squote.SQuote.query_tick_open_close"></a>

#### query\_tick\_open\_close

```python
def query_tick_open_close(item) -> TickDataOpenCloseResponse
```

查詢最後普通股競價交易開(收)盤價資料資訊
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 TickDataOpenCloseResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | TickDataOpenClose | 開(收)盤價資料資訊 |

##### 範例
```python
response = unitrade.squote.query_tick_open_close("2330")
# TickDataOpenCloseResponse(ok=True, error='', data=TickDataOpenClose(stock_code='2330', open_price=1045.0, high_price=1045.0, low_price=1030.0, last_trade_price=1035.0, cumulative_volume=23904, time='999999999999'))
```

<a id="squote.SQuote.query_otc_base_data"></a>

#### query\_otc\_base\_data

```python
def query_otc_base_data(item) -> OTCBaseDataResponse
```

查詢otc普通個股基本資料
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 OTCBaseDataResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | OTCBaseData | otc普通個股基本資料 |

##### 範例
```python
response = unitrade.squote.query_otc_base_data("5483")
# OTCBaseDataResponse(ok=True, error='', data=OTCBaseData(stock_code='5483', product_name='中美晶          ', industry='24', security_type='  ', stock_abnormal_code='0', stock_type='48', reference_price='94.2000', upper_limit_price='103.5000', lower_limit_price='84.8000', non_10_denomination=' ', abnormal_recommendation_note=' ', special_abnormal_security_note=' ', day_trading_note='A', exempt_short_selling_note='Y', exempt_borrowing_short_selling_note='Y', matching_cycle_seconds='0', trading_unit='1000', trading_currency_code='   '))
```

<a id="squote.SQuote.query_otc_tick_data"></a>

#### query\_otc\_tick\_data

```python
def query_otc_tick_data(item) -> TickDataResponse
```

查詢otc最後普通股競價交易即時行情資訊
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 TickDataResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | TickData | 即時行情資訊 |

##### 範例
```python
response = unitrade.squote.query_otc_tick_data("5483")
# TickDataResponse(ok=True, error='', data=TickData(stock_code='5483', match_time='133000000000', limit_up_down_note='0', status_note='4', cumulative_volume=4174, trade_price=91.2, trade_volume=359, best_bid_price_1=91.2, best_bid_volume_1=35, best_bid_price_2=91.1, best_bid_volume_2=54, best_bid_price_3=91.0, best_bid_volume_3=178, best_bid_price_4=90.9, best_bid_volume_4=33, best_bid_price_5=90.8, best_bid_volume_5=34, best_ask_price_1=91.3, best_ask_volume_1=7, best_ask_price_2=91.5, best_ask_volume_2=5, best_ask_price_3=91.6, best_ask_volume_3=2, best_ask_price_4=91.7, best_ask_volume_4=21, best_ask_price_5=91.8, best_ask_volume_5=13))  
```

<a id="squote.SQuote.query_otc_tick_open_close"></a>

#### query\_otc\_tick\_open\_close

```python
def query_otc_tick_open_close(item) -> TickDataOpenCloseResponse
```

查詢otc最後普通股競價交易開(收)盤價資料資訊
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 TickDataOpenCloseResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | TickDataOpenClose | 開(收)盤價資料資訊 |

##### 範例
```python
response = unitrade.squote.query_otc_tick_open_close("5483")
# TickDataOpenCloseResponse(ok=True, error='', data=TickDataOpenClose(stock_code='5483', open_price=93.8, high_price=94.2, low_price=91.2, last_trade_price=91.2, cumulative_volume=4174, time='999999999999'))
```

<a id="squote.SQuote.query_index_data"></a>

#### query\_index\_data

```python
def query_index_data(item) -> IndexDataResponse
```

查詢最後指數資料資訊
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 IndexDataResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | IndexData | 最後指數資料資訊 |

##### 範例
```python
response = unitrade.squote.query_index_data("IX0001")
# IndexDataResponse(ok=True, error='', data=IndexData(index_code='IX0001', index_time='999999', latest_index=22003.5))
```

<a id="squote.SQuote.query_otc_index_data"></a>

#### query\_otc\_index\_data

```python
def query_otc_index_data(item) -> IndexDataResponse
```

查詢最後櫃買指數資料資訊
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 IndexDataResponse

| 型別 | 說明 |
| ------ | ------------- |
| ok | bool | 是否成功 |
| error | str | 錯誤訊息 |
| data | IndexData | 最後指數資料資訊 |

##### 範例
```python
response = unitrade.squote.query_otc_index_data("IX0043")
# IndexDataResponse(ok=True, error='', data=IndexData(index_code='IX0043', index_time='999999', latest_index=228.56))
```

<a id="squote.SQuote.sub_stock"></a>

#### sub\_stock

```python
def sub_stock(item: str) -> Tuple[bool, str]
```

註冊股票行情
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 Tuple[bool, str]  

| 型別 | 說明 |
| ------ | ------------- |
| bool | 是否成功 |
| str | 錯誤訊息 |

##### 範例
```python
success, error = unitrade.squote.sub_stock("2330")
if success:
    print("註冊成功")
else:
    print(f"註冊失敗: {error}")
```

<a id="squote.SQuote.unsub_stock"></a>

#### unsub\_stock

```python
def unsub_stock(item: str) -> Tuple[bool, str]
```

反註冊
##### 參數 

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |

##### 回傳值 Tuple[bool, str]  

| 型別 | 說明 |
| ------ | ------------- |
| bool | 是否成功 |
| str | 錯誤訊息 |

##### 範例
```python
success, error = unitrade.squote.unsub_stock("2330")
if success:
    print("反註冊成功")
else:
    print(f"反註冊失敗: {error}")
```

<a id="squote.SQuote.sub_otc"></a>

#### sub\_otc

```python
def sub_otc(item: str) -> Tuple[bool, str]
```

註冊otc行情
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |     

##### Returns 

| Type | Description |
|------|-------------|
|bool|是否成功|    
|str|錯誤訊息|

<a id="squote.SQuote.unsub_otc"></a>

#### unsub\_otc

```python
def unsub_otc(item: str) -> Tuple[bool, str]
```

反註冊
##### Parameters  

| Name | Type | Description |
| ------ | ------ | ------------- |
| item | str | 股票代碼 |     

##### Returns 

| Type | Description |
|------|-------------|
|bool|是否成功|    
|str|錯誤訊息|

<a id="squote.SQuote.sub_index"></a>

#### sub\_index

```python
def sub_index(item: str) -> Tuple[bool, str]
```

註冊指數資訊
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| item | str | 指數代碼 |     

| 指數名稱 | 指數代碼 |     
| ------ | ------ |
| 臺股指數 | IX0001 |
| 臺灣50指數 | TW50 |
| 臺灣中型100指數 | TWMC |
| 臺灣資訊科技指數 | TWIT |
| 臺灣發達指數 | TWEI |
| 臺灣高股息指數 | TWDP |
| 臺灣就業99指數 | EMP99 |
| 臺灣公司治理100指數 | CG100 |
| 寶島股價指數 | FRMSA |
| 臺灣高薪100指數 | HC100 |
| 電子類兩倍槓桿指數 | EDRL2 |
| 電子類反向指數 | EDRIN |
| 臺指日報酬兩倍指數 | TTDRL2 |
| 臺指反向一倍指數 | TTDRIN |
| 小型股300指數 | SC300 |
| 金融類日報酬兩倍指數 | FDRL2 |
| 金融類日報酬反向一倍指數 | FDRIN |
| 漲升股利150指數 | DVA150 |
| 漲升股利100指數 | DVA100 |
| 藍籌30指數 | BC30 |
| 工業菁英30指數 | INE30 |
| 電子菁英30指數 | ITE30 |
| 低波動精選30指數 | LV30 |
| 低貝塔100指數 | LB100 |
| 藍籌30反向一倍指數 | BC30-1 |
| 中小型精選50指數 | SMC50 |
| 中小型A級動能50指數 | SAM50 |
| 臺灣永續指數 | F4GTTE |
| 股利150報酬指數 | IR0091 |
| 電子菁英30報酬指數 | IR0095 |
| 存股雙十等權重報酬指數 | IR0112 |
| 特選大蘋果報酬指數 | IR0113 |
| 中小型300報酬指數 | IR0114 |
| 特股高息20報酬指數 | IR0115 |
| 臺灣500報酬指數 | IR0116 |
| 特選外資豐擁50報酬指數 | IR0117 |
| 臺灣生技指數 | IX0103 |
| 特選高息低波指數 | IX0104 |
| 工業菁英30反向一倍指數 | IX0106 |
| 特選內需高收益指數 | IX0107 |
| 臺灣中小型公司治理指數 | IX0108 |
| 臺灣IPO指數 | IX0109 |
| 價值投資指數 | IX0110 |
| 中小型300指數 | IX0114 |

##### Returns 

| Type | Description |
|------|-------------|
|bool|是否成功|    
|str|錯誤訊息|

<a id="squote.SQuote.unsub_index"></a>

#### unsub\_index

```python
def unsub_index(item: str) -> Tuple[bool, str]
```

反註冊指數資訊
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| item | str | 指數代碼 |     

| 指數名稱 | 指數代碼 |     
| ------ | ------ |
| 臺股指數 | IX0001 |
| 臺灣50指數 | TW50 |
| 臺灣中型100指數 | TWMC |
| 臺灣資訊科技指數 | TWIT |
| 臺灣發達指數 | TWEI |
| 臺灣高股息指數 | TWDP |
| 臺灣就業99指數 | EMP99 |
| 臺灣公司治理100指數 | CG100 |
| 寶島股價指數 | FRMSA |
| 臺灣高薪100指數 | HC100 |
| 電子類兩倍槓桿指數 | EDRL2 |
| 電子類反向指數 | EDRIN |
| 臺指日報酬兩倍指數 | TTDRL2 |
| 臺指反向一倍指數 | TTDRIN |
| 小型股300指數 | SC300 |
| 金融類日報酬兩倍指數 | FDRL2 |
| 金融類日報酬反向一倍指數 | FDRIN |
| 漲升股利150指數 | DVA150 |
| 漲升股利100指數 | DVA100 |
| 藍籌30指數 | BC30 |
| 工業菁英30指數 | INE30 |
| 電子菁英30指數 | ITE30 |
| 低波動精選30指數 | LV30 |
| 低貝塔100指數 | LB100 |
| 藍籌30反向一倍指數 | BC30-1 |
| 中小型精選50指數 | SMC50 |
| 中小型A級動能50指數 | SAM50 |
| 臺灣永續指數 | F4GTTE |
| 股利150報酬指數 | IR0091 |
| 電子菁英30報酬指數 | IR0095 |
| 存股雙十等權重報酬指數 | IR0112 |
| 特選大蘋果報酬指數 | IR0113 |
| 中小型300報酬指數 | IR0114 |
| 特股高息20報酬指數 | IR0115 |
| 臺灣500報酬指數 | IR0116 |
| 特選外資豐擁50報酬指數 | IR0117 |
| 臺灣生技指數 | IX0103 |
| 特選高息低波指數 | IX0104 |
| 工業菁英30反向一倍指數 | IX0106 |
| 特選內需高收益指數 | IX0107 |
| 臺灣中小型公司治理指數 | IX0108 |
| 臺灣IPO指數 | IX0109 |
| 價值投資指數 | IX0110 |
| 中小型300指數 | IX0114 |

##### Returns 

| Type | Description |
|------|-------------|
|bool|是否成功|    
|str|錯誤訊息|

<a id="squote.SQuote.sub_otc_index"></a>

#### sub\_otc\_index

```python
def sub_otc_index(item: str) -> Tuple[bool, str]
```

註冊櫃買指數資訊
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| item | str | 指數代碼 |     

| 指數名稱 | 指數代碼 |     
| ------ | ------ |
| 櫃買指數 | IX0043 |
| 富櫃五十指數 | GTSM50 |
| 指標公債指數 | TWTBI |
| 線上遊戲業指數 | GAME |
| 高殖利率指數 | GTHD |
| 勞工就業88指數 | EMP88 |
| 櫃買薪酬指數 | GTCI |
| 櫃買公司治理指數 | TPCGI |
| 富櫃200報酬指數 | IR0118 |
| 臺灣生技指數 | IX0103 |
| 臺灣中小型公司治理指數 | IX0108 |
| 臺灣IPO指數 | IX0109 |
| 富櫃200指數 | IX0118 |

##### Returns 

| Type | Description |
|------|-------------|
|bool|是否成功|    
|str|錯誤訊息|

<a id="squote.SQuote.unsub_otc_index"></a>

#### unsub\_otc\_index

```python
def unsub_otc_index(item: str) -> Tuple[bool, str]
```

反註冊櫃買指數資訊
##### Parameters 

| Name | Type | Description |
| ------ | ------ | ------------- |
| item | str | 指數代碼 |     

| 指數名稱 | 指數代碼 |     
| ------ | ------ |
| 櫃買指數 | IX0043 |
| 富櫃五十指數 | GTSM50 |
| 指標公債指數 | TWTBI |
| 線上遊戲業指數 | GAME |
| 高殖利率指數 | GTHD |
| 勞工就業88指數 | EMP88 |
| 櫃買薪酬指數 | GTCI |
| 櫃買公司治理指數 | TPCGI |
| 富櫃200報酬指數 | IR0118 |
| 臺灣生技指數 | IX0103 |
| 臺灣中小型公司治理指數 | IX0108 |
| 臺灣IPO指數 | IX0109 |
| 富櫃200指數 | IX0118 |

##### Returns 

| Type | Description |
|------|-------------|
|bool|是否成功|    
|str|錯誤訊息|

<a id="squote.SQuote.close"></a>

#### close

```python
def close()
```

關閉物件

<a id="squote.Format"></a>

## Format Objects

```python
class Format()
```

<a id="squote.Format.Data01"></a>

#### Data01

集中市場普通股個股基本資料

<a id="squote.Format.Data03"></a>

#### Data03

集中市場普通股競價交易指數統計資料

<a id="squote.Format.Data06"></a>

#### Data06

集中市場普通股競價交易即時行情資訊

<a id="squote.Format.Data10"></a>

#### Data10

新編臺灣指數資料

<a id="squote.Format.Data12"></a>

#### Data12

集中市場普通股競價交易開(收)盤價資料

<a id="squote.Format.OTC_Data01"></a>

#### OTC\_Data01

上櫃股票個股基本資料

<a id="squote.Format.OTC_Data03"></a>

#### OTC\_Data03

上櫃股票等價交易指數統計資料

<a id="squote.Format.OTC_Data06"></a>

#### OTC\_Data06

上櫃股票等價交易即時行情資訊

<a id="squote.Format.OTC_Data11"></a>

#### OTC\_Data11

上櫃股票等價交易個股開收盤價資料

<a id="squote.Format.OTC_Data12"></a>

#### OTC\_Data12

新編櫃買指數資料

