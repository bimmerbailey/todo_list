<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <PopupDialog
            class="float-right"
            :icon="true"
            :create-todo="true"
            :title="'Add Todo'"
        ></PopupDialog>
      </v-col>
    </v-row>
    <div v-if="tasks">
      <v-row
          v-for="task in tasks"
          :key="task['id']"
      >
        <v-col>
          <v-card>
            <v-card-text>
              {{ task['description'] }}
            </v-card-text>
            <v-container fluid>

              <v-row>
                <v-spacer></v-spacer>
                <v-card-actions>
                  <v-btn color="green" @click="deleteTask(task['id'])">Completed/Delete</v-btn>
                </v-card-actions>
                <v-card-actions>
                  <PopupDialog
                      :create-todo="false"
                      :title="'Update Todo ' + task['id']"
                      :task-id="task['id']"
                  >
                  </PopupDialog>
                </v-card-actions>
              </v-row>
            </v-container>
          </v-card>
        </v-col>

      </v-row>
    </div>
    <v-row v-else><v-card>Nothing To Do. Please Add Something</v-card></v-row>
  </v-container>
</template>

<script lang="ts">
import {Vue, Component} from "vue-property-decorator";
import {mapGetters} from "vuex";
import PopupDialog from "@/components/PopupDialog.vue";

@Component({
  components: {
    PopupDialog
  },
  computed: {
    ...mapGetters({
      tasks: 'tasks/tasks'
    }),
  }
})
export default class Task extends Vue {

  toAdd!: string

  public constructor() {
    super();
    this.toAdd = ''
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
