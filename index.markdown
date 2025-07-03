---
layout: home
title: 事先準備
nav_order: 0
description: "pfcfpy"
permalink: /
---
 

## 1. 事先準備

### 1.1 開立統一期貨帳號
- 完成開立統一期貨帳號。若尚未開戶，請先進行開戶作業，並參閱統一期貨官網說明。

### 1.2 完成新戶密碼開通
- 完成新戶密碼的開通，並取得電腦憑證。
- 若尚未擁有電腦憑證，請至憑證e總管申請。

### 1.3 申請統一API開通測試
- 向營業員申請統一API開通測試，並取得測試通知的Email。

### 1.4 測試丟單
- 請操作API完成測試丟單。可以參考測試丟單範例[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/PFCEC/unitrade/blob/main/%E6%95%99%E5%AD%B8/sample/unitrade_Demo.ipynb)進行操作。


- <a href="./教學/sample/unitrade_Demo.ipynb" download>下載範例</a> 


### 1.5 開通正式API
- 通知您的營業員開通正式API，並取得正式開通的Email。

### 1.6 儲存憑證
- 取得您的憑證檔案和密碼。
- 將憑證檔案放置於程式執行目錄下。您的目錄結構應該類似於以下格式：

```
 ├── 您的程式.py
 └── XXXXXXXXXX.pfx
```

### 1.7 安裝 `unitrade` 套件
- 使用以下命令安裝 `unitrade` 套件：
```bash
pip install unitrade
```

- 支援Python版本: 3.7、3.8、3.9、3.10、3.11、3.12
- 支援 OS: Linux, macOS, Windows

### 1.8 開始使用
- 完成以上準備後，您可以開始使用API進行交易操作。

---

 