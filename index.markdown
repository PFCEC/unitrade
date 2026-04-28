---
layout: landing
title: 首頁
nav_exclude: true
---

* **`layout: landing`**: 這行最關鍵，告訴 Jekyll 這個頁面不要用預設的 `default` 或 `home` 版型，而是用我們剛剛建立的 `landing.html`。
* **`nav_exclude: true`**: 因為首頁已經有自己的導覽列了，這可以避免它又出現在某些自動生成的目錄中（視主題設定而定）。

#### 第三步：確認內頁連結

在 `landing.html` 中，我預設將「閱讀完整文件」的按鈕連結指向 `{{ '/docs/home/' | relative_url }}`。

**請確認您的第一頁文件路徑是否正確**。如果您的第一頁文件（例如原本的 `index.md` 內容）被您移動到了 `docs/intro.md`，請將該連結修正為對應的路徑。

### 常見問題：為什麼不用 `_includes`？

因為 `just-the-docs` 的預設 Layout (`default.html`) 已經包含了側邊欄 (`Sidebar`)、搜尋框和內容容器 (`main content`)。如果我們只是把這段 HTML 塞進原本的 `index.md` 內容裡，它會被限制在右邊那個小小的內容框框裡，沒辦法做到「全螢幕 Hero Section」的效果。

使用 **Custom Layout (`layout: landing`)** 可以讓我們完全跳脫主題的限制，獲得 100% 的畫面控制權，同時又不影響其他頁面的運作。這是最乾淨的做法。