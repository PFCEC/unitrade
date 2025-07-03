---  
nav_order: 7
parent: API Reference  
title: "dtrade_data"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
內期交易物件

<a id="ddata.DOrderReply"></a>

## DOrderReply Objects

```python
@dataclass
class DOrderReply()
```

委託回報物件

<a id="ddata.DOrderReply.brokerid"></a>

#### brokerid

分公司 str

<a id="ddata.DOrderReply.investoracno"></a>

#### investoracno

帳號 str

<a id="ddata.DOrderReply.networkid"></a>

#### networkid

網路流水序號 str

<a id="ddata.DOrderReply.ordertime"></a>

#### ordertime

委託時間 str

<a id="ddata.DOrderReply.orderno"></a>

#### orderno

委託書號 str

<a id="ddata.DOrderReply.subact"></a>

#### subact

子帳 str

<a id="ddata.DOrderReply.productkind"></a>

#### productkind

商品類別 str (1:期貨 2:選擇權 3:複式選擇權 4:複式期貨)

<a id="ddata.DOrderReply.productid"></a>

#### productid

商品代碼 str

<a id="ddata.DOrderReply.bs"></a>

#### bs

買賣別 str B:買進 S:賣出

<a id="ddata.DOrderReply.ordertype"></a>

#### ordertype

價格別 str (L:限價 M:市價 P:範圍市價)

<a id="ddata.DOrderReply.price"></a>

#### price

委託價格 float

<a id="ddata.DOrderReply.orderqty"></a>

#### orderqty

委託數量 str

<a id="ddata.DOrderReply.nomatchqty"></a>

#### nomatchqty

未成交數量

<a id="ddata.DOrderReply.matchqty"></a>

#### matchqty

成交數量 int

<a id="ddata.DOrderReply.delqty"></a>

#### delqty

刪除數量 int

<a id="ddata.DOrderReply.ordercondition"></a>

#### ordercondition

委託種類 I:IOC R:ROD F:FOK

<a id="ddata.DOrderReply.opencloseflag"></a>

#### opencloseflag

開倉別 str 0:新倉 1:平倉 空白:自動

<a id="ddata.DOrderReply.tradedate"></a>

#### tradedate

交易日期 str

<a id="ddata.DOrderReply.note"></a>

#### note

備註 str

<a id="ddata.DOrderReply.mdate"></a>

#### mdate

異動時間 str

<a id="ddata.DOrderReply.orderstatus"></a>

#### orderstatus

委託狀態 str

<a id="ddata.DOrderReply.statuscode"></a>

#### statuscode

委託狀態碼 str

<a id="ddata.DOrderReply.seq"></a>

#### seq

下單序號 str

<a id="ddata.DMatchReply"></a>

## DMatchReply Objects

```python
@dataclass
class DMatchReply()
```

成交回報物件

<a id="ddata.DMatchReply.brokerid"></a>

#### brokerid

分公司 str

<a id="ddata.DMatchReply.investoracno"></a>

#### investoracno

帳號 str

<a id="ddata.DMatchReply.networkid"></a>

#### networkid

網路流水序號 str

<a id="ddata.DMatchReply.matchtime"></a>

#### matchtime

成交時間 str

<a id="ddata.DMatchReply.orderno"></a>

#### orderno

委託書號 str

<a id="ddata.DMatchReply.subact"></a>

#### subact

子帳 str

<a id="ddata.DMatchReply.productkind"></a>

#### productkind

商品類別 str(1:期貨 2:選擇權 3:複式選擇權 4:複式期貨)

<a id="ddata.DMatchReply.productid"></a>

#### productid

商品代碼 str

<a id="ddata.DMatchReply.bs"></a>

#### bs

買賣別 str B:買進 S:賣出

<a id="ddata.DMatchReply.matchprice"></a>

#### matchprice

成交價格 float

<a id="ddata.DMatchReply.matchqty"></a>

#### matchqty

成交口數 int

<a id="ddata.DMatchReply.matchseq"></a>

#### matchseq

成交序號 str

<a id="ddata.DMatchReply.matchpricefoot1"></a>

#### matchpricefoot1

成交價1 float

<a id="ddata.DMatchReply.matchpricefoot2"></a>

#### matchpricefoot2

成交價2 float

<a id="ddata.DMatchReply.note"></a>

#### note

備註 str

<a id="ddata.DMatchReply.mdate"></a>

#### mdate

異動時間 str

<a id="ddata.DMatchReply.brokerid"></a>

#### brokerid

分公司 str

<a id="ddata.DMatchReply.investoracno"></a>

#### investoracno

帳號 str

<a id="ddata.DMatchReply.networkid"></a>

#### networkid

網路流水序號 str

<a id="ddata.DMatchReply.matchtime"></a>

#### matchtime

成交時間 str

<a id="ddata.DMatchReply.orderno"></a>

#### orderno

委託書號 str

<a id="ddata.DMatchReply.subact"></a>

#### subact

子帳 str

<a id="ddata.DMatchReply.productkind"></a>

#### productkind

商品類別 str(1:期貨 2:選擇權 3:複式選擇權 4:複式期貨)

<a id="ddata.DMatchReply.productid"></a>

#### productid

商品代碼 str

<a id="ddata.DMatchReply.bs"></a>

#### bs

買賣別 str B:買進 S:賣出

<a id="ddata.DMatchReply.matchprice"></a>

#### matchprice

成交價格 float

<a id="ddata.DMatchReply.matchqty"></a>

#### matchqty

成交口數 int

<a id="ddata.DMatchReply.matchseq"></a>

#### matchseq

成交序號 str

<a id="ddata.DMatchReply.matchpricefoot1"></a>

#### matchpricefoot1

成交價1 float

<a id="ddata.DMatchReply.matchpricefoot2"></a>

#### matchpricefoot2

成交價2 float

<a id="ddata.DMatchReply.note"></a>

#### note

備註 str

<a id="ddata.DMatchReply.mdate"></a>

#### mdate

異動時間 str

<a id="ddata.DOrderObject"></a>

## DOrderObject Objects

```python
@dataclass
class DOrderObject()
```

下單物件

<a id="ddata.DOrderObject.actno"></a>

#### actno

帳號 str

<a id="ddata.DOrderObject.subactno"></a>

#### subactno

子帳 str

<a id="ddata.DOrderObject.productid"></a>

#### productid

商品代號 str

<a id="ddata.DOrderObject.bs"></a>

#### bs

買賣別 str B:買進 S:賣出

<a id="ddata.DOrderObject.ordertype"></a>

#### ordertype

下單方式 str L:限價 M:市價 P:範圍市價

<a id="ddata.DOrderObject.price"></a>

#### price

委託價格 float

<a id="ddata.DOrderObject.orderqty"></a>

#### orderqty

委託數量 int

<a id="ddata.DOrderObject.ordercondition"></a>

#### ordercondition

委託種類 str I:IOC R:ROD F:FOK

<a id="ddata.DOrderObject.opencloseflag"></a>

#### opencloseflag

新平倉碼 str 0:新倉 1:平倉 空白:自動

<a id="ddata.DOrderObject.dtrade"></a>

#### dtrade

當沖碼 str Y:當沖 N:非當沖

<a id="ddata.DOrderObject.note"></a>

#### note

備註 str:限10碼非中文

<a id="ddata.DReplaceObject"></a>

## DReplaceObject Objects

```python
@dataclass
class DReplaceObject()
```

改單物件

<a id="ddata.DReplaceObject.replacetype"></a>

#### replacetype

修改方式 str4:取消, 5: 減量, m:改價

<a id="ddata.DReplaceObject.actno"></a>

#### actno

帳號 str

<a id="ddata.DReplaceObject.orderno"></a>

#### orderno

委託書號 str

<a id="ddata.DReplaceObject.ordercondition"></a>

#### ordercondition

委託種類 str I:IOC R:ROD F:FOK

<a id="ddata.DReplaceObject.ordertype"></a>

#### ordertype

下單方式 str L:限價 M:市價 P:範圍市價

<a id="ddata.DReplaceObject.price"></a>

#### price

委託價格 float

<a id="ddata.DReplaceObject.orderqty"></a>

#### orderqty

委託數量 int

<a id="ddata.DReplaceObject.note"></a>

#### note

備註 str:限10碼非中文

<a id="ddata.DOrderResponse"></a>

## DOrderResponse Objects

```python
@dataclass
class DOrderResponse()
```

下單回覆物件

<a id="ddata.DOrderResponse.issend"></a>

#### issend

是否送出 bool

<a id="ddata.DOrderResponse.errorcode"></a>

#### errorcode

錯誤代碼 str

<a id="ddata.DOrderResponse.errormsg"></a>

#### errormsg

錯誤訊息 str

<a id="ddata.DOrderResponse.note"></a>

#### note

下單傳入備註 str

<a id="ddata.DOrderResponse.seq"></a>

#### seq

下單序號 str

<a id="ddata.DQueryReplyResponse"></a>

## DQueryReplyResponse Objects

```python
@dataclass
class DQueryReplyResponse()
```

委託回報查詢回覆物件

<a id="ddata.DQueryReplyResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DQueryReplyResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DQueryReplyResponse.data"></a>

#### data

回報集合 List[OrderReply]

<a id="ddata.DQueryMatchResponse"></a>

## DQueryMatchResponse Objects

```python
@dataclass
class DQueryMatchResponse()
```

成交回報查詢回覆物件

<a id="ddata.DQueryMatchResponse.ok"></a>

#### ok

是否成功 bool

<a id="ddata.DQueryMatchResponse.error"></a>

#### error

錯誤訊息 str

<a id="ddata.DQueryMatchResponse.data"></a>

#### data

成回集合 List[MatchReply]

