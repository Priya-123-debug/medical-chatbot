import { useState, useRef, useEffect } from "react";
import { askQuestion } from "./api";

export default function Chat() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatBoxRef = useRef(null);

  useEffect(() => {
    if (chatBoxRef.current) {
      chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
    }
  }, [messages, loading]);

  const handleSend = async () => {
    if (!question.trim() || loading) return;

    const userMsg = { role: "user", text: question };
    setMessages((prev) => [...prev, userMsg]);
    setQuestion("");
    setLoading(true);

    try {
      const answer = await askQuestion(question);
      setMessages((prev) => [...prev, { role: "bot", text: answer }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "Sorry, something went wrong. Please try again." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-container">
      <h2>🩺 Medical Chatbot</h2>

      <div className="chat-box" ref={chatBoxRef}>
        {messages.length === 0 && (
          <div className="empty-state">Ask me a medical question to get started.</div>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={msg.role === "user" ? "user" : "bot"}>
            {msg.text}
          </div>
        ))}
        {loading && <div className="bot typing">Typing...</div>}
      </div>

      <div className="input-box">
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask a medical question..."
          disabled={loading}
        />
        <button onClick={handleSend} disabled={loading || !question.trim()}>
          {loading ? "..." : "Send"}
        </button>
      </div>
    </div>
  );
}