# Unitrade API 文件網站

這個專案是以 **Jekyll + just-the-docs** 建立的 Unitrade API 文件站，內容包含：
- API 說明（國內/國外期貨帳務與委託、國內期貨行情等）
- 教學文件與 Notebook 範例
- 常見問題與錯誤代碼

## 專案結構

- `API/`：各 API 章節（`.md`）
- `教學/`：操作教學與範例 Notebook
- `說明/`：代碼、分類、維護時程與其他補充說明
- `常見問題/`：FAQ 文件
- `_layouts/`、`_includes/`：Jekyll 版型與共用片段
- `assets/`：自訂樣式與前端資源
- `_site/`：Jekyll 產生後的靜態網站（建置輸出）

## 需求環境

- Ruby（建議使用與 `github-pages` 相容版本）
- Bundler
- Node.js（若要使用 PDF 產生功能）

## 本機啟動（文件站）

1. 安裝 Ruby 套件
   - `bundle install`
2. 啟動 Jekyll
   - `bundle exec jekyll serve`
3. 開啟瀏覽器
   - `http://127.0.0.1:4000/unitrade/`

## 產生 PDF（選用）

此專案包含 `generate-pdf.js`，透過 Puppeteer 將網站頁面輸出 PDF。

1. 安裝 Node 套件
   - `npm install`
2. 先啟動 Jekyll（見上節）
3. 執行 PDF 產生
   - `node generate-pdf.js`

> 預設會輸出 `index.pdf`（依 `generate-pdf.js` 設定的 URL 與檔名規則）。

## 設定重點

請參考 `_config.yml`：
- `theme: just-the-docs`
- `baseurl: "/unitrade"`
- `url: "https://pfcec.github.io"`
- `repository: PFCEC/unitrade`

若部署路徑或網域有調整，請同步更新 `url` 與 `baseurl`。

## 維護建議

- 新增文件請放在對應目錄，並維持既有命名規則
- Notebook 範例建議放在 `教學/sample/`
- `_site/` 為產出目錄，不建議手動修改

## 授權與聯絡

- 聯絡信箱：`pfc.ec@uni-psg.com`
- Repository：`PFCEC/unitrade`
