<template class="fullscreen">
  <q-card class="absolute-center" style="width: 20%">
    <div class="text-h1 text-center q-my-lg">
      Register
    </div>
    <q-form
      @submit="onSubmit"
      class="q-gutter-md q-mt-xl"
    >
      <q-input
        filled
        v-model="username"
        label="Your username *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type your username']"
      />

      <q-input
        filled
        type="password"
        v-model="password"
        label="Your password *"

        lazy-rules
        :rules="[
          val => val !== null && val !== '' || 'Please type your password',
        ]"
      />

      <q-toggle v-model="accept" label="I accept the license and terms" />

      <div class="text-center">
        <q-btn label="Register" type="submit" color="primary"/>
        <q-btn label="Already a user?" color="primary" flat class="q-ml-sm" @click="onLogin()"/>
      </div>
    </q-form>
  </q-card>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      accept: false,
      username: '',
      password: ''
    }
  },
  methods: {
    onSubmit() {
      if(!this.accept) {
        this.$q.notify({
          type: 'warning',
          message: 'License and terms must be accepted!'
        })
        return
      }
      let _this = this
      this.$axios.post('http://127.0.0.1:8001/api/register',
        {
          username: this.username,
          password: this.password
        }).then(function (response) {
        let res = response.data
        if(res.status !== 'Success') {
          _this.$q.notify({
            type: 'negative',
            message: 'Register error: ' + res.message
          })
        } else {
          _this.$router.push('/')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    onLogin() {
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
</style>
<style lang="sass">
.q-page
  background: linear-gradient(to right, #c31432, #240b36) /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
.trees
  flex: 0 0 100px
  background: url(../static/trees.png)
  background-size: contain
  background-position: center bottom
</style>
