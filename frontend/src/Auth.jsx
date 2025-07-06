import React, { useState } from 'react';

function Auth() {
  const [mode, setMode] = useState('login');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [token, setToken] = useState(localStorage.getItem('jwt') || '');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const res = await fetch(process.env.NEXT_PUBLIC_API_BASE_URL + `/auth/${mode}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      const data = await res.json();
      if (res.ok && data.token) {
        setToken(data.token);
        localStorage.setItem('jwt', data.token);
      } else {
        setError(data.error || 'Auth failed');
      }
    } catch (err) {
      setError('Network error');
    }
  };

  const logout = () => {
    setToken('');
    localStorage.removeItem('jwt');
  };

  if (token) {
    return (
      <div className="max-w-md mx-auto bg-surface rounded shadow p-6 dark:bg-secondary text-center">
        <div className="mb-4">Logged in as <span className="font-bold">{email || 'user'}</span></div>
        <button className="px-4 py-2 bg-accent text-white rounded" onClick={logout}>Logout</button>
      </div>
    );
  }

  return (
    <div className="max-w-md mx-auto bg-surface rounded shadow p-6 dark:bg-secondary">
      <div className="flex justify-center mb-4">
        <button
          className={`px-4 py-2 rounded-l ${mode === 'login' ? 'bg-accent text-white' : 'bg-secondary text-on-primary'}`}
          onClick={() => setMode('login')}
        >Login</button>
        <button
          className={`px-4 py-2 rounded-r ${mode === 'signup' ? 'bg-accent text-white' : 'bg-secondary text-on-primary'}`}
          onClick={() => setMode('signup')}
        >Sign Up</button>
      </div>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          className="px-3 py-2 rounded bg-background text-on-primary border border-secondary focus:outline-none"
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
        />
        <input
          className="px-3 py-2 rounded bg-background text-on-primary border border-secondary focus:outline-none"
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        {error && <div className="text-red-400 text-sm">{error}</div>}
        <button className="px-4 py-2 bg-accent text-white rounded" type="submit">
          {mode === 'login' ? 'Login' : 'Sign Up'}
        </button>
      </form>
    </div>
  );
}

export default Auth; 