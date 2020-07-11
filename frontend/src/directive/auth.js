const auth = value => {
  let auth
  if (typeof value === 'string') {
    auth = this.$store.getters['permission/hasAuthorization'](value)
  } else {
    auth = value.some(item => {
      return this.$store.getters['permission/hasAuthorization'](item)
    })
  }
  return auth
}
const install = function(Vue) {
  Vue.directive('auth', {
    inserted: (el, binding) => {
      if (!auth(binding.value)) {
        el.remove()
      }
    }
  })
  Vue.prototype.$auth = auth
}

if (window.Vue) {
  window['auth'] = auth
  Vue.use(install); // eslint-disable-line
}
auth.install = install
export default auth

// 注册 v-auth 指令

