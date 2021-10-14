<template>
  <div>
    <ImportantToDo></ImportantToDo>
  </div>

</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import ImportantToDo from "@/components/TaskToDo.vue";

@Component(
    {
      components:
          {ImportantToDo}
    }
)
export default class BasicTaskViewer extends Vue {

}

</script>

<style scoped lang="scss">

</style>
