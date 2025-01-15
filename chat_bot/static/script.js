document.getElementById("send").addEventListener("click", function () {
    const userInput = document.getElementById("user-input").value;
    const chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById("user-input").value = "";

    fetch(`/chat?msg=${userInput}`)
        .then((response) => response.json())
        .then((data) => {
            chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
            chatbox.scrollTop = chatbox.scrollHeight;
        });
});
