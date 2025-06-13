# 使用 GitHub Copilot Chat 開發  🚀
本指南將說明如何在 VS Code 中利用 GitHub Copilot Chat 來協助開發 FastAPI 專案，<br>
具體包含生成 requirements.txt、解釋程式碼，以及編寫單元測試。<br>

## 前置準備 🛠️<br>
在開始之前，請確保您已安裝以下工具：<br>

1. Visual Studio Code (VS Code)
2. GitHub Copilot Chat 擴充功能: 在 VS Code 擴充功能市場中搜尋並安裝。
3. Python 環境: 使用 venv 建立虛擬環境。
4. 將專案抓取至本地端

## 使用 Copilot Chat 目標 💬
### 1. 生成 requirements.txt 檔案
requirements.txt 檔案列出了您的專案所需的所有 Python 套件及其版本。<br>
Copilot Chat 可以根據您的專案程式碼自動生成它。

步驟：
- 在 VS Code 中打開您的 FastAPI 專案。
- 打開 Chat 視窗 (通常在側邊欄)。
- 在 Chat 輸入框中，輸入以下指令：
```chat
@workspace /fix generate requirements.txt for this project
```

Copilot Chat 會分析您的 main.py 檔案（以及其他相關 Python 檔案），並建議一個 requirements.txt 內容。

Copilot Chat 通常會提示您是否要將其輸出寫入一個新檔案。<br>
接受此提示，或者手動將其輸出複製並貼上到專案根目錄下的 requirements.txt 檔案中。


### 2. 解釋程式碼 (/explain)
Copilot Chat 的 /explain 指令可以幫助您理解程式碼片段的功能、邏輯和潛在問題。

步驟：
- 在您的 FastAPI 專案中，選取您想要解釋的任何程式碼片段。<br>
    例如，選取 main.py 中的 generate_fibonacci 函數。
- 右鍵點擊選取的程式碼，然後選擇 Copilot > Explain This，或者在 Chat 視窗中輸入：

```chat
@selection /explain
```

Copilot Chat 將在 Chat 視窗中提供對選定程式碼的詳細解釋，包括其目的、參數、返回值以及如何運作。<br>
這對於理解不熟悉的程式碼或學習新的程式碼模式非常有幫助。

### 3. 編寫單元測試
單元測試對於確保您的應用程式的穩定性和正確性至關重要。<br>
Copilot Chat 可以根據您的函數或類別自動生成單元測試的範本。

步驟：
- 在您的 FastAPI 專案中，打開您想要編寫單元測試的 main.py
- 在 Chat 視窗中，輸入以下指令並替換 <檔案或函數名> 為您想要測試的目標：

```chat
@file /tests main.py
```
或者更具體地選取想要函數後輸入：
```chat
@selection /tests
```

將生成的測試代碼複製並貼上到您的專案中的適當測試檔案（例如 test_main.py）。<br>
運行測試: 確保您已安裝 pytest (pip install pytest)，然後在終端中運行測試：
```terminal
pytest
```