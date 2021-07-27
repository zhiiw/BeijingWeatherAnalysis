<template>
  <q-page class="flex bg-image flex-center">
    <q-input
      filled
      v-model="username"
      label="danmu"
      lazy-rules
      :rules="[ val => val && val.length > 0 || 'Please type your danmu']"
    />
    <q-btn label="Send" @click="onSend" color="primary"/>

    <div id='container'></div>


  </q-page>

</template>
<script>
import easyDanmaku from 'easy-danmaku-js';

let Danmaku;
export default {
  //~~~

  data(){
    return{
      Danmaku,
      username:'',
      danmus:[]
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
  }
  // ~~~
};
</script>
<style>
#container{
  width:600px;
  height:400px;
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
