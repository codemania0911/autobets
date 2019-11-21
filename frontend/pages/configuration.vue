


<template>
<div class="table">
    <tr v-for="(entry, id) in combined" :key=id>
        <td>{{entry.type == 'event' ? event.start_time : ''}} </td>
        <td>{{ entry.type == 'event' ?  event.event_name : ''}} </td>
        <td>{{ entry.type = 'market' ? market.name : ''}}</td>
        <td>{{ entry.type == 'runner' ? runner.name : ''}}</td>
    </tr>
 </div>


</template>

<script>
import SelectStake from '~/components/SelectStake.vue';

//import axios from "axios";
//import SelectStake from '~/components/SelectStake.vue';
export default {

  components:{
    SelectStake
  },

 async asyncData ({ app }) {
   
    let response = await app.$axios.get('/api/events/')
    const events = response.data.results

    response = await app.$axios.get('/api/markets')
    const markets = response.data.results

    response = await app.$axios.get('/api/runners')
    const runners = response.data.results

    return {
      events,
      markets,
      runners
    }
 }
}

</script>


<style>

th, td {
font-family: ‘Lato’, sans-serif;
font-size: 12px;
font-weight: 400;
padding: 10px;
text-align: left;
width: 0%;
border-bottom: 1px solid black;

}



</style>
