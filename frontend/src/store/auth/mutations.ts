import { MutationTree } from "vuex";
import { AuthState } from "@/store/auth/types";

export const mutations: MutationTree<AuthState> = {
    setToken(state, payload) {
        state.token = payload;
    },
    setLoginError(state, payload) {
        state.logInError = payload
    },
    setIsLoggedIn(state, payload) {
        state.isLoggedIn = payload
    }
}
