function sendMessage() {
    var userInput = document.getElementById("userInput").value;
    if (userInput.trim() === "") return; // Do not send empty messages
    var loadingMessageElement = displayLoadingMessage();
    
    // Send user input to server
    fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        updateChatbotMessage(loadingMessageElement, data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    document.getElementById("userInput").value = ""; // Clear input field after sending
}

function displayLoadingMessage() {
    var messageContainer = document.getElementById("responseContainer");
    var loadingMessageElement = document.createElement("p");
    loadingMessageElement.textContent = "Loading response...";
    messageContainer.appendChild(loadingMessageElement);
    return loadingMessageElement;
}

function updateChatbotMessage(element, message) {
    element.textContent = "Chatbot: " + message;
}

function checkEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}
