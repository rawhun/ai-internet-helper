import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import StatusPage from './StatusPage';
import ChatWindow from './ChatWindow';
import Auth from './Auth';

function App() {
  const [dark, setDark] = useState(() => localStorage.getItem('theme') === 'dark');

  useEffect(() => {
    if (dark) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }, [dark]);

  return (
    <Router>
      <div className="min-h-screen bg-background text-on-primary dark:bg-background dark:text-on-primary">
        <nav className="flex items-center justify-between p-4 bg-primary dark:bg-primary">
          <div className="flex gap-4">
            <Link to="/" className="font-bold text-accent">AI Chatbot</Link>
            <Link to="/status">Status</Link>
          </div>
          <button
            className="ml-4 px-2 py-1 rounded bg-secondary text-on-primary"
            onClick={() => setDark(d => !d)}
            aria-label="Toggle dark mode"
          >
            {dark ? '🌙' : '☀️'}
          </button>
        </nav>
        <main className="p-4">
          <Routes>
            <Route path="/" element={<ChatWindow />} />
            <Route path="/status" element={<StatusPage />} />
            <Route path="/auth" element={<Auth />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App; 