---  
nav_order: 13
parent: API Reference  
title: "faccount_data"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
<a id="fdata.FMargin"></a>

## FMargin Objects

```python
@dataclass
class FMargin()
```

外期保證金物件

<a id="fdata.FMargin.total_count"></a>

#### total\_count

總筆數 int

<a id="fdata.FMargin.current_count"></a>

#### current\_count

現在筆數int

<a id="fdata.FMargin.web_code"></a>

#### web\_code

Web代號 str

<a id="fdata.FMargin.web_serial"></a>

#### web\_serial

網路序號 str

<a id="fdata.FMargin.currency"></a>

#### currency

幣別 str

<a id="fdata.FMargin.previous_day_balance"></a>

#### previous\_day\_balance

前日帳款餘額 float

<a id="fdata.FMargin.commission"></a>

#### commission

手續費 float

<a id="fdata.FMargin.exchange_rate"></a>

#### exchange\_rate

匯率 float

<a id="fdata.FMargin.futures_tax"></a>

#### futures\_tax

期交稅 float

<a id="fdata.FMargin.deposit_withdrawal_amount"></a>

#### deposit\_withdrawal\_amount

存提金額 float

<a id="fdata.FMargin.close_pnl"></a>

#### close\_pnl

平倉損益 float

<a id="fdata.FMargin.unrealized_pnl"></a>

#### unrealized\_pnl

未平倉損益 float

<a id="fdata.FMargin.buy_option_market_value"></a>

#### buy\_option\_market\_value

買方選擇權市值 float

<a id="fdata.FMargin.sell_option_market_value"></a>

#### sell\_option\_market\_value

賣方選擇權市值 float

<a id="fdata.FMargin.order_withholding_premium"></a>

#### order\_withholding\_premium

下單預扣權利金 float

<a id="fdata.FMargin.today_premium_income_expense"></a>

#### today\_premium\_income\_expense

當日權利金收支 float

<a id="fdata.FMargin.net_value"></a>

#### net\_value

淨值 float

<a id="fdata.FMargin.original_margin"></a>

#### original\_margin

原始保證金 float

<a id="fdata.FMargin.maintenance_margin"></a>

#### maintenance\_margin

維持保證金 float

<a id="fdata.FMargin.available_balance"></a>

#### available\_balance

可用餘額 float

<a id="fdata.FMargin.order_available_margin"></a>

#### order\_available\_margin

下單可用保證金 float

<a id="fdata.FMargin.today_order_margin"></a>

#### today\_order\_margin

當日委託保證金 float

<a id="fdata.FMargin.performance_pnl"></a>

#### performance\_pnl

履約損益 float

<a id="fdata.FMargin.variable_premium"></a>

#### variable\_premium

變動權利金float

<a id="fdata.FMargin.marking_time"></a>

#### marking\_time

洗價時間 str

<a id="fdata.FMargin.additional_payment"></a>

#### additional\_payment

追繳金額 float

<a id="fdata.FMargin.yesterday_unrealized_pnl"></a>

#### yesterday\_unrealized\_pnl

昨日未平倉損益 float

<a id="fdata.FMargin.today_intraday_unrealized_pnl"></a>

#### today\_intraday\_unrealized\_pnl

今日盤中浮動損益 float

<a id="fdata.FMargin.sell_vertical_spread_market_value"></a>

#### sell\_vertical\_spread\_market\_value

賣方垂直價差市值 float

<a id="fdata.FMargin.strike_payment"></a>

#### strike\_payment

履約價款 float

<a id="fdata.FMargin.today_balance"></a>

#### today\_balance

今日餘額 float

<a id="fdata.FMargin.account_total_market_value"></a>

#### account\_total\_market\_value

帳戶總市值 float

<a id="fdata.FMargin.full_original_margin"></a>

#### full\_original\_margin

足額原始保證金 float

<a id="fdata.FMargin.total_market_value_risk"></a>

#### total\_market\_value\_risk

總市值風險 float

<a id="fdata.FMargin.risk_coefficient"></a>

#### risk\_coefficient

風險係數 float

<a id="fdata.FMargin.maintenance_rate"></a>

#### maintenance\_rate

維持率 float

<a id="fdata.FMargin.company_type"></a>

#### company\_type

公司別 str

<a id="fdata.FMargin.account"></a>

#### account

帳號 str

<a id="fdata.FMargin.group"></a>

#### group

組別 str

<a id="fdata.FMargin.trader"></a>

#### trader

交易員 str

<a id="fdata.FMarginResponse"></a>

## FMarginResponse Objects

```python
@dataclass
class FMarginResponse()
```

保證金查詢回覆物件

<a id="fdata.FMarginResponse.ok"></a>

#### ok

是否成功 bool

<a id="fdata.FMarginResponse.error"></a>

#### error

錯誤訊息 str

<a id="fdata.FMarginResponse.data"></a>

#### data

回覆物件 List[Margin]

<a id="fdata.FUnliquidation"></a>

## FUnliquidation Objects

```python
@dataclass
class FUnliquidation()
```

外期未平倉物件

<a id="fdata.FUnliquidation.total_count"></a>

#### total\_count

總筆數 int

<a id="fdata.FUnliquidation.current_count"></a>

#### current\_count

現在筆數 int

<a id="fdata.FUnliquidation.company_type"></a>

#### company\_type

公司別 str

<a id="fdata.FUnliquidation.client_account"></a>

#### client\_account

客戶帳號 str

<a id="fdata.FUnliquidation.exchange"></a>

#### exchange

交易所 str

<a id="fdata.FUnliquidation.buy_sell_type_1"></a>

#### buy\_sell\_type\_1

買賣別1 str

<a id="fdata.FUnliquidation.trade_type_1"></a>

#### trade\_type\_1

交易種類1 str

<a id="fdata.FUnliquidation.product_code_1"></a>

#### product\_code\_1

商品代號1 str

<a id="fdata.FUnliquidation.product_year_month_1"></a>

#### product\_year\_month\_1

商品年月1 str

<a id="fdata.FUnliquidation.strike_price_1"></a>

#### strike\_price\_1

履約價1 float

<a id="fdata.FUnliquidation.buy_sell_option_1"></a>

#### buy\_sell\_option\_1

買賣權1 str

<a id="fdata.FUnliquidation.open_interest_1"></a>

#### open\_interest\_1

未平倉量1 int

<a id="fdata.FUnliquidation.settlement_price_1"></a>

#### settlement\_price\_1

結算價1 float

<a id="fdata.FUnliquidation.spot_price_1"></a>

#### spot\_price\_1

即時價1 float

<a id="fdata.FUnliquidation.unrealized_pnl_1"></a>

#### unrealized\_pnl\_1

未平倉損益1 float

<a id="fdata.FUnliquidation.initial_margin_1"></a>

#### initial\_margin\_1

原始保證金1 float

<a id="fdata.FUnliquidation.maintenance_margin_1"></a>

#### maintenance\_margin\_1

維持保證金1 float

<a id="fdata.FUnliquidation.currency_1"></a>

#### currency\_1

幣別1 str

<a id="fdata.FUnliquidation.deal_price_1"></a>

#### deal\_price\_1

成交價1 float

<a id="fdata.FUnliquidation.broker_code"></a>

#### broker\_code

上手代號 str

<a id="fdata.FUnliquidation.unrealized_pnl_ntd_1"></a>

#### unrealized\_pnl\_ntd\_1

未平倉損益-約當台幣1 float

<a id="fdata.FUnliquidation.commission_1"></a>

#### commission\_1

手續費1 float

<a id="fdata.FUnliquidation.business_tax_1"></a>

#### business\_tax\_1

營業稅1 float

<a id="fdata.FUnliquidation.net_open_interest_pnl_1"></a>

#### net\_open\_interest\_pnl\_1

淨未平倉損益1 float

<a id="fdata.FUnliquidation.net_open_interest_pnl_ntd_1"></a>

#### net\_open\_interest\_pnl\_ntd\_1

淨未平倉損益-約當台幣1 float

<a id="fdata.FUnliquidation.group"></a>

#### group

組別 str

<a id="fdata.FUnliquidation.trader"></a>

#### trader

交易員 str

<a id="fdata.FUnliquidation.abbreviation"></a>

#### abbreviation

簡稱 str

<a id="fdata.FUnliquidation.backend_pricebase"></a>

#### backend\_pricebase

後台Pricebase str

<a id="fdata.FUnliquidation.display_pricebase"></a>

#### display\_pricebase

顯示pricebase str

<a id="fdata.FUnliquidationResponse"></a>

## FUnliquidationResponse Objects

```python
@dataclass
class FUnliquidationResponse()
```

未平倉查詢回覆物件

<a id="fdata.FUnliquidationResponse.ok"></a>

#### ok

是否成功 bool

<a id="fdata.FUnliquidationResponse.error"></a>

#### error

錯誤訊息 str

<a id="fdata.FUnliquidationResponse.data"></a>

#### data

回覆物件 List[TickDataSettle]

<a id="fdata.FPosition"></a>

## FPosition Objects

```python
@dataclass
class FPosition()
```

外期即時部位物件

<a id="fdata.FPosition.total_count"></a>

#### total\_count

總筆數 int

<a id="fdata.FPosition.current_count"></a>

#### current\_count

現在筆數 int

<a id="fdata.FPosition.web_code"></a>

#### web\_code

Web代號 str

<a id="fdata.FPosition.web_serial"></a>

#### web\_serial

網路序號 str

<a id="fdata.FPosition.company_type"></a>

#### company\_type

公司別 str

<a id="fdata.FPosition.client_account"></a>

#### client\_account

客戶帳號 str

<a id="fdata.FPosition.exchange"></a>

#### exchange

交易所 str

<a id="fdata.FPosition.trade_type"></a>

#### trade\_type

交易種類 str

<a id="fdata.FPosition.product_code"></a>

#### product\_code

商品代號 str

<a id="fdata.FPosition.product_year_month"></a>

#### product\_year\_month

商品年月 str

<a id="fdata.FPosition.strike_price"></a>

#### strike\_price

履約價 float

<a id="fdata.FPosition.buy_sell_option"></a>

#### buy\_sell\_option

買賣權 str

<a id="fdata.FPosition.net_buy"></a>

#### net\_buy

淨買 int

<a id="fdata.FPosition.net_sell"></a>

#### net\_sell

淨賣 int

<a id="fdata.FPosition.buyer_position"></a>

#### buyer\_position

買方留倉 int

<a id="fdata.FPosition.seller_position"></a>

#### seller\_position

賣方留倉 int

<a id="fdata.FPosition.buyer_transaction"></a>

#### buyer\_transaction

買方成交 int

<a id="fdata.FPosition.seller_transaction"></a>

#### seller\_transaction

賣方成交 int

<a id="fdata.FPosition.buyer_order"></a>

#### buyer\_order

買方委託 int

<a id="fdata.FPosition.seller_order"></a>

#### seller\_order

賣方委託 int

<a id="fdata.FPosition.delivery_date"></a>

#### delivery\_date

交割日期 str

<a id="fdata.FPosition.currency"></a>

#### currency

幣別 str

<a id="fdata.FPosition.average_deal_price"></a>

#### average\_deal\_price

成交均價 float

<a id="fdata.FPosition.instant_price"></a>

#### instant\_price

即時價 float

<a id="fdata.FPosition.unrealized_pnl"></a>

#### unrealized\_pnl

未平倉損益 float

<a id="fdata.FPosition.close_volume"></a>

#### close\_volume

平倉口數 int

<a id="fdata.FPosition.close_pnl"></a>

#### close\_pnl

平倉損益 float

<a id="fdata.FPosition.group"></a>

#### group

組別 str

<a id="fdata.FPosition.trader"></a>

#### trader

交易員 str

<a id="fdata.FPosition.abbreviation"></a>

#### abbreviation

簡稱 str

<a id="fdata.FPosition.price_base"></a>

#### price\_base

Pricebase str

<a id="fdata.FPositionResponse"></a>

## FPositionResponse Objects

```python
@dataclass
class FPositionResponse()
```

即時部位查詢回覆物件

<a id="fdata.FPositionResponse.ok"></a>

#### ok

是否成功 bool

<a id="fdata.FPositionResponse.error"></a>

#### error

錯誤訊息 str

<a id="fdata.FPositionResponse.data"></a>

#### data

回覆物件 List[Position]

