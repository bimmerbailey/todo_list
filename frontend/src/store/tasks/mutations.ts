import { MutationTree } from "vuex";
import { TaskState, Task } from "@/store/tasks/types";

export const mutations: MutationTree<TaskState> = {
    tasksLoaded(state, payload: Task) {
        state.error = false;
        state.tasks = payload
    },
    profileError(state) {
        state.error = true;
        state.tasks = undefined;
    }
}