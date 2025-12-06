---  
nav_order: 2
parent: API Reference  
title: "domesticcontract"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
<a id="domesticcontract.DomesticContract"></a>

## DomesticContract Objects

```python
@dataclass
class DomesticContract()
```

內期商品合約檔

<a id="domesticcontract.DomesticContract.prod_id"></a>

#### prod\_id

商品代號 str

<a id="domesticcontract.DomesticContract.month"></a>

#### month

年月 str 預設年月(格式YYYYMM) 但股票週選會放年月日(格式YYMMDD)

<a id="domesticcontract.DomesticContract.cp"></a>

#### cp

CP str

<a id="domesticcontract.DomesticContract.stikeprice"></a>

#### stikeprice

履約價 float

<a id="domesticcontract.DomesticContract.maxprice"></a>

#### maxprice

漲停價 float

<a id="domesticcontract.DomesticContract.minprice"></a>

#### minprice

跌停價 float

<a id="domesticcontract.DomesticContract.premium"></a>

#### premium

參考價 float

