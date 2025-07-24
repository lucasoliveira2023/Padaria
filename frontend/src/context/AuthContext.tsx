import { createContext, useContext, useEffect, useState } from "react";
import api from "../services/api";


interface AuthContextType {
    isAuthenticated: boolean;
    token: string | null;
    signIn: (email: string, password: string) => Promise<boolean>;
    signOut: () => void;
}

const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
    const [token, setToken] = useState<string | null>(
        localStorage.getItem("token")
    );

    const singIn = async (email: string, password: string): Promise<boolean> => {
        try {
            const response = await api.post("/login", { email, password });
            const { token } = response.data;
            setToken(token);
            localStorage.setItem("token", token);
            return true;
        } catch (error) {
            console.error("Erro ao fazer login:", error);
            return false;
        }
    };

    const signOut = () => {
        localStorage.removeItem("token");
        setToken(null);
    };

    useEffect(() => {
        if(token) {
            api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
        } else {
            delete api.defaults.headers.common["Authorization"];
        }
    }, [token]);

    return (
        <AuthContext.Provider value={{ isAuthenticated: !!token, token, signIn: singIn, signOut }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);

