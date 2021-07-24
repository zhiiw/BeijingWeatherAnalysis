<template>
<q-page>
  <div id="q-app" style="min-height: 100vh;">
    <q-select v-model="model" :options="options" label="Standard" model-value="Beijing"></q-select>

    <div class="q-pa-md">
      <q-date
        v-model="date"
        landscape
       model-value='2021/07/24'></q-date>
    </div>
  </div>
</q-page>
</template>

<script>

export default {
  name: 'calendar',
  data(){
    return{
      model:"Beijing",
      options:["shanghai","shenzhen"],
      date:'2021/07/24'
    }
  },
  methods:{
    trunToIndex()
  }
}
</script>

<style scoped>

</style>
