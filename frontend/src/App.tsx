// src/App.tsx
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';

import { PrivateRoute } from './routes/PrivateRoute';
import UserProfile from './pages/UserProfile';

const App: React.FC = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/registro" element={<RegisterPage />} />
      <Route path="/perfil" element={<PrivateRoute><UserProfile /></PrivateRoute>} />
    </Routes>
  </BrowserRouter>
);

export default App;
