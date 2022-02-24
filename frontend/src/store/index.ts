import Vue from 'vue'
import Vuex from 'vuex'

import {tasks} from "@/store/tasks";
import {auth} from "@/store/auth";
import {RootState} from "@/store/types";

Vue.use(Vuex);

export default new Vuex.Store<RootState>({
    state: {
        version: '1.0.0',
    },
    modules: {
        tasks,
        auth,
    },
    mutations: {},
    actions: {},
});

