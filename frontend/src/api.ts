import {IUserProfile, IUserProfileUpdate, IUserProfileCreate} from './interfaces';
import {AuthState} from "@/store/auth/types";

function authHeaders(token: string) {
    return {
        Authorization: `Bearer ${token}`
    };
}

const baseURL = 'http://localhost';

export const api = {
    async logInGetToken(username: string, password: string) {
        return await fetch(baseURL + ':8000/login', {
            method: 'post',
            body: new URLSearchParams({username: username, password: password})
        })
    },
    async deleteTask(token: string, taskId: number) {
        return await fetch(baseURL + ':8000/api_v1/todos/' + taskId, {
            method: "delete",
            headers: authHeaders(token)
        })
    },
    async getAllTasks() {
        return await fetch(baseURL + ':8000/api_v1/todos/')
    }
};
