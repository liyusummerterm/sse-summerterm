import Vue from 'vue'
import './plugins/fontawesome'

import Home from "./Home";
import './plugins/element.js'
import axios from "axios"

Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  render: h => h(Home),
}).$mount('#app')
