import {Module} from "vuex";
import {actions} from "@/store/auth/actions";
import {mutations} from "@/store/auth/mutations";
import {getters} from "@/store/auth/getters";
import {AuthState} from './types'
import {RootState} from "@/store/types";

export const state: AuthState = {
    token: '',
    isLoggedIn: null,
    logInError: false
}

export const auth: Module<AuthState, RootState> = {
    namespaced: true,
    state,
    actions,
    getters,
    mutations
};
