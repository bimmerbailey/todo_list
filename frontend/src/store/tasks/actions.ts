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
    }
}
