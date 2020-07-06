import Vue from 'vue'
import './plugins/fontawesome'

import Home from "./views/Home";
import './plugins/element.js'
import axios from "axios"

import VeLine from "v-charts/lib/line"



Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.component(VeLine.name, VeLine)




new Vue({
  render: h => h(Home),
}).$mount('#app')
