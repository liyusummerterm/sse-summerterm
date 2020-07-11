<template>
  <div class="app-container">
    <div v-if="user">
      <el-row :gutter="20">

        <el-col :span="6" :xs="24">
          <user-card :user="user" />
        </el-col>

        <el-col :span="18" :xs="24">
          <el-card>
            <el-tabs v-model="activeTab">
              <el-tab-pane label="Account" name="account">
                <account :user="user" />
              </el-tab-pane>
              <el-tab-pane label="Avatar" name="avatar">
                <el-button type="primary" @click="show=true">Upload Avatar</el-button>
                <avatar-upload
                  v-model="show"
                  field="img"
                  :width="300"
                  :height="300"
                  url="http://127.0.0.1:5000/api/upload"
                  :headers="headers"
                  img-format="png"
                  :with-credentials="false"
                  @crop-upload-success="cropUploadSuccess"
                />
              </el-tab-pane>
            </el-tabs>
          </el-card>
        </el-col>

      </el-row>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import UserCard from './components/UserCard'
import Account from './components/Account'
import { updateAvatar } from '@/api/user'

export default {
  name: 'Profile',
  components: { UserCard, Account },
  data() {
    return {
      user: {},
      activeTab: 'account',
      show: false,
      headers: { 'Authorization': '5Elz35ckLkjBKMurwW3FwiJ8wookBrds' },
      params: ''
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'avatar',
      'roles'
    ])

  },
  created() {
    this.getUser()
  },
  methods: {
    async getUser() {
      this.user = {
        name: this.name,
        role: this.roles.join(' | '),
        email: 'admin@test.com',
        avatar: this.avatar
      }
    },
    cropUploadSuccess(jsonData, field) {
      console.log('-------- upload success --------')
      console.log(jsonData)
      console.log('field: ' + field)
      this.$store.commit('user/SET_AVATAR', jsonData.data.url)
      this.user.avater = jsonData.data.url
      updateAvatar({
        'avatar': this.user.avater
      })
      // this.$router.push({ path: '/permission/index?' + +new Date() }) TODO this might work
      location.reload()
    }

  }
}
</script>
