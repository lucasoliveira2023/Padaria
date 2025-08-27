// src/App.tsx
import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Home from "./pages/Home";
import RegisterPage from "./pages/RegisterPage";


const App: React.FC = () => {
  return (
    <BrowserRouter>
     <Routes>
      {/* rota inicial */}
      <Route path="/" element={<Home />} />

      {/* login */}
      <Route path="/login" element={<LoginPage />} />

      {/* registro */}
      <Route path="/registro" element={<RegisterPage />} />
     </Routes>
    </BrowserRouter>
  );
};

export default App;
