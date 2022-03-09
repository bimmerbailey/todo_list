<template>
  <div>
    <v-dialog
        v-model="addDialog"
        width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            color="red"
            v-bind="attrs"
            v-on="on"
        >
          <v-icon v-if="icon">mdi-plus</v-icon>
          <span v-else>Update</span>
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 green">
          {{ title }}
        </v-card-title>

        <v-card-text>
          <v-text-field
              hide-details="auto"
              v-model="description"
          ></v-text-field>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              v-if="createTodo"
              @click="createTask(description)"
              color="green"
          >
            Add
          </v-btn>
          <v-btn
              v-else
              @click="updateTask(description, taskId)"
              color="red"
          >
            Update
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import {Vue, Component, Prop} from "vue-property-decorator";

@Component
export default class PopupDialog extends Vue {

  description!: string;
  addDialog!: boolean;

  public constructor() {
    super();
    this.description = '';
    this.addDialog = false;
  }

  // @PropSync('addDialog', { type: Boolean }) syncedDialog!: boolean
  @Prop({default: false}) icon!: boolean
  @Prop() title!: string
  @Prop({default: true}) createTodo!: boolean
  @Prop({default: null}) taskId!: number

  public async createTask(description: string): Promise<void> {
    await this.$store.dispatch('tasks/createTask', {description: description})
    await this.$store.dispatch('tasks/getTasks')
    this.addDialog = false;
    // this.$emit('updatedAddDialog', false);
  }

  public async updateTask(description: string, taskID: number): Promise<void> {
    await this.$store.dispatch('tasks/updateTask', {taskId: taskID, description: description})
    await this.$store.dispatch('tasks/getTasks')
    this.addDialog = false;
    // this.$emit('updatedAddDialog', false);
  }

}
</script>

<style scoped>

</style>
