const getters = {
  sidebar: state => state.app.sidebar,
  size: state => state.app.size,
  device: state => state.app.device,
  visitedViews: state => state.tagsView.visitedViews,
  cachedViews: state => state.tagsView.cachedViews,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,
  introduction: state => state.user.introduction,
  roles: state => state.user.roles,
  auth: state => state.user.auth,
  permission_routes: state => state.permission.routes,
  errorLogs: state => state.errorLog.logs,

  hasAuth: state => auth => {
    return state.user.auth.some(stateAuth => {
      return stateAuth.children.some(childAuth => childAuth.name === auth)
    })
  }
}
export default getters
