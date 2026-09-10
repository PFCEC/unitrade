---  
nav_order: 0
parent: API Reference  
title: "unitrade"
--- 
<link rel="stylesheet" href="/assets/css/just-the-docs-custom.css">
統一期貨API元件

<a id="unitrade.LoginResponse"></a>

## LoginResponse Objects

```python
@dataclass
class LoginResponse()
```

登入回覆物件

<a id="unitrade.LoginResponse.ok"></a>

#### ok

是否成功

<a id="unitrade.LoginResponse.error"></a>

#### error

錯誤訊息

<a id="unitrade.Unitrade"></a>

## Unitrade Objects

```python
class Unitrade()
```

<a id="unitrade.Unitrade.login_status_flag"></a>

#### login\_status\_flag

登入旗標 <br/> True:登入 <br/> False:未登入

<a id="unitrade.Unitrade.test_mode"></a>

#### test\_mode

是否測試環境  <br/> True:測試環境 <br/>  False:正式環境

<a id="unitrade.Unitrade.dtrade"></a>

#### dtrade

內期交易元件(必需登入才可以使用)

<a id="unitrade.Unitrade.ftrade"></a>

#### ftrade

外期交易元件(必需登入才可以使用)

<a id="unitrade.Unitrade.dquote"></a>

#### dquote

內期報價元件(必需登入才可以使用)

<a id="unitrade.Unitrade.fquote"></a>

#### fquote

外期報價元件(必需登入才可以使用)

<a id="unitrade.Unitrade.squote"></a>

#### squote

現貨報價元件(必需登入才可以使用)

<a id="unitrade.Unitrade.daccount"></a>

#### daccount

內期帳務元件(必需登入才可以使用)

<a id="unitrade.Unitrade.faccount"></a>

#### faccount

外期帳務元件(必需登入才可以使用)

<a id="unitrade.Unitrade.on_error"></a>

#### on\_error

錯誤事件

<a id="unitrade.Unitrade.login"></a>

#### login

```python
def login(url, userid, password, ca_path, ca_password) -> LoginResponse
```

登入
##### 參數  

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| url|str | 主機 |
| userid | str | 登入帳號 |
| password | str | 登入密碼 |
| ca_path | str | 憑證路徑 |  
| ca_password | str | 憑證密碼 |

##### 回傳值 LoginResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True 成功 <br>False 失敗 |
| str | 錯誤訊息 |

##### 範例
```python 
response = unitrade.login(
    "https://test167.pfctrade.com", "登入帳號", "登入密碼", '憑證路徑', '憑證密碼')
# 憑證路徑可以是絕對路徑或相對路徑，必須是.pfx檔案
# 憑證密碼是憑證的密碼
# 登入成功後，會返回 LoginResponse(ok=True, error='')，失敗則返回 LoginResponse(ok=False, error='錯誤訊息')  
```

<a id="unitrade.Unitrade.logout"></a>

#### logout

```python
def logout()
```

登出
##### 範例
```python
unitrade.logout()
```

<a id="unitrade.Unitrade.get_domestic_products"></a>

#### get\_domestic\_products

```python
def get_domestic_products()
```

取得內期商品檔
##### 回傳值 DomesticProducts

| 型別 | 說明 |
| ------ | ------------- |
| dict | 內期商品代碼對應 DomesticProduct 的字典 |
| key | str | 商品代碼 |
| value | DomesticProduct | 商品資料 |

##### 範例
```python
domestic_products = unitrade.get_domestic_products() 
# {'TXF': DomesticProduct(kind_id='TXF', name='臺指', stock_id='', subtype='I', contract_size=200, strike_price_decimal_locator=0),
#  'MXF': DomesticProduct(kind_id='MXF', name='小臺指', stock_id='', subtype='I', contract_size=50, strike_price_decimal_locator=0),
#  ......
# }
```

<a id="unitrade.Unitrade.get_foreign_products"></a>

#### get\_foreign\_products

```python
def get_foreign_products()
```

取得外期商品檔
##### 回傳值 ForeignProducts

| 型別 | 說明 |
| ------ | ------------- |
| dict | 外期商品代碼對應 ForeignProduct 的字典 |
| key | str | 交易所|商品代碼 |
| value | ForeignProduct | 商品資料 |

##### 範例
```python
foreign_products = unitrade.get_foreign_products()
# {'CBT|10Y': ForeignProduct(exchange='CBT', symbol='10Y', type='F', name='微型 10 年收益率期貨', shortname='微型十年收益', country='USA', currency='USD'), 
#  'CBT|2YY': ForeignProduct(exchange='CBT', symbol='2YY', type='F', name='微型2年收益率期貨', shortname='微型2年收益', country='USA', currency='USD'),            
#  ......
# }
```

<a id="unitrade.Unitrade.get_exchanges"></a>

#### get\_exchanges

```python
def get_exchanges()
```

取得外期交易所
##### 回傳值 EXCHANGE

| 型別 | 說明 |
| ------ | ------------- |
| dict | 外期交易所代碼對應 EXCHANGE 的字典 |
| key | str | 交易所代碼 |
| value | EXCHANGE | 交易所資料 |

##### 範例
```python
exchanges = unitrade.get_exchanges()
# {'CME': EXCHANGE(exchange='CME', name='芝加哥商品交易所', country='USA', currency='USD', shortname='CME'),
#  'CBT': EXCHANGE(exchange='CBT', name='芝加哥期貨交易所', country='USA', currency='USD', shortname='CBOT'),
#  ......
# }
```

<a id="unitrade.Unitrade.get_domestic_contracts"></a>

#### get\_domestic\_contracts

```python
def get_domestic_contracts(symbol, type) -> DomesticContractResponse
```

取得內期合約檔
##### 參數  

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| symbol | str | 商品代碼 |
| type | str | 類別<br/> F:期貨<br/> O:選擇權 |

##### 回傳值 DomesticContractResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True: 成功 <br/>False: 失敗 |
| str | 錯誤訊息 |
| list[DomesticContract] | 商品合約資料 |

##### 範例
```python
response = unitrade.get_domestic_contracts("TXF", "F") 
# [DomesticContract(prod_id='TXFK5', month='202511', cp=None, stikeprice=0, maxprice=28360, minprice=23204, premium=25782, divdate='20251119'),
#  DomesticContract(prod_id='TXFL5', month='202512', cp=None, stikeprice=0, maxprice=29317, minprice=23987, premium=26652, divdate='20251217'),
#  ......] 
```

<a id="unitrade.Unitrade.get_foreign_contracts"></a>

#### get\_foreign\_contracts

```python
def get_foreign_contracts(exchange, symbol, type) -> ForeignContractResponse
```

取得外期商品檔
##### 參數

| 參數 | 型別 | 說明 |
| ------ | ------ | ------------- |
| exchange | str | 交易所 |
| symbol |str | 商品 |    
| type | str | 類別<br/> F:期貨<br/> O:選擇權 |

##### 回傳值 ForeignContractResponse

| 型別 | 說明 |
| ------ | ------------- |
| bool | True:成功 <br/> False:失敗 |
| str | 錯誤訊息 |
| List[ForeignContract] | 商品合約資料 |

##### 範例
```python
response = unitrade.get_foreign_contracts("CME", "NQ", "F")
# ForeignContractResponse(ok=True, error='', data=[
#  ForeignContract(exchange='CME', symbol='NQ', type='F', monthyear='202512', strikeprice='0.0000000', cp='', lasttradedate='20251219', firsttradedate='20231215', deliverydate='20251219'),
#  ForeignContract(exchange='CME', symbol='NQ', type='F', monthyear='202603', strikeprice='0.0000000', cp='', lasttradedate='20260321', firsttradedate='20251016', deliverydate='20260321'),            
#  ...... )
response = unitrade.get_foreign_contracts("CME", "ADO", "O")
# ForeignContractResponse(ok=True, error='', data=[
#  ForeignContract(exchange='CME', symbol='ADO', type='O', monthyear='202511', strikeprice='3150.0000000', cp='C', lasttradedate='20251107', firsttradedate='20211206', deliverydate='20251110'),
#  ForeignContract(exchange='CME', symbol='ADO', type='O', monthyear='202511', strikeprice='3150.0000000', cp='P', lasttradedate='20251107', firsttradedate='20211206', deliverydate='20251110'),
#  ...... )
```

<a id="unitrade.Unitrade.get_accounts"></a>

#### get\_accounts

```python
def get_accounts()
```

取得交易帳號

##### 回傳值 List[str]

| 型別 | 說明 |
| ------ | ------------- |
| List[str] | 交易帳號清單 |

##### 範例
```python
accounts = unitrade.get_accounts()
# ['12345678', '87654321', ...]  # 返回帳號清單
```

<a id="unitrade.Unitrade.get_domestic_product_info"></a>

#### get\_domestic\_product\_info

```python
def get_domestic_product_info(product) -> DomesticProductInfoResponse
```

查詢內期商品資訊。

**Arguments**:

- `product` _str_ - 商品代碼，例如 TXF。
  

**Returns**:

- `DomesticProductInfoResponse` - 查詢結果。
  
  ##### 回傳值 DomesticProductInfoResponse
  
  | 型別 | 說明 |
  | ------ | ------------- |
  | bool | ok：是否查詢成功 |
  | str | error：錯誤訊息，成功時為空字串 |
  | List[DomesticProductInfo] | data：內期商品資訊清單，查詢失敗時為 None |
  
  ##### DomesticProductInfo 欄位
  
  | 型別 | 說明 |
  | ------ | ------------- |
  | str | product_type：商品類別，1 為單式期貨，2 為單式選擇權 |
  | str | product_code：商品代號，例如 TXF |
  | str | contract_type：契約種類；I 指數類、R 利率類、B 債券類、C 商品類、S 股票類、E 匯率類 |
  | str | contract_size：合約大小 |
  | str | order_decimal_places：委託價格小數位數 |
  | str | name：商品名稱 |
  | str | stock_code：股票代號，例如 2330 |
  | str | initial_margin：交易保證金，僅期貨商品適用 |
  | str | currency：交易幣別 |
  | str | maintenance_margin：維持保證金，僅期貨商品適用 |
  | Optional[float] | tickvalue：最小跳動點數；查無 TickData 設定時為 None |
  

**Example**:

  response = unitrade.get_domestic_product_info("TXF")
  `DomesticProductInfoResponse`(ok=True, error='', data=[DomesticProductInfo(product_type='1', product_code='TXF', contract_type='I', contract_size='200', order_decimal_places='2', name='臺指', stock_code='', initial_margin='636000', currency='NTT', maintenance_margin='488000', tickvalue=1.0)])

