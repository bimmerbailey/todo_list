import Vue from 'vue'
import Vuex from 'vuex'
import tasks from './tasks'

Vue.use(Vuex)

export default new Vuex.Store({
  // state: {
  // },
  // mutations: {
  // },
  // actions: {
  // },
  modules: {
    tasks
  }
})
