<template>
  <div>
    <b-form-select v-model="selected" :options="options" size="sm" class="mt-3"></b-form-select>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        selected: null,
        options: [
          { value: null, text: 'Off' },
          { value: 0.02, text: '2%' },
          { value: 0.03, text: '3%' },
          { value: 0.04, text: '4%' },
          { value: 0.05, text: '5%' },
          { value: 0.06, text: '6%' },
          { value: 0.07, text: '7%' },
          { value: 0.08, text: '8%' },
          { value: 0.09, text: '9%' },
          { value: 0.1, text: '10%' },

]
      }
    }
  }
</script>

<style>

.mt-3
{
  width: auto !important;
  height: 15%;
  border-bottom: 1px solid black;

}

</style>