<template>
  <q-page class="flex flex-center bg-image" style="flex-direction: column">
    <vue3-chart-js
      :id="doughnutChart.id"
      :type="doughnutChart.type"
      :data="doughnutChart.data"
      :options="doughnutChart.options"
      @before-render="beforeRenderLogic"
    ></vue3-chart-js>
  </q-page>


</template>

<script>
import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'

export default {
  name: 'App',
  components: {
    Vue3ChartJs,
  },
  created() {
    let _this = this
    /*
    this.$axios.get('http://127.0.0.1:8000/api/maintainence_count').then(function (response) {
      let res = response.data
      console.log(res)
      _this.Temperature.rows1 = res.x1
      _this.Temperature.rows2 = res.x2
      _this.Temperature.rows3 = res.x3

    })*/

  },
  data () {
    return {
      data:{},
      Temperature: {
        columns: ['time', 'TMin','TMax',"TAvg"],
        rows1: [],
        rows2: [],
        rows3: [],
      },

    }
  },
  setup () {
    const doughnutChart = {
      id: 'line',
      type: 'line',
      data: {
        labels: ['VueJs', 'EmberJs', 'ReactJs', 'AngularJs'],
        datasets: [
          {
            labels:"TMax",
            backgroundColor: [
              '#41B883',
            ],
            borderColor:[
              '#41B883',

            ],
            data: [33, 22, 84, 40]
          },
          {
            labels:"TAvg",
            backgroundColor: [
              '#00D8FF',
            ],
            borderColor:[
              '#00D8FF',
            ],
            data: [40, 20, 80, 10]
          },
          {
            labels:"TMin",
            backgroundColor: [
              '#E46651',
            ],
            borderColor:[
              '#E46651',

            ],
            data: [22, 44, 22, 123]
          }
        ]
      },
      options: {
        responsive: true,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        stacked: false,
        plugins: {
          title: {
            display: true,
            text: 'Chart.js Line Chart - Multi Axis'
          }
        },
        scales: {
          y: {
            type: 'linear',
            display: true,
            position: 'left',
          },

        }
      }
    }

    const beforeRenderLogic = (event) => {
      //...
      //if(a === b) {
      //  event.preventDefault()
      //}
    }

    return {
      doughnutChart,
      beforeRenderLogic
    }
  },
}
</script>
<style>
.bg-image {
  background-color: white
}
</style>
