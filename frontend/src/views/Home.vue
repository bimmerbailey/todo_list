<template>
  <div class="home">
    <Tasks></Tasks>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Tasks from '@/components/Tasks.vue'

@Component({
  components: {
    Tasks
  },
})
export default class Home extends Vue {
  // public tasks!: Array<{ description: string, id: number }>;
  //
  // // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  // mounted() {
  //   this.getTasks()
  // }
  //
  // private async getTasks() {
  //   // console.log(window.location.origin + ':8000/api_v1/todos/')
  //   fetch(window.location.origin + ':8000/api_v1/todos/').then(response => {
  //     // console.log(response);
  //     return response.json();
  //   }).then(data => {
  //     this.tasks = data
  //     // Work with JSON data here
  //     console.log(this.tasks);
  //   }).catch(err => {
  //     console.log("Error Reading data " + err);
  //   });
  //
  // }
}
</script>
