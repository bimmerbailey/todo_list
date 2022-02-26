<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-12">
          <v-toolbar dark color="green">
            <v-toolbar-title>Login form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                  prepend-icon="person"
                  name="login"
                  label="Login"
                  type="text"
                  v-model="email"
              ></v-text-field>
              <v-text-field
                  id="password"
                  prepend-icon="lock"
                  name="password"
                  label="Password"
                  type="password"
                  v-model="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green" @click="login">Login</v-btn>
          </v-card-actions>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="red" @click="logout">Logout</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
// https://jasonwatmore.com/post/2018/09/21/vuejs-basic-http-authentication-tutorial-example
import {Component, Vue} from "vue-property-decorator";


@Component
export default class Login extends Vue {
  public email: string;
  public password: string;

  public constructor() {
    super();
    this.email = '';
    this.password = '';
  }

  public async login() {
    await this.$store.dispatch('auth/login', {username: this.email, password: this.password});
    if (this.$store.getters['auth/authenticated']) {
      await this.$router.push({name: 'Home'})
    } else {
      if (this.$router.currentRoute.path !== '/login') {
        await this.$router.push('/login');
      }
    }

  }

  public async logout() {
    await this.$store.dispatch('auth/logout')
  }
}
</script>

<style></style>
