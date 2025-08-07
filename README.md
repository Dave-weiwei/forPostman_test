# 📘 Postman API 測試練習專案（Flask + JWT）

本專案是一個 API 測試練習平台，使用 Python Flask 架設後端，實作基本帳號系統與權限驗證，並透過 Postman 撰寫完整測試流程，支援帳號註冊、登入、Token 驗證、角色控制、書籍查詢等功能。

---

## 🚀 線上測試環境（Render）

你可以直接使用以下部署網址進行 API 測試：

- **Base URL**：`https://forpostman-test.onrender.com`

### 🔐 測試帳號

| 角色     | 帳號             | 密碼        |
| -------- | ---------------- | ----------- |
| 管理員   | `admin@test.com` | `Admin123`  |
| 一般會員 | `davetest2`      | `davetest2` |

---

## 📁 專案結構

```bash
📁 Postman_test/
├── app.py # Flask API 主程式
├── requirements.txt # 套件需求列表
├── templates/
│ └── index.html # 首頁簡介（靜態說明）
├── tests/ # Postman 測試資源
│ ├── postman_collection.json # Postman 測試流程
│ └── postman_environment.json # 測試用環境變數（baseURL、帳密等）
```

---

## ✅ Postman 測試涵蓋內容

### 👤 會員系統

- ✅ 註冊成功 / 空白欄位 / 帳號重複
- ✅ 登入成功 / 帳號錯誤 / 密碼錯誤
- ✅ 自動取得 JWT token 並儲存為變數

### 🔐 JWT 權限驗證

- ✅ 未登入存取 `/profile`（應回 401）
- ✅ 一般會員登入後存取 `/profile`
- ✅ 管理員登入後存取 `/profile`

### 📚 書籍管理

- ✅ 查詢書籍 `/books?page=1&limit=10`
- ✅ 上傳書籍封面（目前為未實作 API，驗證回傳 501）
- ✅ 權限驗證（一般會員 / 未登入應無法上傳）

---

## 🛠 使用方式（Postman）

1. 開啟 Postman，匯入 `tests/postman_collection.json`
2. 可選擇匯入 `tests/postman_environment.json`
3. 選擇對應環境，執行測試流程
4. 測試時會自動登入並儲存 token
5. 可搭配 Collection Runner 跑完整自動化測試

---

## 🧪 技術重點

- **後端框架**：Flask
- **授權機制**：JWT Token（PyJWT）
- **測試工具**：Postman（含 Pre-request Script、驗證區）
- **部署平台**：Render（含免費 HTTPS）

---

## 📌 補充

本專案僅做 API 測試練習用途，尚未串接資料庫，目前使用記憶體暫存帳號資料，適合用於：

- Postman 測試實作練習
- JWT 權限測試流程理解
- 自動化測試流程展示
