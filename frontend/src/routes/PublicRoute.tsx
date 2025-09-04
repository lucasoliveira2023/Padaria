// src/routes/PublicRoute.tsx
import { Navigate } from "react-router-dom";
import { useAuth } from '../hooks/useAuth';
import type { ReactNode } from "react";



export const PublicRoute = ({ children }: { children: ReactNode }) => {
    const { isAuthenticated } = useAuth();
    return isAuthenticated? <Navigate to="/" /> : <>{children}</>;
};