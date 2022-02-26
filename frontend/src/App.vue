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
          <v-btn icon to="/login">
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </v-toolbar>

        <v-navigation-drawer
            v-model="drawer"
            app
            temporary
        >
          <v-list
              flat dense nav class="py-1"
          >
            <v-list-item-group color='primary' mandatory>
              <v-list-item
                  v-for="item in items"
                  :key="item.title"
                  dense
                  :to="item.route"
              >
                <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>

              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>
        <v-main>
          <router-view></router-view>
        </v-main>
      </v-card>
    </v-app>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";

@Component
export default class App extends Vue {
  drawer = false
  items: Array<{ route: string, icon: string, title: string }> = [
    {route: '/', icon: 'home', title: 'Home'},
    {route: '/stack', icon: 'laptop', title: 'Tech Stack'},
    {route: '/about', icon: 'mdi-information', title: 'About'},
  ]
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
