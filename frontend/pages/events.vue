<template>

  <div id="app">
    <treeselect   v-model="label" 

                  :multiple="true"
                  :options="options" 
                  :openOnClick="true"
                  :label= "label"
                  
                  />
      <div>
      <button type="button" class="btn btn-dark">delete</button>
      <button type="button" class="btn btn-dark">clear</button>
      <button type="button" class="btn btn-dark">add</button>
    </div>
  </div>
    

</template>

<script>
  // import the component
  import Treeselect from '@riophae/vue-treeselect'
  // import the styles
  import '@riophae/vue-treeselect/dist/vue-treeselect.css'

  export default {
      components: { Treeselect },
  name: 'HelloWorld',
  data () {
    return {
      multiple: true,
      clearable: true,
      searchable: true,
      openOnClick: true,
      clearOnSelect: true,
      value: {},
      options:[],
      label: [],
    }
  },
   async asyncData ({ app }) {
    try {
      const response = await app.$axios.get('/api/events/')

      return {
        label: response.data.results,
        options: response.data.results,

        error: false
      }
    } catch (e) { 
      console.log('error', e)
      return {
        value: [],
        error: true
      }
    }
  }, 

 }


</script>
