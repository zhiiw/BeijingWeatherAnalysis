<template>
  <q-page :class="bgclass">
    <div class="text-h3 text-weight-light flex flex-center text-white" style="height: 30vh">
      Weather Query
    </div>
    <div id="q-app" style="min-height: 50vh;">
      <q-select filled color="purple-12" v-model="model" class="absolute-top-left" :options="options" label="City" style="color: aliceblue" label-color="white"
                ></q-select>
      <div class="q-pa-md absolute-center " style="">
        <q-date
          style="width: 80vh;
                height:50vh;"
          v-model="date"
          landscape
          class="fa-3x"
          navigation-min-year-month="2021/07/14"
          navigation-max-year-month="2022/12/31"
          color="purple"
          model-value='2021/07/28'></q-date>
      </div>
    </div>
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-fab
        icon="keyboard_arrow_right"
        @click="trunToIndex"
        color="accent"
      >
      </q-fab>
    </q-page-sticky>
  </q-page>
  <div class="col skyline"></div>

</template>
<script>
export default {
  name: 'calendar',
  data() {
    return {
      confirm: false,
      model: "Beijing",
      options: ["Shanghai", "Guangzhou", "Tianjin", "Harbin", "Nanjing", "Hefei", "Chongqing", "Xian", "Hangzhou", "Beijing"],
      date: '2021/07/28'
    }
  },
  created(){
    this.$q.loading.hide()

  },
  methods: {
    trunToIndex() {
      let _this = this

      this.$axios.post('http://192.168.43.78:8001/api/everyday',//from here get the value
        {
          city: this.model.toUpperCase(),
          date: this.date,
        }).then(function (response)
      {
        let res = response.data
        console.log(res)
        sessionStorage.setItem('tmin', res.tmin)
        sessionStorage.setItem('tmax', res.tmax)
        sessionStorage.setItem('tavg', res.tavg)
        sessionStorage.setItem('wearing', res.wearing)
        sessionStorage.setItem('weather', res.weather)
        sessionStorage.setItem('travel', res.travel)
        sessionStorage.setItem('city', res.city)
        sessionStorage.setItem('date', res.date)
        sessionStorage.setItem('windspeed', res.windspeed)
        sessionStorage.setItem('RH', res.RH)

        _this.$router.push('/index')
        this.$q.loading.hide()


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
