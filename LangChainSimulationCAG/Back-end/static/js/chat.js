document.addEventListener("DOMContentLoaded", function () {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");

    function appendMessage(text, isUser) {
        const msgDiv = document.createElement("div");
        msgDiv.classList.add("chat-message", isUser ? "user-message" : "bot-message");
        msgDiv.textContent = text;
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const text = userInput.value.trim();
        if (text) {
            // 顯示用戶訊息
            appendMessage(text, true);
            userInput.value = "";

            // 顯示「回覆中...」
            const loadingMessage = document.createElement("div");
            loadingMessage.classList.add("chat-message", "bot-message");
            loadingMessage.innerHTML = '<div class="spinner-border spinner-border-sm" role="status"><span class="visually-hidden">Loading...</span></div> 回覆中...';
            chatBox.appendChild(loadingMessage);

            // 發送請求到後端
            const response = await fetch("http://127.0.0.1:8000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();

            // 移除「回覆中...」，並顯示 AI 回應
            chatBox.removeChild(loadingMessage);
            appendMessage(data.response, false);
        }
    }

    sendBtn.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });
});
