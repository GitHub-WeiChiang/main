document.getElementById("temperature").addEventListener("input", function () {
    document.getElementById("temp-value").innerText = this.value;
});

async function sendMessage() {
    let userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    addMessage(userInput, "user-message");

    // 顯示 Loading
    showLoading();

    let topK = document.getElementById("top-k").value;
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
        addMessage(data.answer, "bot-message");

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

    document.getElementById("user-input").value = "";
}

function addMessage(text, className) {
    let chatBox = document.getElementById("chat-box");
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("message", className);
    messageDiv.innerText = text;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showLoading() {
    document.getElementById("loading").style.display = "block";
}

function hideLoading() {
    document.getElementById("loading").style.display = "none";
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
