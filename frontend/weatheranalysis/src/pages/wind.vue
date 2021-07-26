<template>
  <q-page class="flex flex-center bg-image" style="flex-direction: column">
    <q-select v-model="model" :options="options" label="Standard" model-value="Beijing"></q-select>

    <vue3-chart-js
      :id="doughnutChart.id"
      :type="doughnutChart.type"
      :data="doughnutChart.data"
      :options="doughnutChart.options"
    ></vue3-chart-js>
    <q-btn label="Login" @click="onsubmit" color="primary"/>

  </q-page>


</template>

<script>
import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'
export default {
  name: 'wind',
  components: {
    Vue3ChartJs,
  },

  created () {
    let _this=this

    this.$axios.get('http://127.0.0.1:8001/api/get').then((response)=> {
      let res = response.data
      console.log(res)
      console.log(res.x)

      _this.columns = res.x

      _this.rows1 = res.ymin
      _this.rows2 = res.yavg
      _this.rows3 = res.ymax

      _this.doughnutChart.data.labels=this.columns
      _this.doughnutChart.data.datasets=[
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
      console.log(_this.doughnutChart.data.datasets)

    })
    console.log("ee")

  },
  data () {
    return {
      chartRef : ref(null),

      doughnutChart : {
        id: 'line',
        type: 'line',
        data: {
          labels: ["2021/7/26", "2021/7/27", "2021/7/28", "2021/7/29", "2021/7/30", "2021/7/31", "2021/8/1"],
          datasets: [
            {
              label:'Temperatrue Max',
              backgroundColor: [
                '#41B883',
              ],
              borderColor:[
                '#41B883',
              ],
              data: [26, 25, 25, 24, 24, 22, 25]
            },
            {
              label:'Temperatrue average',
              backgroundColor: [
                '#00D8FF',
              ],
              borderColor:[
                '#00D8FF',
              ],
              data: [28, 29, 31, 32, 26, 26, 26]
            },
            {
              label:'Temperatrue Min',
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
      },
      columns: ['time', 'TMin','TMax',"TAvg"],
      rows1: [1,3],
      rows2: [1,4],
      rows3: [1,3],

    }
  },
  methods:{
    onsubmit() {
      console.log(this.doughnutChart.data)
      this.columns=["eee","weafd","wesd","wesd"]
    },
    update(){
      const updateChart = () => {
        this.doughnutChart.options.plugins.title = {
          text: 'Updated Chart',
          display: true
        }
        this.doughnutChart.data.labels = ['Cats', 'Dogs', 'Hamsters', 'Dragons']
        this.doughnutChart.data.datasets = [
          {
            backgroundColor: [
              '#333333',
              '#E46651',
              '#00D8FF',
              '#DD1B16'
            ],
            data: [100, 20, 800, 20]
          }
        ]

        chartRef.value.update(250)
      }
    }

  }
}
</script>
<style>
.bg-image {
  background-color: white
}
</style>
