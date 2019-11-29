<template>
  <div class="course-list-row">
    <th scope="col"> Start date </th>
    <th scope="col" style= "width:10%"> Event name</th>
    <th scope="col">Status</th>
    <th scope="col">Market</th>
    <th scope="col">inplay</th>
    <th scope="col">Volume</th>
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

        <td>{{ event.event.start_time }} </td>
        <td>{{ event.event.event_name }}</td>
        <td>{{ event.event.status }}</td>
        <td>{{ event.market.market_name }}</td>
        <td> {{ event.market.is_ip }}</td>
        <td> {{ event.market.volume }} </td>
        <td> {{ event.name }} </td>
        <td> {{ event.back_odds }} </td>
        <td> {{ event.lay_odds }} </td>


        <td/>




    </tr>

  </div>
</template>
<script>
export default{
 async asyncData ({ app }) {

    try {
      const events = await app.$axios.get('/api/combined/')

      return {
        events: events.data.results,

        error: false
      }
    } catch (e) {
      console.log('error', e)
      return {
        events: {},
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