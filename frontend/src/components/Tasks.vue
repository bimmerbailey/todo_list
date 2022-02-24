<template>
  <v-container fluid>
    <v-card
        v-for="task in tasks"
        :key="task.id"
    >
      <v-card-text>
        {{ task.description }}
      </v-card-text>
      <v-container fluid>

        <v-row>
          <v-spacer></v-spacer>
          <v-card-actions>
            <v-btn color="green" @click="deleteTask(task.id)">Completed/Delete</v-btn>
          </v-card-actions>
          <v-card-actions>
            <v-btn color="red">Update</v-btn>
          </v-card-actions>
        </v-row>
      </v-container>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import {Vue, Component} from "vue-property-decorator";
import {mapGetters} from "vuex";
//https://blog.logrocket.com/vue-typescript-tutorial-examples/

@Component({
  computed: {
    ...mapGetters({
      tasks: 'tasks/tasks'
    }),
  }
})
export default class Task extends Vue {

  public constructor() {
    super();
  }

  public async deleteTask(taskID: number): Promise<void> {
    await this.$store.dispatch('tasks/deleteTask', {taskId: taskID})
    await this.$store.dispatch('tasks/getTasks')
  }

  mounted(): void {
    this.$store.dispatch('tasks/getTasks')
  }
}

</script>

<style scoped>

</style>
