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
          { value: 'a', text: '2%' },
          { value: 'b', text: '3%' },
          { value: 'c', text: '4%' },
          { value: 'd', text: '5%' },
          { value: 'e', text: '6%' },
          { value: 'f', text: '7%' },
          { value: 'g', text: '8%' },
          { value: 'h', text: '9%' },
          { value: 'i', text: '10%' },

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