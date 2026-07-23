# AI 輔助開發

本章節說明如何使用本專案提供的 **Claude Code plugin** 與 **LLM 文件**，協助第一次使用 Unitrade API 的開發者快速理解元件、產生範例程式、排查錯誤，並建立較安全的開發流程。

{: .warning }
> **重要安全提醒**  
> AI 產生的下單程式碼僅能作為 API 串接範例，不代表任何交易建議。執行任何可能送出委託的程式前，請務必確認登入環境、帳號、商品、買賣別、價格別、數量與委託條件。  
> 即使程式碼包含防呆開關，也請務必在**完全隔離的測試環境**中執行，並由開發者人工逐行審核後再上線實盤。

## 前置準備

使用本章節的 AI 輔助功能前，請先完成以下準備：

1. **安裝 Claude Code CLI**（使用 plugin 時需要）
   - 需要 Node.js 18 以上版本
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

2. **準備 Unitrade 開發環境**
   - `pip install unitrade`
   - 下載並放置 `.pfx` 憑證檔案
   - 建議先申請**測試帳號**進行開發

3. **Clone 本專案**（使用 plugin 時需要）
   ```powershell
   git clone https://github.com/PFCEC/unitrade.git
   cd unitrade
   ```

> **注意**：Claude Code plugin 與 `LLM.txt` / `llms-full.txt` 為本專案即將提供的 AI 輔助資源。若目前尚未看到 `.claude-plugin/` 與 `skills/` 資料夾，請先使用傳統方式閱讀 `開始.md` 與 `API/` 文件入門。

## 可用資源

本專案提供兩種 AI 輔助方式：

| 資源                  | 適合情境                                   | 路徑                                      |
|-----------------------|--------------------------------------------|-------------------------------------------|
| Claude Code plugin    | 在本機專案內互動式開發、產生範例、查元件用途 | `.claude-plugin/plugin.json`<br>`skills/unitrade-quickstart/` |
| `LLM.txt`             | 給 LLM 快速理解專案、元件地圖與常用範例     | `LLM.txt`                                 |
| `llms-full.txt`       | 給支援長上下文的 LLM 讀完整文件、API、教學與 notebook 範例 | `llms-full.txt`                           |

## 使用 Claude Code Plugin

Claude Code plugin 適合在本機專案中使用。它會把 Unitrade API 的元件說明、教學範例與排錯規則整理成可呼叫的 skill，讓 Claude 可以更快判斷該使用哪個元件與方法。

### 1. 安裝與啟動 Plugin

**從本機載入（推薦開發時使用）**

```powershell
# 在 unitrade 專案根目錄執行
claude --plugin-dir .
```

啟動後，可用以下指令呼叫 skill：

```text
/unitrade-onboarding:unitrade-quickstart 我要第一次使用內期行情
```

> **小提醒**：若更新 plugin 內容後 Claude Code 沒有立即生效，請在 Claude Code 內執行 `/reload-plugins`，或關閉後重新用 `--plugin-dir` 啟動。

### 2. 常用提問範例

**第一次登入與取得帳號清單：**
```text
/unitrade-onboarding:unitrade-quickstart 幫我產生 Unitrade 第一次登入與取得帳號清單的範例
```

**查詢行情：**
```text
/unitrade-onboarding:unitrade-quickstart 我想查詢 TXF 內期行情，請告訴我應該用哪個元件並給我最小範例
```

**下單前安全檢查：**
```text
/unitrade-onboarding:unitrade-quickstart 我要做內期測試下單，請先列出需要確認的欄位，再產生有防呆開關的範例
```

**錯誤排除：**
```text
/unitrade-onboarding:unitrade-quickstart 登入時出現憑證有誤，請幫我排查可能原因
```

### 3. Plugin 會協助的事情

- 判斷應使用 `api.dquote`、`api.fquote`、`api.squote`、`api.dtrade`、`api.ftrade`、`api.daccount` 或 `api.faccount`
- 根據教學範例產生可複製的最小程式碼
- 在下單範例中提醒註冊 `on_reply`、`on_match` callback
- 對可能送單的程式加入確認步驟或防呆開關（例如 `CONFIRM_SEND_ORDER`）
- 根據錯誤訊息查找常見原因（URL、帳密、憑證、尚未連線、維護時段、參數格式錯誤等）

## 使用 LLM 文件輔助開發

若不使用 Claude Code，也可以把 `LLM.txt` 或 `llms-full.txt` 提供給 ChatGPT、Claude、Gemini、Grok 或其他支援文件上傳的 LLM 使用。

### 選擇文件

| 文件            | 用法建議                                      | 推薦情境                     |
|-----------------|-----------------------------------------------|------------------------------|
| `LLM.txt`       | 內容較短，包含元件地圖、常用流程與安全規則     | 快速入門、日常查詢           |
| `llms-full.txt` | 包含完整 API reference、所有教學與 notebook 範例 | 複雜問題、需要完整 context   |

### 建議提示詞範例

**快速入門：**
```text
請先閱讀我提供的 LLM.txt。我要第一次使用 Unitrade API，請用繁體中文教我完成登入、檢查登入結果、取得帳號清單，並指出下一步可以查哪些元件。
```

**產生特定元件範例：**
```text
請根據 llms-full.txt 中的 Unitrade 文件，產生一個查詢現貨股票 2330 即時行情與基本資料的 Python 範例。請使用 api 變數，並檢查 response.ok。
```

**錯誤排查：**
```text
請根據我提供的文件排查這個錯誤：「尚未連線」。請列出最可能原因、檢查順序，以及可以加入程式中的 debug print。
```

**下單安全檢查：**
```text
我要建立內期測試下單範例。請先列出必須確認的欄位與風險，再產生預設不會送單、需要手動打開 CONFIRM_SEND_ORDER 的程式。
```

**使用小技巧：**
- Claude.ai：建議建立 Project 並上傳 `llms-full.txt`
- ChatGPT / Gemini：可直接上傳檔案或貼上內容
- 需要長上下文時優先使用 `llms-full.txt`

## 建議開發流程

1. **先確認要用哪個元件**  
   使用 `LLM.txt` 或 Claude plugin 判斷應使用 `api.dquote` / `api.ftrade` 等。

2. **產生最小可執行範例**  
   只做登入、查詢或回傳物件檢查，先確認 `api.login_response.ok` 為 True。

3. **對照 API 文件確認欄位**  
   參考 `API/` 目錄下的 `dquote.md`、`dtrade_data.md` 等，確認欄位名稱與型別。

4. **逐步加入進階功能**  
   再加入訂閱 callback、查詢條件或下單物件。

5. **加入安全機制**  
   對任何可能送單的程式加上防呆開關、測試環境提示與明確的 `print` 輸出。

6. **發生錯誤時的排查順序**  
   先查 `常見問題/` → `說明/錯誤代碼.md` → `說明/系統維護時程與時間格式說明.md`

> **強烈建議**：所有下單相關程式碼，務必先在測試環境完整跑過，並加入人工確認機制後再考慮實盤使用。

## 維護 LLM 文件

文件內容更新後，建議同步更新以下項目：

- `LLM.txt`：摘要版 LLM 入口（元件地圖 + 常用流程 + 安全規則）
- `llms-full.txt`：完整文件彙整版
- `skills/unitrade-quickstart/references/`：Claude plugin 的參考資料來源

**維護建議：**
- 新增 API、教學或常見問題時，請同步更新上述三處
- 建議未來可開發自動化 script，從 `API/`、`教學/`、`說明/` 目錄自動產生 `LLM.txt` 與 `references/` 內容，減少手動同步錯誤

## 目前狀態與貢獻

- 本章節描述的 AI 輔助功能為本專案的實驗性／進階支援功能
- 目前 plugin 與 LLM 文件正在準備中，預計隨後續版本一併開放
- 歡迎社群貢獻 plugin skill、範例提示詞，或協助優化 `LLM.txt` 內容

**參考資源：**
- [Claude Code Plugins 官方文件](https://code.claude.com/docs/en/plugins)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- 本專案 `開始.md` 與 `API/` 文件

 