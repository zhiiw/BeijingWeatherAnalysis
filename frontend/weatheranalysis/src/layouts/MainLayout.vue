<template>
  <q-layout view="hHh lpR fFf" >

    <q-header elevated className="bg-blue-grey-9 text-white" height-hint="98">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          icon="menu"
          aria-label="Menu"
        />
        <q-toolbar-title>
          Weather Analysis
        </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-primary text-white"
    >
      <q-list>
        <q-item to="/cal" active-class="q-item-no-link-highlighting">
          <q-item-section avatar>
            <q-icon name="dashboard"/>
          </q-item-section>
          <q-item-section>
            <q-item-label>Calendar</q-item-label>
          </q-item-section>
        </q-item>
        <q-item to="/temperature" active-class="q-item-no-link-highlighting">
          <q-item-section avatar>
            <q-icon name="thermostat"/>
          </q-item-section>
          <q-item-section>
            <q-item-label>Temperature Forecast</q-item-label>
          </q-item-section>
        </q-item>
        <q-item to="/wind" active-class="q-item-no-link-highlighting">
          <q-item-section avatar>
            <q-icon name="water"/>
          </q-item-section>
          <q-item-section>
            <q-item-label>Temperature Forecast(LSTM)</q-item-label>
          </q-item-section>
        </q-item>

        <q-item to="/About" active-class="q-item-no-link-highlighting">
        <q-item-section avatar>
          <q-icon name="face"/>
        </q-item-section>
        <q-item-section>
          <q-item-label>About us</q-item-label>
        </q-item-section>
        </q-item>
        <q-item to="/login" @click="onLogout" active-class="q-item-no-link-highlighting">
          <q-item-section avatar>
            <q-icon name="logout"/>
          </q-item-section>
          <q-item-section>
            <q-item-label>Logout</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container style="padding-top: 0">
      <router-view/>
    </q-page-container>

  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      leftDrawerOpen: false,
      loggedIn: false
    }
  },
  created() {
    this.loggedIn = sessionStorage.getItem('loggedIn') !== null
    const timer = setInterval(() => {
      this.checkLogin();
    }, 500)
  },
  methods: {

    onLogout() {
      console.log('logout')
      sessionStorage.removeItem('loggedIn')
      sessionStorage.removeItem('userid')
      sessionStorage.removeItem('role')
      this.loggedIn = true
      this.$router.replace('/')
    },
    checkLogin() {
      this.loggedIn = sessionStorage.getItem('loggedIn') !== null
      if(this.loggedIn) {
        if(this.$route.path === '/' || this.$route.path === '/reg')
          this.$router.push('/cal')
      }
      else {

        if(this.$route.path !== '/' && this.$route.path !== '/reg')
          this.$router.push('/login')
      }
    }
  }
}
</script>
