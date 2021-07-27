<template>
  <q-page>
    <div id="q-app" style="min-height: 100vh;">
      <q-select v-model="model" class="absolute-top-left" :options="options" label="Standard"
                model-value="Beijing"></q-select>
      <div class="q-pa-md">
        <q-date
          v-model="date"
          landscape
          class="fa-1x"
          navigation-min-year-month="2021/07/14"
          navigation-max-year-month="2022/12/31"
          @click="trunToIndex"
          model-value='2021/07/24'></q-date>
      </div>
    </div>
  </q-page>
</template>
<script>
export default {
  name: 'calendar',
  data() {
    return {
      confirm: false,
      model: "Beijing",
      options: ["Shanghai", "Guangzhou", "Tianjin", "Harbin", "Nanjing", "Hefei", "Chongqing", "Xian", "Hangzhou", "Beijing"],
      date: '2021/07/24'
    }
  },
  methods: {
    trunToIndex() {
      let _this = this
      this.$q.dialog({
        title: 'Jump?',
        message: 'Are you sure to turn to this page'
      }).onOk(() => {
        this.$axios.post('http://192.168.43.78:8001/api/everyday',//from here get the value
          {
            city: this.model.toUpperCase(),
            date: this.date,
          }).then(function (response) {
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
          _this.$router.push('/index')

        }).catch(function (error) {
          console.log(error)
        })
      }).onCancel(() => {
        return
      }).onDismiss(() => {
        return
      })

    }

  }
}
</script>

<style scoped>

</style>
