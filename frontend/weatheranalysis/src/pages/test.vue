<template>
  <q-page class="q-pa-sm bg-image" style="flex-direction: column">
    <q-card class="q-mt-sm">
      <q-card-section class="text-h6 q-pb-none">
        <q-item>
          <q-item-section avatar class="">
            <q-icon color="blue" name="fas fa-chart-line" size="44px" />
          </q-item-section>

          <q-item-section>
            <div class="text-h6">Weather Charts</div>
          </q-item-section>
        </q-item>
        <div class="row">
        <div class="col-lg-3 col-md-3 col-xs-3 col-sm-3">
          <q-item>
            <q-item-section top avatar>
              <q-avatar color="blue" text-color="white" icon="thermostat" />
            </q-item-section>
            <q-item-section>
              <q-item-label class="text-h6 text-blue text-bold">{{ max }}</q-item-label>
              <q-item-label caption>Fashions</q-item-label>
            </q-item-section>
          </q-item>
        </div>



        <div class="col-lg-3 col-md-3 col-xs-3 col-sm-3">
          <q-item>
            <q-item-section top avatar>
              <q-avatar color="green-6" text-color="white" icon="bluetooth" />
            </q-item-section>
            <q-item-section>
              <q-item-label class="text-h6 text-green-6 text-bold">{{avg}}</q-item-label>
              <q-item-label caption>Toys</q-item-label>
            </q-item-section>
          </q-item>
        </div>
        <div class="col-lg-3 col-md-3 col-xs-3 col-sm-3">
          <q-item>
            <q-item-section top avatar>
              <q-avatar color="orange-8" text-color="white" icon="ac_unit" />
            </q-item-section>
            <q-item-section>
              <q-item-label class="text-h6 text-orange-8 text-bold">{{ min }}</q-item-label>
              <q-item-label caption>Vouchers</q-item-label>
            </q-item-section>
          </q-item>
        </div>

        </div>
      </q-card-section>
      <q-select v-model="model" class="absolute-top-right" :options="options" label="City"></q-select>
      <vue3-chart-js
        :id="doughnutChart.id"
        ref="chartRef"
        :type="doughnutChart.type"
        :data="doughnutChart.data"
        :options="doughnutChart.options"
      ></vue3-chart-js>
    </q-card>

    <button @click="updateChart();updateVal();">Update Chart</button>
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
  data(){
    return{
      avg:28.2,
      max :32.1,
      min:24.1,
    }
  },
  methods:{
    updateVal(){
        const average = arr => arr.reduce( ( p, c ) => p + c, 0 ) / arr.length;
        this.avg=this.doughnutChart.avg.toFixed(1)
        this.max=this.doughnutChart.max.toFixed(1)
        this.min=this.doughnutChart.min.toFixed(1)

    }
  },
  setup () {
    const chartRef = ref(null)

    const model="Beijing"
    const doughnutChart = {
      id: 'line',
      type: 'line',
      avg:24.4,
      max:28.2,
      min:32.1,
      data: {
        labels: ["2021/26", "2021/7/27", "2021/7/28", "2021/7/29", "2021/7/30", "2021/7/31", "2021/8/1"],
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

      axios.post('http://192.168.43.78:8001/api/forecast',{
        city:"Shanghai"
      }).then((response)=> {
        let res = response.data
        console.log(res)
        console.log(res.x)
        const average = arr => arr.reduce( ( p, c ) => p + c, 0 ) / arr.length;
        doughnutChart.avg=average(res.yavg)
        doughnutChart.max=average(res.ymax)
        doughnutChart.min=average(res.ymin)
        console.log("the min is "+doughnutChart.min)

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
