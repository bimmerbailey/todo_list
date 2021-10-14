<template>
  <div>
    <!--    TODO: for-loop will go here -->
    <md-card class="md-rounded">
      <md-card-header>
        <div class="md-title">{{ task }}</div>
      </md-card-header>

      <md-card-content>
        Created by: {{ creator }}
      </md-card-content>

      <md-card-actions>
        <md-button>Add Importance</md-button>
        <md-button>Task Completed</md-button>
      </md-card-actions>
    </md-card>
  </div>
</template>

<script lang="ts">
import {Component, Prop, Vue} from 'vue-property-decorator';

@Component
export default class ImportantToDo extends Vue {

  @Prop() private msg!: string;
  @Prop({default: 'Default Creator'}) private creator!: string;
  @Prop({default: 'Default Task'}) private task!: string;

}
</script>

<style scoped lang="scss">
.md-rounded {
  border-radius: 10px;
  padding: 5px;
  margin: 2%;
}

</style>
