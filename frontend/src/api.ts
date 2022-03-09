function authHeaders(token: string) {
    return {
        'Content-Type' : 'application/json',
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
    },
    async updateTask(token: string, taskId: number, description: string) {
        return await fetch(baseURL + '/todos/' + taskId, {
            method: "put",
            headers: authHeaders(token),
            body: JSON.stringify({ description: description })
        })
    },
    async createTask(token: string, description: string) {
        return await fetch(baseURL + '/todos/', {
            method: "post",
            headers: authHeaders(token),
            body: JSON.stringify({ description: description })
        })
    },
};
