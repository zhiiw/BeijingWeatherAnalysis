<template>
  <q-page class="flex flex-center bg-image" style="flex-direction: column">
    <q-select v-model="model" class="absolute-top-right" :options="options" label="City"></q-select>
    <vue3-chart-js
      :id="doughnutChart.id"
      ref="chartRef"
      :type="doughnutChart.type"
      :data="doughnutChart.data"
      :options="doughnutChart.options"
    ></vue3-chart-js>

    <button @click="updateChart">Update Chart</button>
  </q-page>

</template>

<script>
import { ref } from 'vue'
import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'
import axios from "axios";

export default {
  name: 'App',
  components: {
    Vue3ChartJs,
  },
  setup () {
    const chartRef = ref(null)

    const doughnutChart = {
      id: 'line',
      type: 'line',
      data: {
        labels: ["2021/7/26", "2021/7/27", "2021/7/28", "2021/7/29", "2021/7/30", "2021/7/31", "2021/8/1"],
        datasets: [
          {
            label:"Temperatrue Max",
            backgroundColor: [
              '#41B883',
            ],
            borderColor:[
              '#41B883',
            ],
            data: [26, 25, 25, 24, 24, 22, 25]
          },
          {
            label:"Temperatrue average",
            backgroundColor: [
              '#00D8FF',
            ],
            borderColor:[
              '#00D8FF',
            ],
            data: [28, 29, 31, 32, 26, 26, 26]
          },
          {
            label:"Temperatrue Min",
            backgroundColor: [
              '#E46651',
            ],
            borderColor:[
              '#E46651',
            ],
            data: [31, 32, 36, 37, 31, 27, 31]
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
            text: 'Weather Analysis'
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
    const options=["Shanghai","Shenzhen","Guangzhou","Tianjing","Harbin","Nanjing","Hefei","Chongqing","Xian","Hangzhou","Beijing"]

    const updateChart = () => {
      axios.get('http://127.0.0.1:8001/api/get').then((response)=> {
        let res = response.data
        console.log(res)
        console.log(res.x)

        doughnutChart.data.labels=res.x
        doughnutChart.data.datasets=[
          {
            label:'Temperatrue Max',
            backgroundColor: [
              '#41B883',
            ],
            borderColor:[
              '#41B883',
            ],
            data: res.ymin
          },
          {
            label:'Temperatrue average',
            backgroundColor: [
              '#00D8FF',
            ],
            borderColor:[
              '#00D8FF',
            ],
            data: res.yavg
          },
          {
            label:'Temperatrue Min',
            backgroundColor: [
              '#E46651',
            ],
            borderColor:[
              '#E46651',
            ],
            data: res.ymax
          }
        ]
        console.log(doughnutChart.data.datasets)

      })

      chartRef.value.update(250)
    }
    return {
      doughnutChart,
      updateChart,
      chartRef,
      options,
      model: ref("Beijing"),

  }
  },
}
</script>
