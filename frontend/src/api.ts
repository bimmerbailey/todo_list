function authHeaders(token: string) {
    return {
        Authorization: `Bearer ${token}`
    };
}

const baseURL = 'http://localhost:8000/api_v1';

export const api = {
    async logInGetToken(username: string, password: string) {
        return await fetch(baseURL + '/login', {
            method: 'post',
            body: new URLSearchParams({username: username, password: password})
        })
    },
    async deleteTask(token: string, taskId: number) {
        return await fetch(baseURL + '/todos/' + taskId, {
            method: "delete",
            headers: authHeaders(token)
        })
    },
    async getAllTasks() {
        return await fetch(baseURL + '/todos/')
    }
};
