<template>
  <div>
    <treeselect
      :multiple="multiple"
      :clearable="clearable"
      :searchable="searchable"
      :open-on-click="openOnClick"
      :clear-on-select="clearOnSelect"
      :load-root-options="loadRootOptions"
      :options="options"
      :limit="5"
      :max-height="300"
      :normalizer="normalizer"
      v-model="value"
    />



    <div>
      <button type="button" class="btn btn-dark">update</button>
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
      value: [],
      options:[],
    }
  },
 

   loadRootOptions(callback) {
     axios.get('api/event/')
         .then(response => callback(null, [response.data]))
         .catch(response => {
           callback('error')
           console.log(response.data)
         });
   },
  
  }

</script>
