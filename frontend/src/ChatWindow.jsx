import React, { useState, useRef, useEffect } from 'react';
import clsx from 'clsx';

function AnimatedLoader() {
  // Animated ellipsis loader
  return <span className="inline-block animate-pulse">...</span>;
}

function ChatWindow() {
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hello! How can I help you?', timestamp: new Date() }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = { sender: 'user', text: input, timestamp: new Date() };
    setMessages(msgs => [...msgs, userMsg]);
    setInput('');
    setLoading(true);
    // Simulate streaming response
    let botText = '';
    for (const chunk of ['Sure, ', 'let me ', 'think', '...', ' Done!']) {
      await new Promise(r => setTimeout(r, 400));
      botText += chunk;
      setMessages(msgs => [
        ...msgs.slice(0, -1),
        { sender: 'bot', text: botText, timestamp: new Date() }
      ]);
    }
    setLoading(false);
  };

  return (
    <div className="max-w-xl mx-auto bg-surface rounded shadow p-4 dark:bg-secondary">
      <div className="h-96 overflow-y-auto flex flex-col gap-2 mb-4">
        {messages.map((msg, i) => (
          <div key={i} className={clsx('flex items-end', msg.sender === 'user' ? 'justify-end' : 'justify-start')}>
            {msg.sender === 'bot' && (
              <span className="w-8 h-8 rounded-full bg-accent flex items-center justify-center mr-2 text-white">🤖</span>
            )}
            <div className={clsx('px-3 py-2 rounded-lg', msg.sender === 'user' ? 'bg-accent text-white' : 'bg-primary text-on-primary')}
                 style={{ maxWidth: '70%' }}>
              <div>{msg.text}</div>
              <div className="text-xs text-gray-400 mt-1 text-right">
                {msg.timestamp.toLocaleTimeString()}
              </div>
            </div>
            {msg.sender === 'user' && (
              <span className="w-8 h-8 rounded-full bg-gray-500 flex items-center justify-center ml-2 text-white">🧑</span>
            )}
          </div>
        ))}
        {loading && (
          <div className="flex items-center gap-2">
            <span className="w-8 h-8 rounded-full bg-accent flex items-center justify-center mr-2 text-white">🤖</span>
            <span className="text-accent"><AnimatedLoader /></span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <form className="flex gap-2" onSubmit={e => { e.preventDefault(); sendMessage(); }}>
        <input
          className="flex-1 px-3 py-2 rounded bg-background text-on-primary dark:bg-background border border-secondary focus:outline-none"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button
          type="submit"
          className="px-4 py-2 rounded bg-accent text-white font-bold hover:bg-sky-600 transition"
          disabled={loading}
        >
          Send
        </button>
      </form>
    </div>
  );
}

export default ChatWindow; 