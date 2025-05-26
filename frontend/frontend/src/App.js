// src/App.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [statuses, setStatuses] = useState([]);
  const [users, setUsers] = useState([]);
  const [formData, setFormData] = useState({ service_name: '', status: '' });

  const fetchStatuses = async () => {
    try {
      const res = await axios.get("http://localhost:8000/status/");
      setStatuses(res.data);
    } catch (err) {
      console.error("Error fetching statuses", err);
    }
  };

  const fetchUsers = async () => {
    try {
      const res = await axios.get("http://localhost:8000/external_users/");
      setUsers(res.data);
    } catch (err) {
      console.error("Error fetching users", err);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/status/", formData);
      setFormData({ service_name: '', status: '' });
      fetchStatuses();
    } catch (err) {
      console.error("Error posting status", err);
    }
  };

  useEffect(() => {
    fetchStatuses();
    fetchUsers();
  }, []);

  return (
    <div className="App">
      <h1>🛡️ Service Monitor</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Service Name"
          value={formData.service_name}
          onChange={(e) => setFormData({ ...formData, service_name: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Status"
          value={formData.status}
          onChange={(e) => setFormData({ ...formData, status: e.target.value })}
          required
        />
        <button type="submit">Add Status</button>
      </form>

      <h2>📝 Status List</h2>
      <ul>
        {statuses.map((s) => (
          <li key={s.id}>
            {s.timestamp} — <strong>{s.service_name}</strong>: {s.status}
          </li>
        ))}
      </ul>

      <h2>🌐 External Users</h2>
      <ul>
        {users.map((u, i) => (
          <li key={i}>{JSON.stringify(u)}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
