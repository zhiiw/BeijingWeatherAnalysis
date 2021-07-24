<template>
  <router-view />
</template>
<script>
import { defineComponent } from 'vue';
import 'echarts/lib/component/markLine';
import 'echarts/lib/component/markPoint';
import 'echarts/lib/component/markArea';
import 'echarts/lib/component/visualMap';
import 'echarts/lib/component/dataZoom';
import 'echarts/lib/component/toolbox';
import 'echarts/lib/component/title';
import 'zrender/lib/svg/svg';
import 'v-charts/lib/style.css';
export default defineComponent({
  name: 'App'
})
</script>
