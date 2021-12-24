<template>
  <div id="app">
    <v-app>
      <v-card>
        <v-toolbar
            color="green"
        >
          <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
          <v-toolbar-title>ToDo App</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </v-toolbar>

        <v-navigation-drawer
            v-model="drawer"
            app
        >
          <v-list>
            <v-list-item>
              <router-link to="/">Home</router-link>
            </v-list-item>
            <v-list-item>
              <router-link to="/about">About</router-link>
            </v-list-item>
            <v-list-item>
              <router-link to="/stack">Tech Stack</router-link>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
        <v-container>
          <router-view></router-view>
        </v-container>
      </v-card>
    </v-app>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";

@Component
export default class App extends Vue {
  data() {
    return {drawer: false}
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
