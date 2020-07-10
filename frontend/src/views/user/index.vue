<template>
  <div class="app-container">
    <el-button type="primary" @click="addUser">Add User</el-button>
    <el-table
      :data="allUserData"
      stripe
      fit
      style="width: 100%; text-align: center;"
    >
      <el-table-column align="center" prop="username" label="Username" />
      <el-table-column
        align="center"
        prop="role"
        label="Role"
      />
      <el-table-column
        align="center"
        prop="email"
        label="E-Mail"
      />
      <el-table-column
        align="center"
        label="Operation"
      >
        <template slot-scope="scope">
          <el-button size="mini" type="primary" @click="editUser(scope)">Edit</el-button>
          <el-button size="mini" type="danger" @click="deleteUser(scope)">Delete</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog :visible.sync="dialogVisible" :title="dialogType==='edit'?'Edit User':'New User'">
      <el-form :model="userInfo" label-width="80px" label-position="left">
        <el-form-item label="Username">
          <el-input v-model="userInfo.username" placeholder="Username" />
        </el-form-item>
        <el-form-item label="Password">
          <el-input v-model="userInfo.password" type="password" placeholder="Password" />
        </el-form-item>
        <el-form-item label="E-Mail">
          <el-input v-model="userInfo.email" placeholder="E-Mail" />
        </el-form-item>
        <el-form-item label="Role">
          <el-input v-model="userInfo.role" placeholder="Role" />
        </el-form-item>
        <el-form-item label="Desc">
          <el-input
            v-model="userInfo.description"
            :autosize="{ minRows: 2, maxRows: 4}"
            type="textarea"
            placeholder="Role Description"
          />
        </el-form-item>

      </el-form>
      <div style="text-align:right;">
        <el-button type="danger" @click="dialogVisible=false">Cancel</el-button>
        <el-button type="primary" @click="confirmRole">Confirm</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import { getUserList } from '@/api/user'
import { deepClone } from '@/utils'
import { addUser, deleteUser, updateUser } from '@/api/role'

const defaultUser = {
  id: '',
  username: '',
  password: '',
  email: '',
  role: ''
}

export default {
  name: 'Index',
  data() {
    return {
      allUserData: [],
      dialogVisible: false,
      userInfo: Object.assign({}, defaultUser),
      dialogType: '',
      routes: [],
      defaultProps: {
        children: 'children',
        label: 'title'
      }

    }
  },
  computed: {
    routesData() {
      return this.routes
    }
  },
  created() {
    this.getUserList()
  },
  methods: {
    async confirmRole() {
      console.log(this.userInfo)
      let message = ''
      const isEdit = this.dialogType === 'edit'
      if (isEdit) {
        await updateUser(this.userInfo['id'], this.userInfo)
      } else {
        await addUser(this.userInfo)
      }
      const { username } = this.userInfo
      this.dialogVisible = false
      if (isEdit) {
        message = `Username: ${username} information has updated!`
      } else {
        message = `Username: ${username} information has added!`
      }

      this.$notify({
        title: 'Success',
        dangerouslyUseHTMLString: true,
        message: `
            <div>${message}</div>
          `,
        type: 'success'
      })
      await this.getUserList()
    },
    addUser() {
      this.userInfo = deepClone(defaultUser)
      this.dialogVisible = true
      this.dialogType = 'new'
    },
    editUser(scope) {
      this.dialogType = 'edit'
      this.dialogVisible = true
      this.userInfo = deepClone(scope.row)
      console.log(scope)
    },
    deleteUser({ $index, row }) {
      this.$confirm('Confirm to remove the user?', 'Warning', {
        confirmButtonText: 'Confirm',
        cancelButtonText: 'Cancel',
        type: 'warning'
      })
        .then(async() => {
          await deleteUser(row.id)
          this.$message({
            type: 'success',
            message: 'Delete succeed!'
          })
          await this.getUserList()
        })
        .catch(err => { console.error(err) })
    },
    async getUserList() {
      const res = await getUserList()
      this.allUserData = res.data.users
      console.log(this.allUserData)
    }

  }
}
</script>

<style scoped>
  .el-table {

  }
</style>
