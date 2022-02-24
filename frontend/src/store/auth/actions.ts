import {ActionTree} from "vuex";
import {AuthState} from './types';
import {RootState} from "@/store/types";
import {api} from '@/api';
import { saveLocalToken } from '@/utils';


export const actions: ActionTree<AuthState, RootState> = {
    async login({commit}, payload: { username: string, password: string }) {
        await api.logInGetToken(payload.username, payload.password)
            .then((response) => {
                return response.json()
            })
            .then((resp) => {
                saveLocalToken(resp.access_token)
                commit('setToken', resp.access_token)
                commit('setIsLoggedIn', true)
                commit('setLoginError', false)
            })
            .catch(() => {
                commit('setIsLoggedIn', false)
                commit('setLoginError', true)
            })
    },

}
