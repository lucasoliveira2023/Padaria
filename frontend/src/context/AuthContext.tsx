import { createContext, useContext, useEffect, useState } from "react";
import api from "../services/api";


interface AuthContextType {
    isAuthenticated: boolean;
    token: string | null;
    signIn: (username: string, password: string) => Promise<boolean>;
    signOut: () => void;
}

const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
    const [token, setToken] = useState<string | null>(
        localStorage.getItem("token")
    );

    const signIn = async (username: string, password: string): Promise<boolean> => {
      try {
        const response = await api.post("login/", {
            username,
            password,
        });

        const { access } = response.data;

        setToken( access );
        localStorage.setItem("token", access);
        return true;
      } catch (error) {
        console.error("Error ao fazer login:", error);
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
        <AuthContext.Provider value={{ isAuthenticated: !!token, token, signIn, signOut }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);

