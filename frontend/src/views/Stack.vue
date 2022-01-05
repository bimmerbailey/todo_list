<template>
  <div>
    <Tech>

    </Tech>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from "vue-property-decorator";
import Tech from "@/components/Tech.vue";

@Component({
  components: {
    Tech
  }
})
export default class Stack extends Vue {

}
</script>

<style scoped>

</style>