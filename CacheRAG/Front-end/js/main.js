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

        // 確保後端回傳的數據包含 RAG 的來源資訊
        addMessage(data.answer, "bot-message", data.source, data.doc_names, data.doc_chunks);

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

function addMessage(text, className, source = "", docNames = [], docChunks = []) {
    let chatBox = document.getElementById("chat-box");

    // 建立外層容器
    let messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container");

    // 建立訊息框
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("message", className);
    messageDiv.innerText = text;

    messageContainer.appendChild(messageDiv);

    // 建立來源標籤
    if (source) {
        let sourceTag = document.createElement("span");
        sourceTag.classList.add("source-label", `source-${source.toLowerCase()}`);
        sourceTag.innerText = `來源: ${source}`;

        // 只有 RAG 來源可點擊，顯示命中的文件 & chunk
        if (source === "RAG" && docNames.length > 0 && docChunks.length > 0) {
            sourceTag.classList.add("clickable");
            sourceTag.addEventListener("click", function () {
                displayRAGInfo(docNames, docChunks);
            });
        }

        messageContainer.appendChild(sourceTag);
    }

    chatBox.appendChild(messageContainer);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 顯示 RAG 命中資訊
function displayRAGInfo(docNames, docChunks) {
    let ragInfo = document.getElementById("rag-info");

    // 清空舊資料
    document.getElementById("rag-doc-name").innerHTML = "";
    document.getElementById("rag-doc-chunk").innerHTML = "";

    // 顯示所有匹配的文件與 chunk
    let docText = `<strong>📄 文件:</strong> ${docNames.join(", ")}`;
    let chunkText = docChunks.map((chunk, i) => `<p><strong>🔹 Chunk ${i + 1}:</strong> ${chunk}</p>`).join("");

    document.getElementById("rag-doc-name").innerHTML = docText;
    document.getElementById("rag-doc-chunk").innerHTML = chunkText;

    ragInfo.classList.remove("hidden");
}

// 關閉 RAG 命中資訊
document.getElementById("close-rag-info").addEventListener("click", function () {
    document.getElementById("rag-info").classList.add("hidden");
});

function showLoading() {
    document.getElementById("loading").style.display = "block";
    document.getElementById("send-button").disabled = true;
}

function hideLoading() {
    document.getElementById("loading").style.display = "none";
    document.getElementById("send-button").disabled = false;
}

// 透過後端回應控制系統燈號
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
