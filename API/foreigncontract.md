---  
nav_order: 5
parent: API Reference  
title: "foreigncontract"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
<a id="foreigncontract.ForeignContract"></a>

## ForeignContract Objects

```python
@dataclass
class ForeignContract()
```

外期商品合約檔

<a id="foreigncontract.ForeignContract.exchange"></a>

#### exchange

交易所 str

<a id="foreigncontract.ForeignContract.symbol"></a>

#### symbol

商品代碼 str

<a id="foreigncontract.ForeignContract.type"></a>

#### type

類型 str <br/>期貨:F <br/>選擇權:O

<a id="foreigncontract.ForeignContract.monthyear"></a>

#### monthyear

年月 str

<a id="foreigncontract.ForeignContract.strikeprice"></a>

#### strikeprice

履約價 str

<a id="foreigncontract.ForeignContract.cp"></a>

#### cp

call put str

<a id="foreigncontract.ForeignContract.lasttradedate"></a>

#### lasttradedate

最後交易日 str

