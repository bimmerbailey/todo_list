import {ActionTree} from "vuex";
import {TaskState} from './types';
import {RootState} from "@/store/types";

export const actions: ActionTree<TaskState, RootState> = {
    async getTasks({commit}) {
        await fetch(window.location.origin + ':8000/api_v1/todos/')
            .then(response => {
                return response.json()
                // const payload: Promise<Task> = response.json()
                // console.log(payload)
                // return commit('tasksLoaded', payload)
            })
            .then((r) => {
                // console.log(r)
                commit('tasksLoaded', r)
            })
            .catch(err => {
                console.log("Error Reading data " + err);
            });

    }
}