<template>
  <q-page>
    <div id="q-app" style="min-height: 100vh;">
      <q-select v-model="model" class="absolute-top-right" :options="options" label="Standard"
                model-value="Beijing"></q-select>
      <div class="q-pa-md">
        <q-date
          v-model="date"
          landscape
          class="fa-1x"
          navigation-min-year-month="2021/07"
          navigation-max-year-month="2021/10"
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
      options: ["Shanghai", "Shenzhen", "Guangzhou", "Tianjing", "Harbin", "Nanjing", "Hefei", "Chongqing", "Xian", "Hangzhou", "Beijing"],
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
        this.$axios.post('http://127.0.0.1:8001/api/login',//from here get the value
          {
            username: this.username,
            password: this.password,
          }).then(function (response) {
          let res = response.data
          sessionStorage.setItem('loggedIn', _this.username)
          sessionStorage.setItem('user_id', res.user_id)
          this.$router.push('/index')
        }).catch(function (error) {
          console.log(error)
        })
        this.routes.push("/index")
      }).onCancel(() => {

      }).onDismiss(() => {

      })
    }
  }
}
</script>

<style scoped>

</style>
