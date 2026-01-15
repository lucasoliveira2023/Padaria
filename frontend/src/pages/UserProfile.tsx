import React, { useEffect, useState } from "react";
import axios from "axios";


interface UserProfileData {
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;
}

const UserProfile: React.FC = () => {
    const [user, setUser] =useState<UserProfileData | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await axios.get<UserProfileData>("/usuarios/profile");
                setUser(response.data);
            } catch  {
                setError("Error ao carregar perfil do usuário.");
            } finally {
                setLoading(false);
            }
        };

        fetchProfile();
    },  []);

    if (loading) return <p>Carregando...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div className="user-profile">
            <h1>Perfil do Usuário</h1>
            {user && (
                <div className="profile-card">
                    <p><strong>Username:</strong> {user.username}</p>
                    <p><strong>Email:</strong> {user.email}</p>
                    <p><strong>Nome:</strong> {user.first_name} { user.last_name}</p>
                </div>
            )}
        </div>
    );
};

export default UserProfile;