const chatWindow = document.getElementById("chat-window");
const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const clearBtn = document.getElementById("clear-btn");

function addBubble(text, sender) {
  const bubble = document.createElement("div");
  bubble.className = `bubble ${sender}`;
  bubble.textContent = text;
  chatWindow.appendChild(bubble);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = messageInput.value.trim();
  if (!message) return;

  addBubble(message, "user");
  messageInput.value = "";

  addBubble("Typing...", "bot");
  const typingBubble = chatWindow.lastChild;

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await res.json();
    typingBubble.textContent = data.reply;
  } catch (err) {
    typingBubble.textContent = "Something went wrong. Please try again.";
  }
});

clearBtn.addEventListener("click", async () => {
  await fetch("/clear", { method: "POST" });
  chatWindow.innerHTML = "";
  addBubble("Conversation cleared. How can I help you?", "bot");
});
