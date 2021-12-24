<template>
  <v-container fluid>
    <v-card v-if="task">
      <v-card-title>
        {{ title }}
      </v-card-title>
      <v-card-text>
        {{ task }}
      </v-card-text>
      <v-container fluid>

        <v-row>
          <v-spacer></v-spacer>
          <v-card-actions>
            <v-btn color="green">Completed</v-btn>
          </v-card-actions>
          <v-card-actions>
            <v-btn color="red">Delete</v-btn>
          </v-card-actions>
        </v-row>

      </v-container>

    </v-card>
    <v-card v-else>
      <v-card-title>
        Please Create a Task
      </v-card-title>
      <v-card-actions>
        <v-btn color="green">Create Task</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import {Vue, Component, Prop} from "vue-property-decorator";

@Component
export default class Task extends Vue {
  @Prop({default: 'This is a default task'}) task!: string
  @Prop({default: 'This is a default title'}) title!: string
}
</script>

<style scoped>

</style>