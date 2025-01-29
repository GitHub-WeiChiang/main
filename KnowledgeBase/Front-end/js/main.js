document.getElementById("temperature").addEventListener("input", function () {
    document.getElementById("temp-value").innerText = this.value;
});

let isComposing = false; // 記錄輸入法狀態

// 監聽輸入法開始（使用者輸入中文拼音）
document.getElementById("user-input").addEventListener("compositionstart", function () {
    isComposing = true;
});

// 監聽輸入法結束（使用者輸入完成並選擇中文字）
document.getElementById("user-input").addEventListener("compositionend", function () {
    isComposing = false;
});

// 監聽 Enter 鍵，避免 IME 組字時提前送出
document.getElementById("user-input").addEventListener("keydown", function (event) {
    if (event.key === "Enter" && !isComposing) {
        sendMessage();
    }
});

// 監聽「發送」按鈕點擊事件
document.getElementById("send-button").addEventListener("click", function () {
    sendMessage();
});

// 頁面載入時，確保系統預設為「開啟」
document.addEventListener("DOMContentLoaded", function () {
    updateSystemStatus(true);
});

async function sendMessage() {
    let userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    addMessage(userInput, "user-message");

    // 按下發送就立即清空輸入框
    document.getElementById("user-input").value = "";

    // 顯示 Loading
    showLoading();

    let topK = Math.max(1, parseInt(document.getElementById("top-k").value));
    let temperature = document.getElementById("temperature").value;

    try {
        let response = await fetch("http://localhost:8000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: userInput,
                top_k: parseInt(topK),
                temperature: parseFloat(temperature)
            })
        });

        let data = await response.json();

        // 來源標籤顯示在訊息框下方
        addMessage(data.answer, "bot-message", data.source);

        // 檢查後端是否回應系統狀態
        if (data.answer.includes("系統已關閉")) {
            updateSystemStatus(false);
        } else if (data.answer.includes("系統已開啟")) {
            updateSystemStatus(true);
        }

    } catch (error) {
        addMessage("發生錯誤，請稍後再試。", "bot-message error-message");
    } finally {
        hideLoading();
    }
}

function addMessage(text, className, source = "") {
    let chatBox = document.getElementById("chat-box");

    // 建立外層容器，讓訊息與來源標籤獨立
    let messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container");

    // 建立訊息框
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("message", className);
    messageDiv.innerText = text;

    messageContainer.appendChild(messageDiv);

    // 建立來源標籤（顯示在下方）
    if (source) {
        let sourceTag = document.createElement("div");
        sourceTag.classList.add("source-label", `source-${source.toLowerCase()}`);
        sourceTag.innerText = `來源: ${source}`;
        messageContainer.appendChild(sourceTag);
    }

    chatBox.appendChild(messageContainer);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showLoading() {
    document.getElementById("loading").style.display = "block";
    document.getElementById("send-button").disabled = true;
}

function hideLoading() {
    document.getElementById("loading").style.display = "none";
    document.getElementById("send-button").disabled = false;
}

// 透過後端回應控制系統燈號，並確保初始狀態為開啟
function updateSystemStatus(isOn) {
    let light = document.getElementById("status-light");
    let text = document.getElementById("status-text");

    if (isOn) {
        light.classList.remove("status-off");
        light.classList.add("status-on");
        text.innerText = "運行中";
    } else {
        light.classList.remove("status-on");
        light.classList.add("status-off");
        text.innerText = "停止";
    }
}
