<template>
  <v-container fluid>
    <div v-if="!tasks.error">
      <v-card
        v-for="task in tasks.tasks"
        :key="task.id"
      >
        <v-card-text>
          {{ task.description }}
        </v-card-text>
        <v-container fluid>

          <v-row>
            <v-spacer></v-spacer>
            <v-card-actions>
              <v-btn color="green">Completed</v-btn>
            </v-card-actions>
            <v-card-actions>
              <v-btn color="red">Update</v-btn>
            </v-card-actions>
          </v-row>
        </v-container>

      </v-card>
    </div>
  </v-container>
</template>

<script lang="ts">
import {Vue, Component} from "vue-property-decorator";
import {mapState} from "vuex";
//https://blog.logrocket.com/vue-typescript-tutorial-examples/

@Component({
  computed: {
    ...mapState(['tasks']),
  }
})
export default class Task extends Vue {

  // eslint-disable-next-line
  mounted() {
    this.$store.dispatch('tasks/getTasks')
  }
}
</script>

<style scoped>

</style>