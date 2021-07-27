<template class="fullscreen ">
  <q-page class="flex bg-image flex-center fullscreen">
    <q-card class="absolute-center" style="width: 25%">
      <div class="text-h3 text-center q-my-lg">
        Login
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
          <q-btn label="Login" type="submit" color="primary"/>
          <q-btn label="Not a user?" color="primary" flat class="q-ml-sm" @click="onReg()"/>
        </div>
      </q-form>
    </q-card>
  </q-page>
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

      this.$axios.post('http://127.1:8001/api/login',
        {
          username: this.username,
          password: this.password,
        }).then(function (response) {
        let res = response.data

        if(res.status !== 'Success') {
          _this.$q.notify({
            type: 'negative',
            message: 'Login error: ' + res.message
          })
        } else {
          console.log('eeee')
          sessionStorage.setItem('loggedIn', _this.username)
          sessionStorage.setItem('user_id', res.user_id)
          if(res.is_admin === 1)
            sessionStorage.setItem('role', '1')
          _this.$router.push('/index')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    onReg() {
      this.$router.push('/reg')
    }
  }
}
</script>

<style>
  .bg-image {
    background-image: linear-gradient(to right, #c31432, #240b36)

  }
</style>
