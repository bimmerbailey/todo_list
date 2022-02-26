import {AuthState} from './types';

export const getters = {
    token: (state: AuthState) => state.token,
    authenticated: (state: AuthState) => state.isLoggedIn,
}
