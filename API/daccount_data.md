---  
nav_order: 11
parent: API Reference  
title: "daccount_data"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
內期帳務物件

<a id="ddata.DMargin"></a>

## DMargin Objects

```python
@dataclass
class DMargin()
```

內期保證金物件

<a id="ddata.DMargin.total_count"></a>

#### total\_count

總筆數 int

<a id="ddata.DMargin.current_count"></a>

#### current\_count

現在筆數 int

<a id="ddata.DMargin.network_id"></a>

#### network\_id

網路序號 str

<a id="ddata.DMargin.company"></a>

#### company

公司別 str

<a id="ddata.DMargin.actno"></a>

#### actno

帳號 str

<a id="ddata.DMargin.account_date"></a>

#### account\_date

帳務日期 str

<a id="ddata.DMargin.currency"></a>

#### currency

幣別 str

<a id="ddata.DMargin.exrate"></a>

#### exrate

匯率 float

<a id="ddata.DMargin.lctdab"></a>

#### lctdab

昨日權益數 float

<a id="ddata.DMargin.ltdab"></a>

#### ltdab

昨日餘額 float

<a id="ddata.DMargin.dwamt"></a>

#### dwamt

存提 float

<a id="ddata.DMargin.osprtlos"></a>

#### osprtlos

期貨平倉損益 float

<a id="ddata.DMargin.prtlos"></a>

#### prtlos

未沖銷期貨浮動損益 float

<a id="ddata.DMargin.optosprtlos"></a>

#### optosprtlos

選擇權平倉損益 float

<a id="ddata.DMargin.optprtlos"></a>

#### optprtlos

選擇權未平倉損益 float

<a id="ddata.DMargin.tpremium"></a>

#### tpremium

當日權利金支出收入 float

<a id="ddata.DMargin.orignfee"></a>

#### orignfee

成交手續費 float

<a id="ddata.DMargin.ctaxamt"></a>

#### ctaxamt

成交期交稅 float

<a id="ddata.DMargin.ordpremium"></a>

#### ordpremium

委託預扣權利金 float

<a id="ddata.DMargin.ctdab"></a>

#### ctdab

權益數 float

<a id="ddata.DMargin.ordiamt"></a>

#### ordiamt

委託預扣原始保證金 float

<a id="ddata.DMargin.iamt"></a>

#### iamt

原始保證金 float

<a id="ddata.DMargin.mamt"></a>

#### mamt

維持保證金 float

<a id="ddata.DMargin.ordcexcess"></a>

#### ordcexcess

可動用(出金) 保證金 float

<a id="ddata.DMargin.bpremium"></a>

#### bpremium

買方選擇權市值 float

<a id="ddata.DMargin.spremium"></a>

#### spremium

賣方選擇權市值 float

<a id="ddata.DMargin.optequity"></a>

#### optequity

權益總值 float

<a id="ddata.DMargin.inirate"></a>

#### inirate

原始比率 float

<a id="ddata.DMargin.matrate"></a>

#### matrate

維持比率 float

<a id="ddata.DMargin.liquidation_ratio"></a>

#### liquidation\_ratio

清算比率 float

<a id="ddata.DMargin.twdoptequity"></a>

#### twdoptequity

台幣權益總值 float

<a id="ddata.DMargin.twdinirate"></a>

#### twdinirate

台幣原始比率 str

<a id="ddata.DMargin.twdordexcess"></a>

#### twdordexcess

台幣可動用(出金)保證金 float

<a id="ddata.DMargin.securities_payment_amount"></a>

#### securities\_payment\_amount

有價證券抵繳金額 float

<a id="ddata.DMargin.tmp1prices"></a>

#### tmp1prices

加收保證金 float

<a id="ddata.DMargin.optrate"></a>

#### optrate

風險指標 float

<a id="ddata.DMargin.update_date"></a>

#### update\_date

資料更新日期 str

<a id="ddata.DMargin.update_time"></a>

#### update\_time

資料更新時間 str

<a id="ddata.DMargin.securities_valuation"></a>

#### securities\_valuation

有價證券評價價值 str

<a id="ddata.DMargin.excerciseprice"></a>

#### excerciseprice

到期履約損益 float

<a id="ddata.DMargin.transaction_total_quota"></a>

#### transaction\_total\_quota

交易總額度 float

<a id="ddata.DMargin.excess_margin"></a>

#### excess\_margin

超額/追繳保證金 float

<a id="ddata.DMargin.data_source_type"></a>

#### data\_source\_type

資料來源類別 str

<a id="ddata.DMargin.night_session_closing_ctdab"></a>

#### night\_session\_closing\_ctdab

夜盤收盤權益數 float

<a id="ddata.DMargin.night_session_optrate"></a>

#### night\_session\_optrate

夜盤風險指標 float

<a id="ddata.DMargin.night_session_optequity"></a>

#### night\_session\_optequity

夜盤權利總值 float

<a id="ddata.DMargin.night_session_iamt"></a>

#### night\_session\_iamt

夜盤原始保證金 float

<a id="ddata.DMargin.night_session_mamt"></a>

#### night\_session\_mamt

夜盤維持保證金 float

<a id="ddata.DMarginResponse"></a>

## DMarginResponse Objects

```python
@dataclass
class DMarginResponse()
```

保證金查詢回覆物件

<a id="ddata.DMarginResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DMarginResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DMarginResponse.data"></a>

#### data

回覆物件 List[DMargin]

<a id="ddata.DPosition"></a>

## DPosition Objects

```python
@dataclass
class DPosition()
```

內期即時部位物件

<a id="ddata.DPosition.total_count"></a>

#### total\_count

總筆數 int

<a id="ddata.DPosition.current_count"></a>

#### current\_count

現在筆數 int

<a id="ddata.DPosition.network_id"></a>

#### network\_id

網路序號 str

<a id="ddata.DPosition.company"></a>

#### company

公司別 str

<a id="ddata.DPosition.actno"></a>

#### actno

帳號 str

<a id="ddata.DPosition.currency"></a>

#### currency

幣別 str

<a id="ddata.DPosition.product"></a>

#### product

商品 str

<a id="ddata.DPosition.month"></a>

#### month

月份 str 預設年月(格式YYYYMM) 但股票週選會放年月日(格式YYMMDD)

<a id="ddata.DPosition.call_put"></a>

#### call\_put

Call Put str

<a id="ddata.DPosition.strike_price"></a>

#### strike\_price

履約價 float

<a id="ddata.DPosition.ot_qty_b"></a>

#### ot\_qty\_b

前日買進留倉 int

<a id="ddata.DPosition.ot_qty_s"></a>

#### ot\_qty\_s

前日賣出留倉 int

<a id="ddata.DPosition.noworder_qty_b"></a>

#### noworder\_qty\_b

本日買進委託 int

<a id="ddata.DPosition.noworder_qty_s"></a>

#### noworder\_qty\_s

本日賣出委託 int

<a id="ddata.DPosition.nowmatch_qty_b"></a>

#### nowmatch\_qty\_b

本日買進成交 int

<a id="ddata.DPosition.nowmatch_qty_s"></a>

#### nowmatch\_qty\_s

本日賣出成交 int

<a id="ddata.DPosition.today_close_position"></a>

#### today\_close\_position

本日平倉 int

<a id="ddata.DPosition.current_buy_open_position"></a>

#### current\_buy\_open\_position

目前買進留倉 int

<a id="ddata.DPosition.current_sell_open_position"></a>

#### current\_sell\_open\_position

目前賣出留倉 int

<a id="ddata.DPosition.combined_buy_balance"></a>

#### combined\_buy\_balance

組合買進餘額 float

<a id="ddata.DPosition.combined_sell_balance"></a>

#### combined\_sell\_balance

組合賣出餘額 float

<a id="ddata.DPosition.open_buy_position_average_cost"></a>

#### open\_buy\_position\_average\_cost

留倉買進平均成本 float

<a id="ddata.DPosition.open_sell_position_average_cost"></a>

#### open\_sell\_position\_average\_cost

留倉賣出平均成本 float

<a id="ddata.DPosition.buyer_IAMT"></a>

#### buyer\_IAMT

買方原始保證金 float

<a id="ddata.DPosition.seller_IAMT"></a>

#### seller\_IAMT

賣方原始保證金 float

<a id="ddata.DPosition.buyer_MAMT"></a>

#### buyer\_MAMT

買方維持保證金 float

<a id="ddata.DPosition.seller_MAMT"></a>

#### seller\_MAMT

賣方維持保證金 float

<a id="ddata.DPosition.product_base_number"></a>

#### product\_base\_number

商品基數 int

<a id="ddata.DPosition.reference_realPrice"></a>

#### reference\_realPrice

參考即時價 float

<a id="ddata.DPosition.close_position_pnl"></a>

#### close\_position\_pnl

平倉損益 float

<a id="ddata.DPosition.product_name"></a>

#### product\_name

商品名稱 str

<a id="ddata.DPosition.buy_spread_points"></a>

#### buy\_spread\_points

價差點數買

<a id="ddata.DPosition.sell_spread_points"></a>

#### sell\_spread\_points

價差點數賣 float

<a id="ddata.DPosition.floating_pnl"></a>

#### floating\_pnl

浮動損益 float

<a id="ddata.DPosition.data_source_type"></a>

#### data\_source\_type

資料來源類別 str

<a id="ddata.DPosition.productkind"></a>

#### productkind

商品類別 str (1:期貨 2:選擇權 3:複式選擇權 4:複式期貨)

<a id="ddata.DPosition.productid"></a>

#### productid

商品代碼 str

<a id="ddata.DPositionResponse"></a>

## DPositionResponse Objects

```python
@dataclass
class DPositionResponse()
```

即時部位查詢回覆物件

<a id="ddata.DPositionResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DPositionResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DPositionResponse.data"></a>

#### data

回覆物件 List[DPosition]

<a id="ddata.DUnliquidation"></a>

## DUnliquidation Objects

```python
@dataclass
class DUnliquidation()
```

內期未平倉物件

<a id="ddata.DUnliquidation.total_count"></a>

#### total\_count

總筆數 int

<a id="ddata.DUnliquidation.current_count"></a>

#### current\_count

現在筆數 int

<a id="ddata.DUnliquidation.network_id"></a>

#### network\_id

網路序號 str

<a id="ddata.DUnliquidation.company"></a>

#### company

公司別 str

<a id="ddata.DUnliquidation.actno"></a>

#### actno

帳號 str

<a id="ddata.DUnliquidation.productid"></a>

#### productid

商品代碼 str

<a id="ddata.DUnliquidation.bs"></a>

#### bs

買賣別 str

<a id="ddata.DUnliquidation.totalotqty"></a>

#### totalotqty

留倉口數 int

<a id="ddata.DUnliquidation.avgmatchprice"></a>

#### avgmatchprice

成交均價 float

<a id="ddata.DUnliquidation.realprice"></a>

#### realprice

即時價 float

<a id="ddata.DUnliquidation.reftotalpl"></a>

#### reftotalpl

浮動損益 float

<a id="ddata.DUnliquidation.ctaxamt"></a>

#### ctaxamt

交易稅 float

<a id="ddata.DUnliquidation.commission_fee"></a>

#### commission\_fee

手續費 float

<a id="ddata.DUnliquidation.net_profit_loss"></a>

#### net\_profit\_loss

淨損益 float

<a id="ddata.DUnliquidation.leg1_product_category"></a>

#### leg1\_product\_category

腳一商品類別 str

<a id="ddata.DUnliquidation.leg1_product_date"></a>

#### leg1\_product\_date

腳一商品年月 str 預設年月(格式YYYYMM) 但股票週選會放年月日(格式YYMMDD)

<a id="ddata.DUnliquidation.leg1_strike_price"></a>

#### leg1\_strike\_price

腳一履約價 str

<a id="ddata.DUnliquidation.leg1_call_put"></a>

#### leg1\_call\_put

腳一買賣權 str

<a id="ddata.DUnliquidation.leg1_buy_sell"></a>

#### leg1\_buy\_sell

腳一買賣別 str

<a id="ddata.DUnliquidation.leg1_average_price"></a>

#### leg1\_average\_price

腳一成交均價 float

<a id="ddata.DUnliquidation.leg2_product_category"></a>

#### leg2\_product\_category

腳二商品類別 str

<a id="ddata.DUnliquidation.leg2_product_date"></a>

#### leg2\_product\_date

腳二商品年月 str 預設年月(格式YYYYMM) 但股票週選會放年月日(格式YYMMDD)

<a id="ddata.DUnliquidation.leg2_strike_price"></a>

#### leg2\_strike\_price

腳二履約價 str

<a id="ddata.DUnliquidation.leg2_call_put"></a>

#### leg2\_call\_put

腳二買賣權 str

<a id="ddata.DUnliquidation.leg2_buy_sell"></a>

#### leg2\_buy\_sell

腳二買賣別 str

<a id="ddata.DUnliquidation.leg2_average_price"></a>

#### leg2\_average\_price

腳二成交均價 float

<a id="ddata.DUnliquidation.product_name"></a>

#### product\_name

商品名稱 str

<a id="ddata.DUnliquidation.leg1_productid"></a>

#### leg1\_productid

腳一商品 str

<a id="ddata.DUnliquidation.leg2_productid"></a>

#### leg2\_productid

腳二商品 str

<a id="ddata.DUnliquidation.multiname"></a>

#### multiname

複式單策略名稱 str

<a id="ddata.DUnliquidation.data_source_type"></a>

#### data\_source\_type

資料來源類別 str

<a id="ddata.DUnliquidationResponse"></a>

## DUnliquidationResponse Objects

```python
@dataclass
class DUnliquidationResponse()
```

未平倉查詢回覆物件

<a id="ddata.DUnliquidationResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DUnliquidationResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DUnliquidationResponse.data"></a>

#### data

回覆物件 List[TickDataSettle]

<a id="ddata.Response"></a>

## Response Objects

```python
@dataclass
class Response()
```

回覆物件

<a id="ddata.Response.ok"></a>

#### ok

是否成功 bool

<a id="ddata.Response.error"></a>

#### error

錯誤訊息 str

