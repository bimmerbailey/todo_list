<template>
  <div>
    <v-card>
      <v-card-title>
        Hi
      </v-card-title>
    </v-card>
  </div>
</template>

<script lang="ts">
import {Vue, Component, Prop} from "vue-property-decorator";

@Component
export default class Tech extends Vue {

  @Prop() techName!: string | undefined
  @Prop() link!: string | undefined
}
</script>

<style scoped>

</style>