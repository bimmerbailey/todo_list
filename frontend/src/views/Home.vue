<template>
  <div class="home">
    <Login></Login>
    <Tasks></Tasks>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import Tasks from '@/components/Tasks.vue';
import Login from '@/components/Login.vue'

@Component({
  components: {
    Tasks,
    Login
  },
})
export default class Home extends Vue {
}
</script>
