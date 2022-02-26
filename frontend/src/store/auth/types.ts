export interface AuthState {
    token: string;
    isLoggedIn: boolean | null;
    logInError: boolean;
}
