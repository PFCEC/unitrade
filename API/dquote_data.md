---  
nav_order: 15
parent: API Reference  
title: "dquote_data"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
內期行情物件

<a id="ddata.DTickDataTrade"></a>

## DTickDataTrade Objects

```python
@dataclass
class DTickDataTrade()
```

成交價揭示

<a id="ddata.DTickDataTrade.commodityid"></a>

#### commodityid

商品代號 str

<a id="ddata.DTickDataTrade.infotime"></a>

#### infotime

期交所送出時間 str

<a id="ddata.DTickDataTrade.matchprice"></a>

#### matchprice

第一成交價格 float

<a id="ddata.DTickDataTrade.matchquantity"></a>

#### matchquantity

第一成交量 int

<a id="ddata.DTickDataTrade.matchtotalqty"></a>

#### matchtotalqty

成交總量 int

<a id="ddata.DTickDataTrade.matchbuycnt"></a>

#### matchbuycnt

成交買量 int

<a id="ddata.DTickDataTrade.matchsellcnt"></a>

#### matchsellcnt

成交賣量 int

<a id="ddata.DTickDataTrade.matchtime"></a>

#### matchtime

成交時間 str

<a id="ddata.DTickDataTrade.matchpricedata"></a>

#### matchpricedata

第2到第N成交價陣列 List[float]
一筆行情可能會有多筆成交價，此陣列為剩餘所有成交價

<a id="ddata.DTickDataTrade.matchqtydata"></a>

#### matchqtydata

第2到第N成交量陣列 list[int]
一筆行情可能會有多筆成交價，此陣列為剩餘所有成交量

<a id="ddata.DTickDataHighLow"></a>

## DTickDataHighLow Objects

```python
@dataclass
class DTickDataHighLow()
```

最高最低價揭示

<a id="ddata.DTickDataHighLow.commodityid"></a>

#### commodityid

商品代碼 str

<a id="ddata.DTickDataHighLow.showtime"></a>

#### showtime

時間 str

<a id="ddata.DTickDataHighLow.dayhighprice"></a>

#### dayhighprice

最高價 float

<a id="ddata.DTickDataHighLow.daylowprice"></a>

#### daylowprice

最低價 float

<a id="ddata.DTickDataBeforeTrade"></a>

## DTickDataBeforeTrade Objects

```python
@dataclass
class DTickDataBeforeTrade()
```

盤前揭示成交價揭示

<a id="ddata.DTickDataBeforeTrade.commodityid"></a>

#### commodityid

商品代號 str

<a id="ddata.DTickDataBeforeTrade.infotime"></a>

#### infotime

期交所送出時間 str

<a id="ddata.DTickDataBeforeTrade.matchprice"></a>

#### matchprice

成交價格 int

<a id="ddata.DTickDataBeforeTrade.matchquantity"></a>

#### matchquantity

成交量 int

<a id="ddata.DTickDataBeforeTrade.matchtotalqty"></a>

#### matchtotalqty

成交總量 int

<a id="ddata.DTickDataBeforeTrade.matchbuycnt"></a>

#### matchbuycnt

成交買量 int

<a id="ddata.DTickDataBeforeTrade.matchsellcnt"></a>

#### matchsellcnt

成交賣量 int

<a id="ddata.DTickDataBeforeTrade.matchtime"></a>

#### matchtime

成交時間 str

<a id="ddata.DIndexData"></a>

## DIndexData Objects

```python
@dataclass
class DIndexData()
```

現貨價

<a id="ddata.DIndexData.index_kind"></a>

#### index\_kind

現貨代碼 str

<a id="ddata.DIndexData.index_time"></a>

#### index\_time

現貨統計時間 str

<a id="ddata.DIndexData.index_value"></a>

#### index\_value

現貨價 float

<a id="ddata.DTickDataBidOffer"></a>

## DTickDataBidOffer Objects

```python
@dataclass
class DTickDataBidOffer()
```

委託簿揭示

<a id="ddata.DTickDataBidOffer.commodityid"></a>

#### commodityid

商品代碼 str

<a id="ddata.DTickDataBidOffer.bp1"></a>

#### bp1

第一檔委買價格 float

<a id="ddata.DTickDataBidOffer.bp2"></a>

#### bp2

第二檔委買價格 float

<a id="ddata.DTickDataBidOffer.bp3"></a>

#### bp3

第三檔委買價格 float

<a id="ddata.DTickDataBidOffer.bp4"></a>

#### bp4

第四檔委買價格 float

<a id="ddata.DTickDataBidOffer.bp5"></a>

#### bp5

第五檔委買價格 float

<a id="ddata.DTickDataBidOffer.bq1"></a>

#### bq1

第一檔委買數量 int

<a id="ddata.DTickDataBidOffer.bq2"></a>

#### bq2

第二檔委買數量 int

<a id="ddata.DTickDataBidOffer.bq3"></a>

#### bq3

第三檔委買數量 int

<a id="ddata.DTickDataBidOffer.bq4"></a>

#### bq4

第四檔委買數量 int

<a id="ddata.DTickDataBidOffer.bq5"></a>

#### bq5

第五檔委買數量 int

<a id="ddata.DTickDataBidOffer.sp1"></a>

#### sp1

第一檔委賣價格 float

<a id="ddata.DTickDataBidOffer.sp2"></a>

#### sp2

第二檔委賣價格 float

<a id="ddata.DTickDataBidOffer.sp3"></a>

#### sp3

第三檔委賣價格 float

<a id="ddata.DTickDataBidOffer.sp4"></a>

#### sp4

第四檔委賣價格 float

<a id="ddata.DTickDataBidOffer.sp5"></a>

#### sp5

第五檔委賣價格 float

<a id="ddata.DTickDataBidOffer.sq1"></a>

#### sq1

第一檔委買數量 int

<a id="ddata.DTickDataBidOffer.sq2"></a>

#### sq2

第二檔委賣數量 int

<a id="ddata.DTickDataBidOffer.sq3"></a>

#### sq3

第三檔委賣數量 int

<a id="ddata.DTickDataBidOffer.sq4"></a>

#### sq4

第四檔委賣數量 int

<a id="ddata.DTickDataBidOffer.sq5"></a>

#### sq5

第五檔委賣數量 int

<a id="ddata.DTickDataBeforeBidOffer"></a>

## DTickDataBeforeBidOffer Objects

```python
@dataclass
class DTickDataBeforeBidOffer()
```

盤前委託簿揭示

<a id="ddata.DTickDataBeforeBidOffer.commodityid"></a>

#### commodityid

商品代碼 str

<a id="ddata.DTickDataBeforeBidOffer.bp1"></a>

#### bp1

第一檔委買價格 float

<a id="ddata.DTickDataBeforeBidOffer.bp2"></a>

#### bp2

第二檔委買價格 float

<a id="ddata.DTickDataBeforeBidOffer.bp3"></a>

#### bp3

第三檔委買價格 float

<a id="ddata.DTickDataBeforeBidOffer.bp4"></a>

#### bp4

第四檔委買價格 float

<a id="ddata.DTickDataBeforeBidOffer.bp5"></a>

#### bp5

第五檔委買價格 float

<a id="ddata.DTickDataBeforeBidOffer.bq1"></a>

#### bq1

第一檔委買數量 int

<a id="ddata.DTickDataBeforeBidOffer.bq2"></a>

#### bq2

第二檔委買數量 int

<a id="ddata.DTickDataBeforeBidOffer.bq3"></a>

#### bq3

第三檔委買數量 int

<a id="ddata.DTickDataBeforeBidOffer.bq4"></a>

#### bq4

第四檔委買數量 int

<a id="ddata.DTickDataBeforeBidOffer.bq5"></a>

#### bq5

第五檔委買數量 int

<a id="ddata.DTickDataBeforeBidOffer.sp1"></a>

#### sp1

第一檔委賣價格 float

<a id="ddata.DTickDataBeforeBidOffer.sp2"></a>

#### sp2

第二檔委賣價格 float

<a id="ddata.DTickDataBeforeBidOffer.sp3"></a>

#### sp3

第三檔委賣價格 float

<a id="ddata.DTickDataBeforeBidOffer.sp4"></a>

#### sp4

第四檔委賣價格 float

<a id="ddata.DTickDataBeforeBidOffer.sp5"></a>

#### sp5

第五檔委賣價格 float

<a id="ddata.DTickDataBeforeBidOffer.sq1"></a>

#### sq1

第一檔委買數量 int

<a id="ddata.DTickDataBeforeBidOffer.sq2"></a>

#### sq2

第二檔委賣數量 int

<a id="ddata.DTickDataBeforeBidOffer.sq3"></a>

#### sq3

第三檔委賣數量 int

<a id="ddata.DTickDataBeforeBidOffer.sq4"></a>

#### sq4

第四檔委賣數量 int

<a id="ddata.DTickDataBeforeBidOffer.sq5"></a>

#### sq5

第五檔委賣數量 int

<a id="ddata.DTickDataOpen"></a>

## DTickDataOpen Objects

```python
@dataclass
class DTickDataOpen()
```

開盤價揭示

<a id="ddata.DTickDataOpen.commodityid"></a>

#### commodityid

商品代碼

<a id="ddata.DTickDataOpen.opentime"></a>

#### opentime

開盤時間

<a id="ddata.DTickDataOpen.openprice"></a>

#### openprice

開盤價

<a id="ddata.DTickDataOpen.openquantity"></a>

#### openquantity

開盤量

<a id="ddata.DTickDataSettle"></a>

## DTickDataSettle Objects

```python
@dataclass
class DTickDataSettle()
```

收盤行情資料訊息含結算價及未平倉合約數

<a id="ddata.DTickDataSettle.commodityid"></a>

#### commodityid

商品代碼 str

<a id="ddata.DTickDataSettle.period_high_price"></a>

#### period\_high\_price

該期最高價 float

<a id="ddata.DTickDataSettle.period_low_price"></a>

#### period\_low\_price

該期最低價 float

<a id="ddata.DTickDataSettle.daily_high_price"></a>

#### daily\_high\_price

當日最高價 float

<a id="ddata.DTickDataSettle.daily_low_price"></a>

#### daily\_low\_price

當日最低價 float

<a id="ddata.DTickDataSettle.open_price"></a>

#### open\_price

開盤價 float

<a id="ddata.DTickDataSettle.last_bid_price"></a>

#### last\_bid\_price

最後買價 float

<a id="ddata.DTickDataSettle.last_ask_price"></a>

#### last\_ask\_price

最後賣價 float

<a id="ddata.DTickDataSettle.close_price"></a>

#### close\_price

收盤價 float

<a id="ddata.DTickDataSettle.total_bid_orders"></a>

#### total\_bid\_orders

委託買進總筆數 int

<a id="ddata.DTickDataSettle.total_bid_volume"></a>

#### total\_bid\_volume

委託買進總口數 int

<a id="ddata.DTickDataSettle.total_ask_orders"></a>

#### total\_ask\_orders

委託賣出總筆數 int

<a id="ddata.DTickDataSettle.total_ask_volume"></a>

#### total\_ask\_volume

委託賣出總口數 int

<a id="ddata.DTickDataSettle.total_trades"></a>

#### total\_trades

總成交筆數 int

<a id="ddata.DTickDataSettle.total_trade_volume"></a>

#### total\_trade\_volume

總成交口數 int

<a id="ddata.DTickDataSettle.merged_bid_orders"></a>

#### merged\_bid\_orders

合併委託買進總筆數 int

<a id="ddata.DTickDataSettle.merged_bid_volume"></a>

#### merged\_bid\_volume

合併委託買進總口數 int

<a id="ddata.DTickDataSettle.merged_ask_orders"></a>

#### merged\_ask\_orders

合併委託賣出總筆數 int

<a id="ddata.DTickDataSettle.merged_ask_volume"></a>

#### merged\_ask\_volume

合併委託賣出總口數 int

<a id="ddata.DTickDataSettle.merged_volume"></a>

#### merged\_volume

合併總成交量 int

<a id="ddata.DTickDataSettle.settlement_price"></a>

#### settlement\_price

結算價 float

<a id="ddata.DTickDataSettle.open_interest"></a>

#### open\_interest

未平倉合約數 int

<a id="ddata.DTickDataSettle.block_trade_volume"></a>

#### block\_trade\_volume

鉅額交易總成交量 int

<a id="ddata.DTickDataSettleResponse"></a>

## DTickDataSettleResponse Objects

```python
@dataclass
class DTickDataSettleResponse()
```

收盤行情資料訊息含結算價及未平倉合約數回覆物件

<a id="ddata.DTickDataSettleResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DTickDataSettleResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DTickDataSettleResponse.data"></a>

#### data

回覆物件 DTickDataSettle

<a id="ddata.DTickDataTradeResponse"></a>

## DTickDataTradeResponse Objects

```python
@dataclass
class DTickDataTradeResponse()
```

成交價量查詢回覆物件

<a id="ddata.DTickDataTradeResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DTickDataTradeResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DTickDataTradeResponse.data"></a>

#### data

回覆物件 TickDataTrade

<a id="ddata.DTickDataBeforeTradeResponse"></a>

## DTickDataBeforeTradeResponse Objects

```python
@dataclass
class DTickDataBeforeTradeResponse()
```

試撮成交價量查詢回覆物件

<a id="ddata.DTickDataBeforeTradeResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DTickDataBeforeTradeResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DTickDataBeforeTradeResponse.data"></a>

#### data

回覆物件 TickDataBeforeTrade

<a id="ddata.DTickDataHighLowResponse"></a>

## DTickDataHighLowResponse Objects

```python
@dataclass
class DTickDataHighLowResponse()
```

最高最低價查詢回覆物件

<a id="ddata.DTickDataHighLowResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DTickDataHighLowResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DTickDataHighLowResponse.data"></a>

#### data

回覆物件 TickDataHighLow

<a id="ddata.DTickDataOpenResponse"></a>

## DTickDataOpenResponse Objects

```python
@dataclass
class DTickDataOpenResponse()
```

開盤價查詢回覆物件

<a id="ddata.DTickDataOpenResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DTickDataOpenResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DTickDataOpenResponse.data"></a>

#### data

回覆物件 TickDataOpen

<a id="ddata.DIndexDataResponse"></a>

## DIndexDataResponse Objects

```python
@dataclass
class DIndexDataResponse()
```

現貨價格查詢回覆物件

<a id="ddata.DIndexDataResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DIndexDataResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DIndexDataResponse.data"></a>

#### data

回覆物件 IndexData

<a id="ddata.DTickDataBidOfferResponse"></a>

## DTickDataBidOfferResponse Objects

```python
@dataclass
class DTickDataBidOfferResponse()
```

最佳買賣價查詢回覆物件

<a id="ddata.DTickDataBidOfferResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DTickDataBidOfferResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DTickDataBidOfferResponse.data"></a>

#### data

回覆物件 TickDataBidOffer

<a id="ddata.DTickDataBeforeBidOfferResponse"></a>

## DTickDataBeforeBidOfferResponse Objects

```python
@dataclass
class DTickDataBeforeBidOfferResponse()
```

試撮最佳買賣價查詢回覆物件

<a id="ddata.DTickDataBeforeBidOfferResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DTickDataBeforeBidOfferResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DTickDataBeforeBidOfferResponse.data"></a>

#### data

回覆物件 TickDataBeforeBidOffer

<a id="ddata.BarData"></a>

## BarData Objects

```python
@dataclass
class BarData()
```

K線資料物件

<a id="ddata.BarData.productId"></a>

#### productId

商品代碼 str

<a id="ddata.BarData.productkind"></a>

#### productkind

商品種類 str

<a id="ddata.BarData.date"></a>

#### date

日期 str

<a id="ddata.BarData.time"></a>

#### time

時間 str

<a id="ddata.BarData.open"></a>

#### open

開盤價 float

<a id="ddata.BarData.high"></a>

#### high

最高價 float

<a id="ddata.BarData.low"></a>

#### low

最低價 float

<a id="ddata.BarData.close"></a>

#### close

收盤價 float

<a id="ddata.BarData.volume"></a>

#### volume

成交量 int

<a id="ddata.BarDataResponse"></a>

## BarDataResponse Objects

```python
@dataclass
class BarDataResponse()
```

K線資料回覆物件

<a id="ddata.BarDataResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.BarDataResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.BarDataResponse.data"></a>

#### data

回覆物件 List[BarData]

