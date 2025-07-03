---  
nav_order: 19
parent: API Reference  
title: "squote_data"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
現貨行情物件

<a id="sdata.BaseData"></a>

## BaseData Objects

```python
@dataclass
class BaseData()
```

個股基本資料回覆

<a id="sdata.BaseData.stock_code"></a>

#### stock\_code

股票代號 str

<a id="sdata.BaseData.product_name"></a>

#### product\_name

商品名稱 str

<a id="sdata.BaseData.industry"></a>

#### industry

產業別 str

<a id="sdata.BaseData.security_type"></a>

#### security\_type

證券別 str

<a id="sdata.BaseData.stock_abnormal_code"></a>

#### stock\_abnormal\_code

股票異常代碼 str

<a id="sdata.BaseData.reference_price"></a>

#### reference\_price

參考價 float

<a id="sdata.BaseData.upper_limit_price"></a>

#### upper\_limit\_price

漲停價 float

<a id="sdata.BaseData.lower_limit_price"></a>

#### lower\_limit\_price

跌停價 float

<a id="sdata.BaseData.non_10_denomination"></a>

#### non\_10\_denomination

非10元面額 bool

<a id="sdata.BaseData.abnormal_recommendation_note"></a>

#### abnormal\_recommendation\_note

異常推介個股註記 str

<a id="sdata.BaseData.special_abnormal_security_note"></a>

#### special\_abnormal\_security\_note

特殊異常證券註記 str

<a id="sdata.BaseData.day_trading_note"></a>

#### day\_trading\_note

可現股當沖註記 str

<a id="sdata.BaseData.exempt_short_selling_note"></a>

#### exempt\_short\_selling\_note

豁免平盤下融券賣出註記 str

<a id="sdata.BaseData.exempt_borrowing_short_selling_note"></a>

#### exempt\_borrowing\_short\_selling\_note

豁免平盤下借券賣出註記 str

<a id="sdata.BaseData.matching_cycle_seconds"></a>

#### matching\_cycle\_seconds

撮合循環秒數 int

<a id="sdata.BaseData.foreign_stock_identifier"></a>

#### foreign\_stock\_identifier

外國股票識別碼 str

<a id="sdata.BaseData.trading_unit"></a>

#### trading\_unit

交易單位 int

<a id="sdata.BaseData.trading_currency_code"></a>

#### trading\_currency\_code

交易幣別代號 str

<a id="sdata.OTCBaseData"></a>

## OTCBaseData Objects

```python
@dataclass
class OTCBaseData()
```

上櫃股票個股基本資料

<a id="sdata.OTCBaseData.stock_code"></a>

#### stock\_code

股票代號 str

<a id="sdata.OTCBaseData.product_name"></a>

#### product\_name

商品名稱 str

<a id="sdata.OTCBaseData.industry"></a>

#### industry

產業別 str

<a id="sdata.OTCBaseData.security_type"></a>

#### security\_type

證券別 str

<a id="sdata.OTCBaseData.stock_abnormal_code"></a>

#### stock\_abnormal\_code

股票異常代碼 str

<a id="sdata.OTCBaseData.stock_type"></a>

#### stock\_type

類股註記 str

<a id="sdata.OTCBaseData.reference_price"></a>

#### reference\_price

參考價 float

<a id="sdata.OTCBaseData.upper_limit_price"></a>

#### upper\_limit\_price

漲停價 float

<a id="sdata.OTCBaseData.lower_limit_price"></a>

#### lower\_limit\_price

跌停價 float

<a id="sdata.OTCBaseData.non_10_denomination"></a>

#### non\_10\_denomination

非10元面額 bool

<a id="sdata.OTCBaseData.abnormal_recommendation_note"></a>

#### abnormal\_recommendation\_note

異常推介個股註記 str

<a id="sdata.OTCBaseData.special_abnormal_security_note"></a>

#### special\_abnormal\_security\_note

特殊異常證券註記 str

<a id="sdata.OTCBaseData.day_trading_note"></a>

#### day\_trading\_note

可現股當沖註記 str

<a id="sdata.OTCBaseData.exempt_short_selling_note"></a>

#### exempt\_short\_selling\_note

豁免平盤下融券賣出註記 str

<a id="sdata.OTCBaseData.exempt_borrowing_short_selling_note"></a>

#### exempt\_borrowing\_short\_selling\_note

豁免平盤下借券賣出註記 str

<a id="sdata.OTCBaseData.matching_cycle_seconds"></a>

#### matching\_cycle\_seconds

撮合循環秒數 int

<a id="sdata.OTCBaseData.trading_unit"></a>

#### trading\_unit

交易單位 int

<a id="sdata.OTCBaseData.trading_currency_code"></a>

#### trading\_currency\_code

交易幣別代號 str

<a id="sdata.TickData"></a>

## TickData Objects

```python
@dataclass
class TickData()
```

個股競價交易即時行情資訊

<a id="sdata.TickData.stock_code"></a>

#### stock\_code

股票代號 str

<a id="sdata.TickData.match_time"></a>

#### match\_time

撮合時間 str

<a id="sdata.TickData.limit_up_down_note"></a>

#### limit\_up\_down\_note

漲跌停註記 str (0: 一般 64:跌停成交 128:漲停成交)

<a id="sdata.TickData.status_note"></a>

#### status\_note

狀態註記 str(4:收盤揭示 8:開盤揭示 16:逐筆撮合 32:延後收盤 64:延後開盤 128:試撮揭示 256:集合競價 512:一般揭示)

<a id="sdata.TickData.cumulative_volume"></a>

#### cumulative\_volume

累計成交數量 int

<a id="sdata.TickData.trade_price"></a>

#### trade\_price

成交價 float

<a id="sdata.TickData.trade_volume"></a>

#### trade\_volume

成交量 int

<a id="sdata.TickData.best_bid_price_1"></a>

#### best\_bid\_price\_1

最佳一檔買進價 float

<a id="sdata.TickData.best_bid_volume_1"></a>

#### best\_bid\_volume\_1

最佳一檔買進量 int

<a id="sdata.TickData.best_bid_price_2"></a>

#### best\_bid\_price\_2

最佳二檔買進價 float

<a id="sdata.TickData.best_bid_volume_2"></a>

#### best\_bid\_volume\_2

最佳二檔買進量 int

<a id="sdata.TickData.best_bid_price_3"></a>

#### best\_bid\_price\_3

最佳三檔買進價 float

<a id="sdata.TickData.best_bid_volume_3"></a>

#### best\_bid\_volume\_3

最佳三檔買進量 int

<a id="sdata.TickData.best_bid_price_4"></a>

#### best\_bid\_price\_4

最佳四檔買進價 float

<a id="sdata.TickData.best_bid_volume_4"></a>

#### best\_bid\_volume\_4

最佳四檔買進量 int

<a id="sdata.TickData.best_bid_price_5"></a>

#### best\_bid\_price\_5

最佳五檔買進價 float

<a id="sdata.TickData.best_bid_volume_5"></a>

#### best\_bid\_volume\_5

最佳五檔買進量 int

<a id="sdata.TickData.best_ask_price_1"></a>

#### best\_ask\_price\_1

最佳一檔賣出價 float

<a id="sdata.TickData.best_ask_volume_1"></a>

#### best\_ask\_volume\_1

最佳一檔賣出量 int

<a id="sdata.TickData.best_ask_price_2"></a>

#### best\_ask\_price\_2

最佳二檔賣出價 float

<a id="sdata.TickData.best_ask_volume_2"></a>

#### best\_ask\_volume\_2

最佳二檔賣出量 int

<a id="sdata.TickData.best_ask_price_3"></a>

#### best\_ask\_price\_3

最佳三檔賣出價 float

<a id="sdata.TickData.best_ask_volume_3"></a>

#### best\_ask\_volume\_3

最佳三檔賣出量 int

<a id="sdata.TickData.best_ask_price_4"></a>

#### best\_ask\_price\_4

最佳四檔賣出價 float

<a id="sdata.TickData.best_ask_volume_4"></a>

#### best\_ask\_volume\_4

最佳四檔賣出量 int

<a id="sdata.TickData.best_ask_price_5"></a>

#### best\_ask\_price\_5

最佳五檔賣出價 float

<a id="sdata.TickData.best_ask_volume_5"></a>

#### best\_ask\_volume\_5

最佳五檔賣出量 int

<a id="sdata.TickDataOpenClose"></a>

## TickDataOpenClose Objects

```python
@dataclass
class TickDataOpenClose()
```

個股競價交易開(收)盤價資料

<a id="sdata.TickDataOpenClose.stock_code"></a>

#### stock\_code

股票代號 str

<a id="sdata.TickDataOpenClose.open_price"></a>

#### open\_price

開盤價格 float

<a id="sdata.TickDataOpenClose.high_price"></a>

#### high\_price

最高成交價格 float

<a id="sdata.TickDataOpenClose.low_price"></a>

#### low\_price

最低成交價格 float

<a id="sdata.TickDataOpenClose.last_trade_price"></a>

#### last\_trade\_price

最近成交價 float

<a id="sdata.TickDataOpenClose.cumulative_volume"></a>

#### cumulative\_volume

累計成交量 int

<a id="sdata.TickDataOpenClose.time"></a>

#### time

時間 str

<a id="sdata.IndexData"></a>

## IndexData Objects

```python
@dataclass
class IndexData()
```

指數資料

<a id="sdata.IndexData.index_code"></a>

#### index\_code

指數代號 str

<a id="sdata.IndexData.index_time"></a>

#### index\_time

指數時間 str

<a id="sdata.IndexData.latest_index"></a>

#### latest\_index

最新指數 float

<a id="sdata.BaseDataResponse"></a>

## BaseDataResponse Objects

```python
@dataclass
class BaseDataResponse()
```

查詢個股基本資料回覆物件

<a id="sdata.BaseDataResponse.ok"></a>

#### ok

是否成功 bool

<a id="sdata.BaseDataResponse.error"></a>

#### error

錯誤訊息 str

<a id="sdata.BaseDataResponse.data"></a>

#### data

回覆物件 BaseData

<a id="sdata.TickDataResponse"></a>

## TickDataResponse Objects

```python
@dataclass
class TickDataResponse()
```

查詢個股競價交易即時行情資訊回覆物件

<a id="sdata.TickDataResponse.ok"></a>

#### ok

是否成功 bool

<a id="sdata.TickDataResponse.error"></a>

#### error

錯誤訊息 str

<a id="sdata.TickDataResponse.data"></a>

#### data

回覆物件 TickData

<a id="sdata.TickDataOpenCloseResponse"></a>

## TickDataOpenCloseResponse Objects

```python
@dataclass
class TickDataOpenCloseResponse()
```

查詢個股競價交易開(收)盤價資料回覆物件

<a id="sdata.TickDataOpenCloseResponse.ok"></a>

#### ok

是否成功 bool

<a id="sdata.TickDataOpenCloseResponse.error"></a>

#### error

錯誤訊息 str

<a id="sdata.TickDataOpenCloseResponse.data"></a>

#### data

回覆物件 TickDataOpenClose

<a id="sdata.IndexDataResponse"></a>

## IndexDataResponse Objects

```python
@dataclass
class IndexDataResponse()
```

查詢指數回覆物件

<a id="sdata.IndexDataResponse.ok"></a>

#### ok

是否成功 bool

<a id="sdata.IndexDataResponse.error"></a>

#### error

錯誤訊息 str

<a id="sdata.IndexDataResponse.data"></a>

#### data

回覆物件 IndexData

<a id="sdata.OTCBaseDataResponse"></a>

## OTCBaseDataResponse Objects

```python
@dataclass
class OTCBaseDataResponse()
```

查詢上櫃股票個股基本資料回覆物件

<a id="sdata.OTCBaseDataResponse.ok"></a>

#### ok

是否成功 bool

<a id="sdata.OTCBaseDataResponse.error"></a>

#### error

錯誤訊息 str

<a id="sdata.OTCBaseDataResponse.data"></a>

#### data

回覆物件 OTCBaseData

