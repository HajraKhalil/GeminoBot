document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("chat-input").addEventListener("keypress", handleKeyPress);

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

function sendMessage() {
    const inputField = document.getElementById("chat-input");
    const message = inputField.value.trim();
    if (!message) return;

    addMessage("user-message", message);
    inputField.value = "";

    fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: message }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            addMessage("bot-message", `Error: ${data.error} - ${data.details || "No details available"}`);
        } else {
            addMessage("bot-message", data.response || "No response from chatbot.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        addMessage("bot-message", `Error: ${error.message}`);
    });
}

function addMessage(className, text) {
    const chatBody = document.getElementById("chat-body");
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${className}`;
    messageDiv.textContent = text;
    
    chatBody.appendChild(messageDiv);

    const maxMessages = 10;
    const messages = chatBody.getElementsByClassName("message");
    if (messages.length > maxMessages) {
        chatBody.removeChild(messages[0]);
    }

    chatBody.scrollTop = chatBody.scrollHeight; // Auto-scroll
}