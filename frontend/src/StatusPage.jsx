import React, { useEffect, useState } from 'react';

function MorphingLoader() {
  // Simple morphing loader animation
  return (
    <div className="w-8 h-8 bg-accent rounded-full animate-ping"></div>
  );
}

function StatusPage() {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(process.env.NEXT_PUBLIC_API_BASE_URL + '/health')
      .then(res => res.json())
      .then(data => {
        setStatus(data.status);
        setLoading(false);
      })
      .catch(() => {
        setStatus('error');
        setLoading(false);
      });
  }, []);

  return (
    <div className="max-w-lg mx-auto bg-surface rounded shadow p-6 dark:bg-secondary text-center">
      <h2 className="text-2xl font-bold mb-4">System Status</h2>
      {loading ? <MorphingLoader /> : (
        <div>
          <div className={status === 'ok' ? 'text-green-400' : 'text-red-400'}>
            Backend: {status === 'ok' ? 'Online' : 'Offline'}
          </div>
        </div>
      )}
    </div>
  );
}

export default StatusPage; 