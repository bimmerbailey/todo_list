import {ActionTree} from "vuex";
import {TaskState} from './types';
import {RootState} from "@/store/types";
import {api} from "@/api";

export const actions: ActionTree<TaskState, RootState> = {
    async getTasks({commit}) {
        await api.getAllTasks()
            .then(response => {
                return response.json()
            })
            .then((r) => {
                commit('tasksLoaded', r)
            })
            .catch(err => {
                console.log("Error Reading data " + err);
            });
    },

    async deleteTask({commit}, payload: { taskId: number }) {
        await api.deleteTask(this.getters['auth/token'], payload.taskId)
            .catch(err => {
                console.log("Error Reading data " + err);
            });
    },
    async updateTask({commit}, payload: {taskId: number, description: string}) {
        await api.updateTask(this.getters['auth/token'], payload.taskId, payload.description)
            .then(response => {
                return response.json()
            })
            .catch((err) => {
                console.log(err)
            })

    },
    async createTask({commit}, payload: {description: string}) {
        await api.createTask(this.getters['auth/token'], payload.description)
            .then(response => {
                if (response.status == 201) {
                    return response.json()
                } else {
                    throw new Error('Error saving data')
                }
            })
            .catch((err) => {
                console.log(err)
            })

    }
}
