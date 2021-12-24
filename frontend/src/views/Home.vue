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

}
</script>
