import { useEffect, useState } from 'react';

function App() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    fetch("/api/health")
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(() => setStatus("unreachable"));
  }, []);

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-900 text-white">
      <h1 className="text-4xl font-bold mb-4">PulseView</h1>
      <p className={`text-xl ${status === "healthy" ? "text-green-400" : "text-red-400"}`}>
        Cluster Status: {status}
      </p>
    </div>
  );
}

export default App;