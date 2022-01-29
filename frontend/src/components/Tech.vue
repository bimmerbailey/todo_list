<template>
  <v-container fluid>
    <div v-for="item in stack" v-bind:key="item.name">
      <v-row>
        <v-col>
          <v-card elevation="10">
            <v-card-title>
              {{ item.name }}
            </v-card-title>
            <v-card-subtitle>
              {{ item.description }}
            </v-card-subtitle>
            <v-card-actions>
              <v-btn
                  :href="item.link"
              >
                Go To Website
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>

      </v-row>

    </div>
  </v-container>

</template>

<script lang="ts">
import {Vue, Component} from "vue-property-decorator";

@Component
export default class Tech extends Vue {
  stack: Array<{ name: string, description: string, link: string }> = [
    {name: 'FastAPI', description: 'Used in backend', link: 'https://fastapi.tiangolo.com/'},
    {name: 'Postgres', description: 'SQL Database', link: 'https://www.postgresql.org/'},
    {name: 'Alembic', description: 'Database Migrations', link: 'https://alembic.sqlalchemy.org/en/latest/'},
    {name: 'Vue.js', description: 'Frontend. Used with Typescript', link: 'https://vuejs.org/'},
    {name: 'Docker', description: 'Containerization', link: 'https://www.docker.com/'},
    {name: 'Github', description: 'Version Control', link: 'https://github.com/'},
  ]

}
</script>

<style scoped>

</style>
