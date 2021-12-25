import {Module} from "vuex";
import {actions} from "@/store/tasks/actions";
import {mutations} from "@/store/tasks/mutations";
import {TaskState} from './types'
import {RootState} from "@/store/types";

export const state: TaskState = {
    tasks: undefined,
    error: false
}

export const tasks: Module<TaskState, RootState> = {
    namespaced: true,
    state,
    actions,
    mutations
};