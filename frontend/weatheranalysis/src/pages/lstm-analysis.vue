<template>
  <q-page class="q-pa-sm bg-image" style="flex-direction: column">
    <q-card class="q-mt-sm">
      <q-card-section class="text-h6 q-pb-none">
        <q-item>
          <q-item-section avatar class="">
            <q-icon color="blue" name="fas fa-chart-line" size="44px" />
          </q-item-section>

          <q-item-section>
            <div class="text-h6">Weather Charts(LSTM)</div>
          </q-item-section>
        </q-item>
      </q-card-section>
      <div class="absolute-top-right">

        <q-select v-model="model" :options="options" label="City"></q-select>
        <q-btn label="Update" @click="updateChart(this.model)" color="primary"/>

      </div>

      <vue3-chart-js
        :id="doughnutChart.id"
        ref="chartRef"
        :type="doughnutChart.type"
        :data="doughnutChart.data"
        :options="doughnutChart.options"
      ></vue3-chart-js>
    </q-card>
    <br><br>
    <div id='container'></div>
    <div class="row">

      <q-input
        filled
        v-model="username"
        label="danmu"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type your danmu']"
      />

    </div>
    <q-btn label="Send" @click="onSend" color="primary"/>


  </q-page>

</template>

<script>
import { ref } from 'vue'
import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'
import axios from "axios";
import easyDanmaku from 'easy-danmaku-js';

let Danmaku;

export default {
  name: 'App',

  components: {
    Vue3ChartJs,
  },
  data(){
    return{
      Danmaku,
      username:'',
      danmus:[],
      avg:28.2,
      max :32.1,
      min:24.1,
    }
  },
  mounted() {
    Danmaku = new easyDanmaku({
      el:'#container',                        //弹幕挂载节点
      line:10,
      colourful:true,//弹幕行数
      wrapperStyle:'danmaku-wrapper',         //默认弹幕样式
      speed:5,                                //弹幕播放速度
      runtime:3,                              //播放一次的时常
      loop:true,                              //开启循环播放
      hover:true,                             //鼠标移入悬停
      onComplete:()=> {                       //播放结束
        console.log('end');
      },                                      //hover时 参数为该悬停元素
      onHover:(dom) => {
        console.log(dom);
      }
    })
    this.$axios.get(`http://192.168.43.78:8001/api/load_comments`).then(response=>{
      let res = response.data
      console.log(res)
      this.danmus=res.comments_array
      Danmaku.batchSend(this.danmus)

    })
    const data = ['danmaku1','danmaku2','danmaku3','danmaku4','danmaku5','danmaku6']
  },
  methods:{
    updateVal(){
      const average = arr => arr.reduce( ( p, c ) => p + c, 0 ) / arr.length;
      this.avg=this.doughnutChart.avg.toFixed(1)
      this.max=this.doughnutChart.max.toFixed(1)
      this.min=this.doughnutChart.min.toFixed(1)

    },

    onSend(){
      Danmaku.send(
        "<h5>"+"<u>"+this.username+"</u>"+"</h5>",'danmaku-wrapper',(e)=>{
        }
      )
      this.$axios.post(`http://192.168.43.78:8001/api/send_comment`,
        {
          user_id:sessionStorage.getItem('user_id'),
          text:this.username
        }).then(response=>{
      })


    }
  },
  setup () {
    const chartRef = ref(null)

    const model="Beijing"
    const doughnutChart = {
      id: 'bar',
      type: 'bar',
      avg:24.4,
      max:28.2,
      min:32.1,
      data: {
        labels: ["2021/26", "2021/7/27", "2021/7/28", "2021/7/29", "2021/7/30", "2021/7/31", "2021/8/1"],
        datasets: [
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
            text: 'Weather Analysis(LSTM)'
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
    const options=["Shanghai","Guangzhou","Tianjin","Harbin","Nanjing","Hefei","Chongqing","Xian","Hangzhou","Beijing"]
    const updateChart = (model) => {

      axios.post('http://192.168.43.78:8001/api/lstm',{
        city:model.toUpperCase()
      }).then((response)=> {
        console.log(model)
        let res = response.data
        console.log(res)
        console.log(res.y)

        /*
        const average = arr => arr.reduce( ( p, c ) => p + c, 0 ) / arr.length;
        doughnutChart.avg=average(res.yavg)
        doughnutChart.max=average(res.ymax)
        doughnutChart.min=average(res.ymin)*/

        doughnutChart.data.labels=res.x
        doughnutChart.data.datasets=[
          {
            label:'Temperatrue average',
            backgroundColor: [
              '#00D8FF',
            ],
            borderColor:[
              '#00D8FF',
            ],
            data: res.y
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
<style>
#container{
  width:90vh;
  height:40vh;
  margin:0 auto;
}
.danmaku-wrapper{
  background: white;
  border-radius: 8px;
}
.danmaku1-wrapper{
  background: lightgreen;
  border-radius: 8px;
}
</style>

