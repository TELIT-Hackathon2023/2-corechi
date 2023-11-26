// app.js

document.addEventListener("DOMContentLoaded", function () {
    // This event is triggered when the DOM has been fully loaded

function createChatMessage(sender, message, time, isUser) {
    const messageContainer = document.createElement("div");
    const profilePicture = document.createElement("img");
    const messageContent = document.createElement("div");
    const messageText = document.createElement("p");
    const messageTime = document.createElement("p");

    profilePicture.classList.add("w-8", "h-8", "rounded-full");
    profilePicture.src = "https://unsplash.com/photos/1_CMoFsPfso";
    profilePicture.alt = "Profile picture";

    messageContent.classList.add("p-2", "rounded-lg");

    messageText.classList.add("text-sm");
    messageText.textContent = message;

    messageTime.classList.add("text-xs", "text-gray-500");
    messageTime.textContent = time;

    messageContent.appendChild(messageText);
    messageContent.appendChild(messageTime);

    messageContainer.appendChild(profilePicture);
    messageContainer.appendChild(messageContent);

    // Adjust the positioning based on whether it's a user message
    if (isUser) {
        messageContainer.classList.add("flex", "items-end", "space-x-2", "mb-2", "user-message", "self-end");
    } else {
        messageContainer.classList.add("flex", "items-end", "space-x-2", "mb-2", "bot-message", "self-start");
    }

    return messageContainer;
}

    // Function to handle the creation of a new chat message
    function handleSendMessage() {
        const messageInput = document.getElementById("messageInput");
        const chatMessages = document.getElementById("chatMessages");

        // Get the user's input from the input bar
        const userMessage = messageInput.value.trim();

        // Check if the input is not empty
        if (userMessage !== "") {
            // Get the current time
            const currentTime = new Date().toLocaleTimeString();

            // Create a new user message
            const newUserMessage = createChatMessage("You", userMessage, currentTime, true);

            // Append the new user message to the chat window
            chatMessages.appendChild(newUserMessage);

            // Clear the input bar
            messageInput.value = "";
        }
    }

    // Event listener for the "Send Message" button
    document.getElementById("sendMessageBtn").addEventListener("click", handleSendMessage);

    // Event listener for pressing Enter key in the input bar
    document.getElementById("messageInput").addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            handleSendMessage();
        }
    });

    // Function to get a random welcome message
    function getRandomWelcomeMessage() {
        const welcomeMessages = [
            "Welcome! How can I assist you today?",
            "Hello! What can I help you with?",
            "Greetings! How may I be of service?",
            "Hi there! What brings you here?",
            "Welcome aboard! What can I do for you?",
            "Hello! How can I make your day better?",
            "Greetings! Ready to chat?",
            "Hi! What can I help you achieve today?",
            "Welcome! Let's chat about anything you'd like.",
            "Hello! How may I assist you right now?"
        ];

        const randomIndex = Math.floor(Math.random() * welcomeMessages.length);
        return welcomeMessages[randomIndex];
    }

    // Function to handle the creation of a new chat
    function handleNewChat() {
        const chatHistoryList = document.getElementById("chatHistoryList");

        // Get the current date in the specified format
        const currentDate = new Date().toLocaleDateString("en-US", {
            weekday: "long",
            year: "numeric",
            month: "short",
            day: "numeric"
        });

        // Example: Adding a new chat to the chat history
        const newChatHistoryItem = document.createElement("div");
        newChatHistoryItem.classList.add("flex", "items-center", "space-x-3");

        const profilePicture = document.createElement("img");
        profilePicture.classList.add("w-10", "h-10", "rounded-full");
        profilePicture.src = "https://unsplash.com/photos/1_CMoFsPfso";
        profilePicture.alt = "Profile picture";

        const chatInfo = document.createElement("div");

        const chatName = document.createElement("p");
        chatName.classList.add("font-medium");
        chatName.textContent = currentDate;

        const welcomeMessage = getRandomWelcomeMessage();

        const lastMessage = document.createElement("p");
        lastMessage.classList.add("text-sm", "text-gray-600");
        lastMessage.textContent = welcomeMessage;

        chatInfo.appendChild(chatName);
        chatInfo.appendChild(lastMessage);

        newChatHistoryItem.appendChild(profilePicture);
        newChatHistoryItem.appendChild(chatInfo);

        chatHistoryList.appendChild(newChatHistoryItem);

        // Clear the chat window
        const chatMessages = document.getElementById("chatMessages");
        chatMessages.innerHTML = '';

        // Add the welcome message to the chat window
        const welcomeMessageInChat = createChatMessage("Bot", welcomeMessage, "Just now", false);
        chatMessages.appendChild(welcomeMessageInChat);
    }

    // Function to toggle dark mode
    function toggleDarkMode() {
        const body = document.body;
        body.classList.toggle("dark-mode");

        // You can add additional logic here to save the user's preference (e.g., in local storage)
    }

    // Event listener for the dark mode switch
    document.getElementById("darkModeSwitch").addEventListener("change", toggleDarkMode);

    // Event listener for the "New Chat" button
    document.getElementById("newChatBtn").addEventListener("click", handleNewChat);

    // Trigger the initial welcome message and chat creation
    handleNewChat();
});
