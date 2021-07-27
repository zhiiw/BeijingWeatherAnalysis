<template>
  <q-page class="flex column" :class="bgclass">
    <div class="col q-pt-lg q-px-md">
      <q-input bottom-slots v-model="search" placeholder="Location" v-on:keyup.enter="searchWeather" dark borderless>
        <template v-slot:prepend >
          <q-icon name="place" />
        </template>
        <template v-slot:append>
          <q-icon name="close" @click="text = ''" class="cursor-pointer" />
        </template>
      </q-input>
    </div>
    <template v-if="true">
      <div class="col text-white text-center">
        <div class="text-h3 text-weight-light">
          {{ city }}
        </div>
        <br>
        <div class="text-h4 text-weight-light">
          {{ weatehr }}
        </div>
        <br>
        <div class="text-h2 text-weight-light">
          {{ Math.round(tmin) }}&deg;C / {{ Math.round(tmax) }}&deg;C
        </div>
        <div class="col text-center">
          <img :src="`https://openweathermap.org/img/wn/${icon }@2x.png`">
        </div>
        <div class="text-h6 text-weight-light">
          Wind Speed:1
        </div>
        <div class="text-h6 text-weight-light">
          Cloths: {{wearing}}
        </div>
        <div class="text-h6 text-weight-light">
          Travel: {{travel}}
        </div>

      </div>
    </template>
    <div class="col skyline"></div>

  </q-page>
</template>

<script>
export default {
  name: 'PageIndex',
  data() {
    return {
      loggedIn: true,
      username: '',
      user_id: -1,
      isAdmin: false,
      search: '',
      weatherData:null,
      tmin:0,
      tmax:0,
      tavg:0,
      weatehr:'',
      city:'',
      date:'',
      wearing:'',
      travel:'',
      icon:'',
      apiUrl:'api.openweathermap.org/data/2.5/weather?q='
    }
  },
  computed:{
    bgclass(){
      if (this.weatherData){
        if (this.weatherData.weather[0].icon.endsWith('n')){
          return 'bg-night'
        }else {
          return 'bg-day'
        }
      }
    }
  },
  created() {
    /*
    this.$axios(`https://api.openweathermap.org/data/2.5/weather?q=Beijing&appid=ef1942f6f1f4a6fc239f6a48c0b47a38&units=metric`).then(response=>{
    console.log('response',response)
    this.weatherData=response.data
    })*/
    this.loggedIn = sessionStorage.getItem('loggedIn') !== null
    if(this.loggedIn) {
      if(this.$route.path === '/' || this.$route.path === '/reg')
        this.$router.push('/index')
    }
    else {
      if(this.$route.path !== '/' && this.$route.path !== '/reg')
        this.$router.push('/')
    }
    this.username = sessionStorage.getItem('loggedIn')
    this.user_id = sessionStorage.getItem('user_id')
    this.isAdmin = sessionStorage.getItem('role') === '1'
    this.tmin=sessionStorage.getItem('tmin')
    this.tmax=sessionStorage.getItem('tmax')
    this.tavg=sessionStorage.getItem('tavg')
    this.weatehr=sessionStorage.getItem('weather')
    if (this.weatehr==="sunny"){
      this.icon="01d"
    }else if (this.weatehr==="cloudy"){
      this.icon="04d"
    }else if (this.weatehr==="rainy"){
      this.icon="09d"
    }
    this.wearing=sessionStorage.getItem('wearing')
    this.travel=sessionStorage.getItem('travel')
    this.city=sessionStorage.getItem('city')
    this.date=sessionStorage.getItem('date')

  },
  mounted() {
    let _this = this
    /*this.$axios.get('http://192.168.43.78:8001/api/random').then(function (response) {
      console.log(response)
      let res = response.data
      _this.random_house_decoration = res.decoration
      _this.random_house_price = res.price
      _this.random_house_unit_type = res.unit_type
      _this.random_house_id = res.house_id
    })*/
  },
  methods: {
    goRandom() {
      //this.$router.push({name: 'info', params: {id: this.random_house_id}})
    },
    searchWeather() {
      this.$q.loading.show()
      this.$axios(`https://api.openweathermap.org/data/2.5/weather?q=${this.search}&appid=ef1942f6f1f4a6fc239f6a48c0b47a38&units=metric`).then(response=>{
        console.log('response',response)
        this.weatherData=response.data
        this.$q.loading.hide()
      }).catch(err=>{
        if (err.response.status===404){
          this.$q.loading.hide()
          this.$q.notify({
            type: 'warning',
            message: 'Please input the correct city name.'
          })
        }
        })
      }
    }
}
</script>

<style lang="sass">
  .q-page
    background-image: linear-gradient(to right, #c31432, #240b36)

  .skyline
    flex: 0 0 100px
    background: url("../static/ee.png")
    background-size: contain
    background-position: bottom center
</style>
