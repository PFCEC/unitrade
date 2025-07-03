---  
nav_order: 9
parent: API Reference
title: "ftrade_data"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
外期交易物件

<a id="fdata.FOrderReply"></a>

## FOrderReply Objects

```python
@dataclass
class FOrderReply()
```

委託回報物件

<a id="fdata.FOrderReply.brokerid"></a>

#### brokerid

分公司 str

<a id="fdata.FOrderReply.investoracno"></a>

#### investoracno

帳號 str

<a id="fdata.FOrderReply.networkid"></a>

#### networkid

網路流水序號 str

<a id="fdata.FOrderReply.ordertime"></a>

#### ordertime

委託時間 str

<a id="fdata.FOrderReply.orderno"></a>

#### orderno

委託書號 str

<a id="fdata.FOrderReply.subact"></a>

#### subact

子帳 str

<a id="fdata.FOrderReply.productkind"></a>

#### productkind

商品類別 str(1:期貨 2:選擇權 3:複式選擇權 4:複式期貨)

<a id="fdata.FOrderReply.exchange"></a>

#### exchange

交易所 str

<a id="fdata.FOrderReply.symbol"></a>

#### symbol

商品代碼 str

<a id="fdata.FOrderReply.maturitymonthyear"></a>

#### maturitymonthyear

年月 str

<a id="fdata.FOrderReply.putorcall"></a>

#### putorcall

CP str F:期貨 C:Call P:Put

<a id="fdata.FOrderReply.strikeprice"></a>

#### strikeprice

履約價 str

<a id="fdata.FOrderReply.symbol2"></a>

#### symbol2

商品代碼2 str

<a id="fdata.FOrderReply.maturitymonthyear2"></a>

#### maturitymonthyear2

年月2 str

<a id="fdata.FOrderReply.putorcall2"></a>

#### putorcall2

CP2 str  F:期貨 C:Call P:Put

<a id="fdata.FOrderReply.strikeprice2"></a>

#### strikeprice2

履約價2 str

<a id="fdata.FOrderReply.side1"></a>

#### side1

side1 str

<a id="fdata.FOrderReply.side2"></a>

#### side2

side2 str

<a id="fdata.FOrderReply.bs"></a>

#### bs

"買賣別 str B:買進 S:賣出

<a id="fdata.FOrderReply.ordertype"></a>

#### ordertype

價格別 str L:限價 M:市價  3:停損市價 4:停損限價

<a id="fdata.FOrderReply.price"></a>

#### price

委託價格 float

<a id="fdata.FOrderReply.stopprice"></a>

#### stopprice

停損價格 float

<a id="fdata.FOrderReply.orderqty"></a>

#### orderqty

委託數量 int

<a id="fdata.FOrderReply.nomatchqty"></a>

#### nomatchqty

未成交數量 int

<a id="fdata.FOrderReply.matchqty"></a>

#### matchqty

成交數量 int

<a id="fdata.FOrderReply.delqty"></a>

#### delqty

刪除數量 int

<a id="fdata.FOrderReply.pricebase"></a>

#### pricebase

pricebase int

<a id="fdata.FOrderReply.ordercondition"></a>

#### ordercondition

委託種類 str  I:IOC R:ROD F:FOK

<a id="fdata.FOrderReply.opencloseflag"></a>

#### opencloseflag

開倉別 str0:新倉 1:平倉 空白:自動

<a id="fdata.FOrderReply.tradedate"></a>

#### tradedate

交易日期 str

<a id="fdata.FOrderReply.note"></a>

#### note

備註 str

<a id="fdata.FOrderReply.mdate"></a>

#### mdate

異動時間 str

<a id="fdata.FOrderReply.orderstatus"></a>

#### orderstatus

委託狀態 str

<a id="fdata.FOrderReply.statuscode"></a>

#### statuscode

委託狀態碼 str

<a id="fdata.FOrderReply.seq"></a>

#### seq

下單序號 str

<a id="fdata.FMatchReply"></a>

## FMatchReply Objects

```python
@dataclass
class FMatchReply()
```

成交回報物件

<a id="fdata.FMatchReply.brokerid"></a>

#### brokerid

分公司 str

<a id="fdata.FMatchReply.investoracno"></a>

#### investoracno

帳號 str

<a id="fdata.FMatchReply.networkid"></a>

#### networkid

網路流水序號 str

<a id="fdata.FMatchReply.matchtime"></a>

#### matchtime

委託時間 str

<a id="fdata.FMatchReply.orderno"></a>

#### orderno

委託書號 str

<a id="fdata.FMatchReply.subact"></a>

#### subact

子帳 str

<a id="fdata.FMatchReply.productkind"></a>

#### productkind

商品類別 str(1:期貨 2:選擇權 3:複式選擇權 4:複式期貨)

<a id="fdata.FMatchReply.exchange"></a>

#### exchange

交易所 str

<a id="fdata.FMatchReply.symbol"></a>

#### symbol

商品代碼 str

<a id="fdata.FMatchReply.maturitymonthyear"></a>

#### maturitymonthyear

年月 str

<a id="fdata.FMatchReply.putorcall"></a>

#### putorcall

CP str F:期貨 C:Call P:Put

<a id="fdata.FMatchReply.strikeprice"></a>

#### strikeprice

履約價 str

<a id="fdata.FMatchReply.symbol2"></a>

#### symbol2

商品代碼2 str

<a id="fdata.FMatchReply.maturitymonthyear2"></a>

#### maturitymonthyear2

年月2 str

<a id="fdata.FMatchReply.putorcall2"></a>

#### putorcall2

CP2 str

<a id="fdata.FMatchReply.strikeprice2"></a>

#### strikeprice2

履約價2 str

<a id="fdata.FMatchReply.side1"></a>

#### side1

side1 str

<a id="fdata.FMatchReply.side2"></a>

#### side2

side2 str

<a id="fdata.FMatchReply.bs"></a>

#### bs

"買賣別 str B:買進 S:賣出

<a id="fdata.FMatchReply.matchprice"></a>

#### matchprice

"成交價格 float

<a id="fdata.FMatchReply.matchqty"></a>

#### matchqty

"成交口數 int

<a id="fdata.FMatchReply.matchseq"></a>

#### matchseq

"成交序號 str

<a id="fdata.FMatchReply.pricebase"></a>

#### pricebase

pricebase int

<a id="fdata.FMatchReply.note"></a>

#### note

備註 str

<a id="fdata.FMatchReply.mdate"></a>

#### mdate

異動時間 str

<a id="fdata.FOrderObject"></a>

## FOrderObject Objects

```python
@dataclass
class FOrderObject()
```

下單物件

<a id="fdata.FOrderObject.actno"></a>

#### actno

帳號 str

<a id="fdata.FOrderObject.subactno"></a>

#### subactno

子帳 str

<a id="fdata.FOrderObject.exchange"></a>

#### exchange

交易所  str

<a id="fdata.FOrderObject.symbol"></a>

#### symbol

商品代碼  str

<a id="fdata.FOrderObject.maturitymonthyear"></a>

#### maturitymonthyear

年月  str

<a id="fdata.FOrderObject.putorcall"></a>

#### putorcall

CP  str F:期貨 C:Call P:Put

<a id="fdata.FOrderObject.strikeprice"></a>

#### strikeprice

履約價  str

<a id="fdata.FOrderObject.symbol2"></a>

#### symbol2

商品代碼2  str

<a id="fdata.FOrderObject.maturitymonthyear2"></a>

#### maturitymonthyear2

年月2  str

<a id="fdata.FOrderObject.putorcall2"></a>

#### putorcall2

CP2  str

<a id="fdata.FOrderObject.strikeprice2"></a>

#### strikeprice2

履約價2  str

<a id="fdata.FOrderObject.side1"></a>

#### side1

side1  str

<a id="fdata.FOrderObject.side2"></a>

#### side2

side2  str

<a id="fdata.FOrderObject.bs"></a>

#### bs

買賣別 str B:買進 S:賣出

<a id="fdata.FOrderObject.ordertype"></a>

#### ordertype

下單方式 str L:限價 M:市價   3:停損市價 4:停損限價

<a id="fdata.FOrderObject.price"></a>

#### price

委託價格 float

<a id="fdata.FOrderObject.stopprice"></a>

#### stopprice

停損價格 float

<a id="fdata.FOrderObject.orderqty"></a>

#### orderqty

委託數量 int

<a id="fdata.FOrderObject.ordercondition"></a>

#### ordercondition

委託種類 str  I:IOC R:ROD F:FOK

<a id="fdata.FOrderObject.opencloseflag"></a>

#### opencloseflag

新平倉碼 str

<a id="fdata.FOrderObject.dtrade"></a>

#### dtrade

當沖碼 str Y:當沖 N:非當沖

<a id="fdata.FOrderObject.note"></a>

#### note

備註 str:限10碼非中文

<a id="fdata.FReplaceObject"></a>

## FReplaceObject Objects

```python
@dataclass
class FReplaceObject()
```

改單物件

<a id="fdata.FReplaceObject.replacetype"></a>

#### replacetype

修改方式 str 4:取消, 5: 減量, m:改價

<a id="fdata.FReplaceObject.actno"></a>

#### actno

帳號 str

<a id="fdata.FReplaceObject.orderno"></a>

#### orderno

委託書號 str

<a id="fdata.FReplaceObject.ordercondition"></a>

#### ordercondition

委託種類 str  I:IOC R:ROD F:FOK

<a id="fdata.FReplaceObject.ordertype"></a>

#### ordertype

下單方式 str  L:限價 M:市價 3:停損市價 4:停損限價

<a id="fdata.FReplaceObject.price"></a>

#### price

委託價格 float

<a id="fdata.FReplaceObject.stopprice"></a>

#### stopprice

停損價格 float

<a id="fdata.FReplaceObject.orderqty"></a>

#### orderqty

委託數量 int

<a id="fdata.FReplaceObject.note"></a>

#### note

備註:限10碼非中文 str

<a id="fdata.FOrderResponse"></a>

## FOrderResponse Objects

```python
@dataclass
class FOrderResponse()
```

下單回覆物件

<a id="fdata.FOrderResponse.issend"></a>

#### issend

是否送出 bool

<a id="fdata.FOrderResponse.errorcode"></a>

#### errorcode

錯誤代碼 str

<a id="fdata.FOrderResponse.errormsg"></a>

#### errormsg

錯誤訊息 str

<a id="fdata.FOrderResponse.note"></a>

#### note

下單傳入備註 str

<a id="fdata.FOrderResponse.seq"></a>

#### seq

下單序號 str

<a id="fdata.FQueryReplyResponse"></a>

## FQueryReplyResponse Objects

```python
@dataclass
class FQueryReplyResponse()
```

委託回報查詢回覆物件

<a id="fdata.FQueryReplyResponse.ok"></a>

#### ok

是否成功 bool

<a id="fdata.FQueryReplyResponse.error"></a>

#### error

錯誤訊息 str

<a id="fdata.FQueryReplyResponse.data"></a>

#### data

回報集合 List[OrderReply]

<a id="fdata.FQueryMatchResponse"></a>

## FQueryMatchResponse Objects

```python
@dataclass
class FQueryMatchResponse()
```

成交回報查詢回覆物件

<a id="fdata.FQueryMatchResponse.ok"></a>

#### ok

是否成功 bool

<a id="fdata.FQueryMatchResponse.error"></a>

#### error

錯誤訊息 str

<a id="fdata.FQueryMatchResponse.data"></a>

#### data

成回集合 List[MatchReply]

