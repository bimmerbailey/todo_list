import {ActionTree} from "vuex";
import {AuthState} from './types';
import {RootState} from "@/store/types";
import {api} from '@/api';
import { saveLocalToken } from '@/utils';


export const actions: ActionTree<AuthState, RootState> = {
    async login({commit}, payload: { username: string, password: string }) {
        await api.logInGetToken(payload.username, payload.password)
            .then((response) => {
                if (response.status == 200) {
                    return response.json()
                } else {
                    throw new Error('Login Failed')
                }
            })
            .then((resp) => {
                commit('setIsLoggedIn', true)
                commit('setLoginError', false)
                saveLocalToken(resp.access_token)
                commit('setToken', resp.access_token)
            })
            .catch(() => {
                commit('setIsLoggedIn', false)
                commit('setLoginError', true)
            })
    },
    async logout({commit}) {
        commit('setIsLoggedIn', false)
        commit('setLoginError', true)
        commit('setToken', '')
    }
}
