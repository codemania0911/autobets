<template>
  <div class="line-chart">
    <LineChart :data="lineChartData" :options="{ maintainAspectRatio: false }" />
  </div>
</template>

<script>
import moment from 'moment'
import LineChart from '~/components/line-chart'
export default {
  components: {
    LineChart
  },
  async asyncData ({ app }) {
    const res = await app.$axios.get('api/reports/')
    return {
      lineChartData: {
        labels: res.data.results.map(stat=> moment(stat.start_time).format('GGGG[-W]WW')),
        datasets: [
          {
            label: 'Profit and Loss',
            backgroundColor: '#41b883',
            data: res.data.results.map(stat =>stat.profit_and_loss),
          }
        ]
      }
    }
  }
}
</script>

<style scoped>
.line-chart {
  position: fixed;
  left: 10%;
  top: 10%;
  width: 80%;
  height: 80%;
}
</style>