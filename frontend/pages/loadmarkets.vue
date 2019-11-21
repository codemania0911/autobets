<template>
  

  <table border>
      <thead>
        <th>Start date</th>   
        <th>Event name</th>
        <th>Market</th>
        <th>Runner</th>
      </thead>
      <tbody>
        <template v-for="event in events">
          <tr :key="'event' + event.id">
              <td>{{ event.start_time }}</td>
              <td>{{ event.event_name }}</td>          
          </tr>
          <template v-for="market in marketsFor[event.id]">
            <tr :key="'market' + market.id">
              <td></td>
              <td></td>
              <td>{{ market.market_name }} </td>
            </tr>
            <tr v-for="runner in runners[market.id]" :key="'runner' + runner.id">
              <td></td>
              <td></td>
              <td></td>
              <td>{{ runner.runner_name }}</td>
            </tr>
          </template>
        </template>
      </tbody>
    </table>


</template>
<script>

export default {

data(){
  return {
      events: [],
      runners: [],
      markets:[],
    }
},
  
  computed: {
   async marketsFor (app) {
      const events = await app.$axios.get('/api/events/')

      const markets = await app.$axios.get('/api/markets/')

      
      for (const market of this.markets) {
        const event = market.event
        markets[event] = markets[event] || []
        markets[event].push(market)
      }
      
      return markets
    },
    
   async runnersFor (app) {
      const runners = await app.$axios.get('/api/runners/')
      
      for (const runner of this.runners) {
        const market = runner.market
        runners[market] = runners[market] || []
        runners[market].push(runner)
      }
      
      return runners
    }
  }
}

</script>


<style>

</style>