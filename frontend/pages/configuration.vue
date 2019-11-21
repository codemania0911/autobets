


<template>
  <div class="course-list-row">
    <th scope="col"> Start date </th>
    <th scope="col"> Event name</th>
    <th scope="col">Market</th>
    <th scope="col">Status</th>
    <th scope="col">Position</th>
    <th scope="col">Runner</th>
    <th scope="col">Back Odds</th>
    <th scope="col">Lay Odds</th>
    <th scope="col">B1 Trig</th>
    <th scope="col">B2 Trig</th>
    <th scope="col">L1 Trig</th>
    <th scope="col">L2 Trig</th>
    <th scope="col">Auto Stake</th>
    <th scope="col">Back Stake</th>
    <th scope="col">Lay Stake</th>


    <tr v-for="event in events" :key="event.id" >

        <td>{{ event.start_time }} </td>
        <td>{{ event.event_name }}</td>
        <td>                       </td>
        <td>        Is inplay      </td>
        <td>         Position Data </td>
        <td>         Back Odds     </td>

      <SelectStake/>

        <td/>




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

    try {
      const events = await app.$axios.get('/api/events/')
      const markets = await app.$axios.get('/api/markets/')

      return {
        events: events.data.results,
        markets: markets.data.results,

        error: false
      }
    } catch (e) {
      console.log('error', e)
      return {
        events: [],
        markets:[],
        error: true
      }
    }
  },
};




</script>


<style>

th, td {
font-family: ‘Lato’, sans-serif;
font-size: 12px;
font-weight: 400;
padding: 10px;
text-align: left;
width: 0%;
}


</style>
